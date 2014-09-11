from django.core.urlresolvers import reverse
from django.db import DatabaseError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..views import LoginRequiredMixin
from models import Word, Question
from form import WordForm
from ..form import CrosswordForm
from random import sample
from django.views.generic import FormView, ListView


class WordList(ListView):
    template_name = "word/words_list.html"
    model = Word
    form_class = CrosswordForm

    def get_context_data(self, **kwargs):
        context = super(WordList, self).get_context_data(**kwargs)
        count_words = self.model.objects.all().count()
        count_question = Question.objects.all().count()
        rand_ids_word = sample(xrange(1, count_words), 20)
        rand_ids_question = sample(xrange(1, count_question), 20)
        context['words'] = self.model.objects.filter(id__in=rand_ids_word)
        context['questions'] = Question.objects.filter(id__in=rand_ids_question)
        return context


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

            return HttpResponseRedirect(reverse('words_list'))

        return render(request, self.template_name, {'form': form})