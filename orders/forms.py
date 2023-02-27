from django import forms
from django_countries.fields import CountryField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    shipping_country = CountryField(blank_label='(select country)')

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city', 'address2', 'shipping_country']
