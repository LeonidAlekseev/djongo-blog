from django.views import generic
from django.contrib.auth import forms
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
