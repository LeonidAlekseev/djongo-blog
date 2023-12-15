from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    avatar = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    father_name = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'avatar', 'first_name', 'last_name', 'father_name')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        if commit:
            user.save()

            user_profile = Profile(
                user=user,
                avatar=self.cleaned_data.get('avatar'),
                first_name=self.cleaned_data.get('first_name'),
                last_name=self.cleaned_data.get('last_name'),
                father_name=self.cleaned_data.get('father_name'),
            )
            user_profile.save()

        return user
