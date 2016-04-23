from django import forms
from .models import Customer, Dress, Order


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'address', 'complement', 'district', 'city', 'uf', 'cep',
                  'person_height', 'bust', 'hip', 'waist', 'heel', 'person_size']


class DressForm(forms.ModelForm):

    class Meta:
        model = Dress
        fields = ['dress_model', 'stylist',
                  'color', 'dress_height', 'dress_size']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['customer', 'dress', 'price']
