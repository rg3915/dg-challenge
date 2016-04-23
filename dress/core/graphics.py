import json
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from .models import Customer, Dress, Order
from dress.utils.lists import COLORS


def customer_per_size_json(request):
    ''' JSON used to generate the graphic '''
    ''' Quantidade de clientes por tamanho '''
    data = Customer.objects.values('person_size')\
        .annotate(quant=Count('person_size'))\
        .order_by('person_size').values('person_size', 'quant')
    '''
    Precisa reescrever o dicionário com os campos do gráfico,
    que são: 'tamanho' e 'quant'.
    '''
    lista = [{'tamanho': i['person_size'], 'quant':i['quant']} for i in data]
    ''' 'quant':i['quant'] não era necessário, mas ... '''
    resp = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(resp)


def dress_per_color_json(request):
    ''' Quantidade de vestidos por cor '''
    pass


def dress_per_size_json(request):
    ''' Quantidade de vestidos por tamanho '''
    pass


def order_per_day_json(request):
    ''' Quantidade de pedidos por dia '''
    pass
