from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'zip_code',
                  'email', 'password1', 'password2',)
