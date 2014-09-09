import random
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from word.models import Word


class HomepageView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('words_list'))


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class CrosswordGenerate(LoginRequiredMixin, TemplateView):
    template_name = "generate_crossword.html"
    model = Word

    def generate_crossword(self, word, difficulty, max_loop=100):
        result = []
        for char in word:
            words = list(self.model.objects.filter(
                name__icontains=char,
                question__difficulty=difficulty
            ).exclude(
                name__iexact=word
            ))

            while True:
                if words:
                    word_to_add = random.choice(words)
                else:
                    if max_loop == 0:
                        return {
                            "success": False,
                            "result": "Can't generate crossword"
                        }
                    result = self.generate_crossword(
                        word,
                        difficulty,
                        max_loop=max_loop-1
                    )
                    return result

                words.remove(word_to_add)
                if not word_to_add.name.upper() in [r[0] for r in result]:
                    name = word_to_add.name.upper()
                    result.append(
                        (
                            name,
                            name.index(char.upper()),
                            word_to_add.question
                        )
                    )
                    break

        return {
            "success": True,
            "result": result
        }

    def format_crossword(self, crossword):
        result = []
        intendation = max([word[1] for word in crossword['result']])
        for row, index, _ in crossword['result']:
            column_to_add = [('', False) for i in range(intendation - index)]
            column_to_add.extend(
                [(row[r],  r == index) for r in range(row.__len__())]
            )
            result.append(column_to_add)

        crossword['result'] = result
        return crossword

    def post(self, request, *args, **kwargs):
        word = request.POST.get('word', None)
        difficulty = request.POST.get('difficulty', None)
        if not word or not difficulty:
            return render(
                request,
                self.template_name,
                {
                    'crossword': {
                        'success': False,
                        'result': 'Please put word and difficulty to generate '
                                  'crossword'
                    },
                    'word': word
                }
            )

        crossword_result = self.generate_crossword(word, difficulty)
        if crossword_result['success']:
            crossword_result = self.format_crossword(crossword_result)

        return render(
            request,
            self.template_name,
            {
                'crossword': crossword_result,
                'word': word,
                'difficulty': difficulty
            }
        )