from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegistrationForm


class UserRegisterView(generic.CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    # success_url = reverse_lazy('login') # desable for modal
