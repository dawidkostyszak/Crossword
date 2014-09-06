from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpResponse


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

    def get(self, request, *args, **kwargs):
        crossword = [
            ['', '', '', 'K', 'A', 'R', 'O', 'L'],
            ['', 'A', 'D', 'A', 'M', '', '', ''],
            ['M', 'A', 'D', 'Z', 'I', 'A', '', ''],
            ['', '', '', 'I', 'G', 'A', '', ''],
            ['', '', '', 'O', 'L', 'A', 'F', '']
        ]
        return render(request, self.template_name, {'crossword': crossword})