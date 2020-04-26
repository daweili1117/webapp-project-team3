from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    postal_code = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
