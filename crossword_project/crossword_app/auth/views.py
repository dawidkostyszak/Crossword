from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, RedirectView
from form import LoginForm


class LoginView(FormView):
    template_name = "auth/login.html"
    form_class = LoginForm

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {'form': 'cos'})
    def form_valid(self, form):
        return super(FormView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(username=form_data['email'], password=form_data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('words_list'))
        return render(request, self.template_name, {'form': form, 'error': 'Username or password are incorrect'})


class LogoutView(RedirectView):

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))