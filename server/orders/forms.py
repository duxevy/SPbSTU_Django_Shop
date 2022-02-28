from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name',
                  'email',
                  'address1',
                  'address2',
                  'city',
                  'phone',
                  'post_code']
