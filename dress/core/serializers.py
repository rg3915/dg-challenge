from rest_framework import serializers
from .models import Customer, Dress, Order


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone',
                  'address', 'complement', 'district', 'city', 'uf', 'cep',
                  'person_height', 'bust', 'hip', 'waist', 'heel',
                  'person_size')


class DressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dress
        fields = ('dress_model', 'stylist', 'color',
                  'dress_height', 'dress_size')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('customer', 'dress', 'price')
