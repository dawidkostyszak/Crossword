from django.views.generic import TemplateView
from django.http import HttpResponse


class HomepageView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse('')
