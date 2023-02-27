from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password', 'role']


class AuthForm(forms.Form):
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
