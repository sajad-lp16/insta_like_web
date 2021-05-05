from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login

from .import forms


class RegisterView(generic.FormView):
    form_class = forms.RegisterationForm
    template_name = 'register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(generic.FormView):
    form_class = forms.LoginForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request,form.cleaned_data['user'])
        return super().form_valid(form)
