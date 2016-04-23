import json
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from .models import Person, Dress, Order
from dress.utils.lists import COLORS


def customer_per_size_json(request):
    ''' JSON used to generate the graphic '''
    ''' Quantidade de clientes por tamanho '''
    pass


def dress_per_color_json(request):
    ''' Quantidade de vestidos por cor '''
    pass


def dress_per_size_json(request):
    ''' Quantidade de vestidos por tamanho '''
    pass


def order_per_day_json(request):
    ''' Quantidade de pedidos por dia '''
    pass
