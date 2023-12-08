from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        