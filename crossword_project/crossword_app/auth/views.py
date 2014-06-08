from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, RedirectView
from form import LoginForm, RegistryForm


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
        form.errors['__all__'] = 'Username or password are incorrect'
        return render(request, self.template_name, {'form': form})


class LogoutView(RedirectView):

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class RegistryView(FormView):
    template_name = 'auth/registry.html'
    form_class = RegistryForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data
            try:
                user = User(
                    username=form_data['username'],
                    password=form_data['password'],
                    first_name=form_data['first_name'],
                    last_name=form_data['last_name']
                )
                user.save()
            except IntegrityError as e:
                # raise forms.ValidationError("Passwords don't match")
                form.errors['__all__'] = "User with that username exist"
                return render(request, self.template_name, {'form': form})

            if user:
                return HttpResponseRedirect(reverse('login'))
        return render(request, self.template_name, {'form': form})
