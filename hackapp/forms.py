from django.forms import ModelForm
from django import forms
from .models import Signin


class SigninForm(forms.ModelForm):
    email= forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    class Meta:
        model = Signin
        fields = ('email', 'password')