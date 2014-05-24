from django.core.urlresolvers import reverse
from django.db import DatabaseError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import Word
from form import WordForm
from django.views.generic import FormView, ListView


class WordList(ListView):
    template_name = "word/words_list.html"
    model = Word

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WordList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['words'] = self.model.objects.all()
        return context


class WordAdd(FormView):
    template_name = "word/add_word.html"
    form_class = WordForm

    def form_valid(self, form):
        return super(FormView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                word = Word(name=data['name'], question=data['question'], category=data['category'])
                word.save()
            except DatabaseError:
                return render(request, self.template_name, {'form': form})
            # <process form cleaned data>
            return HttpResponseRedirect(reverse('words_list'))

        return render(request, self.template_name, {'form': form})