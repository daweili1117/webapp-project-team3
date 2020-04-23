from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import Reserve
from indianexpress.models import Reservation


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    # phone_number = forms.CharField(max_length=10)
    zip_code = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'zip_code',
                  'email', 'password1', 'password2',)


class ReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    num = forms.CharField(max_length=255)
    date = forms.DateField()
    time = forms.TimeField()
    guests = forms.CharField()
    requests = forms.CharField()

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'num', 'date', 'time', 'guests', 'requests',)
