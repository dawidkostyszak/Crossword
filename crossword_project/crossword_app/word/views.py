import json
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db import DatabaseError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from ..views import LoginRequiredMixin
from models import Word, Question
from form import WordForm
from ..form import CrosswordForm
from django.views.generic import FormView, ListView, TemplateView


class Words(TemplateView):
    template_name = "word/words_list.html"
    form_class = CrosswordForm

    def get_context_data(self, **kwargs):
        context = super(Words, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


class WordsList(ListView):
    model = Word
    form_class = CrosswordForm

    def get(self, request, *args, **kwargs):
        offset = int(self.request.GET.get('offset', 0))
        limit = int(self.request.GET.get('limit', 20))
        response_data = {
            'max': self.model.objects.all().count(),
            'words': [
                {
                    'word': word.name,
                    'question': word.question.question,
                    'difficulty': word.question.difficulty.difficulty
                }
                for word in self.model.objects.all()[offset:limit]
            ],
            'questions': [
                {
                    'question': question.question,
                    'difficulty': question.difficulty.difficulty
                }
                for question in Question.objects.all()[offset:limit]
            ]
        }

        return HttpResponse(json.dumps(response_data), content_type="application/json")


class WordAdd(LoginRequiredMixin, FormView):
    template_name = "word/add_word.html"
    form_class = WordForm

    def form_valid(self, form):
        return super(FormView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                word_name = data['name']
                question, question_exist = Question.objects.get_or_create(
                    question=data['question'],
                    difficulty=data['difficulty']
                )
                if not question_exist:
                    question.save()

                word = Word(
                    name=word_name,
                    question=question
                )
                question.word_set.add(word)

            except DatabaseError:
                return render(request, self.template_name, {'form': form})

            return HttpResponseRedirect(reverse('words'))

        return render(request, self.template_name, {'form': form})