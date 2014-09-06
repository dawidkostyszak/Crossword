import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpResponse
from crossword_project.crossword_app.word.models import Word


class HomepageView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse('')


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class CrosswordGenerate(LoginRequiredMixin, TemplateView):
    template_name = "generate_crossword.html"
    model = Word

    def generate_crossword(self, word):
        result = []
        for char in word:
            words = list(self.model.objects.filter(
                name__contains=char
            ).exclude(
                name=word
            ))

            while True:
                if words:
                    word_to_add = random.choice(words)
                else:
                    result = self.generate_crossword(word)
                    return result

                words.remove(word_to_add)
                if not word_to_add.name.upper() in [r[0] for r in result]:
                    result.append(
                        (
                            word_to_add.name.upper(),
                            word_to_add.name.index(char)
                        )
                    )
                    break

        return result

    def format_crossword(self, crossword):
        result = []
        intendation = max([word[1] for word in crossword])
        for row, _ in crossword:
            column_to_add = ['' for i in range(intendation)]
            column_to_add.extend([r for r in row])
            result.append(column_to_add)

        return result

    def get(self, request, *args, **kwargs):
        crossword_result = self.generate_crossword('kazio')
        crossword = self.format_crossword(crossword_result)

        return render(request, self.template_name, {'crossword': crossword})