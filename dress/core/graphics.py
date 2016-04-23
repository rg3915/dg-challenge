import json
import datetime
import itertools
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from .models import Customer, Dress, Order


def customer_per_size_json(request):
    ''' JSON used to generate the graphic '''
    ''' Quantidade de clientes por tamanho '''
    data = Customer.objects.values('person_size')\
        .annotate(quant=Count('person_size'))\
        .order_by('person_size').values('person_size', 'quant')
    '''
    Precisa reescrever a lista com os campos do gráfico,
    que são: 'tamanho' e 'quant'.
    '''
    lista = [{'tamanho': i['person_size'], 'quant':i['quant']} for i in data]
    ''' 'quant':i['quant'] não era necessário, mas ... '''
    resp = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(resp)


def dress_per_color_json(request):
    ''' Quantidade de vestidos por cor '''
    data = Dress.objects.values('color')\
        .annotate(quant=Count('color'))\
        .order_by('color').values('color', 'quant')
    ''' Reescrevendo a lista '''
    lista = [{'cor': i['color'], 'quant':i['quant']} for i in data]
    resp = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(resp)


def dress_per_size_json(request):
    ''' Quantidade de vestidos por tamanho '''
    data = Dress.objects.values('dress_size')\
        .annotate(quant=Count('dress_size'))\
        .order_by('dress_size').values('dress_size', 'quant')
    ''' Reescrevendo a lista '''
    lista = [{'tamanho': i['dress_size'], 'quant':i['quant']} for i in data]
    resp = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(resp)


def order_per_day_json(request):
    ''' Quantidade de pedidos por dia '''
    qs = Order.objects.values('created').values('created')
    grouped = itertools.groupby(
        qs, lambda d: d.get('created').strftime('%Y-%m-%d'))
    data = [{'dia': day, 'quant': len(list(this_day))}
            for day, this_day in grouped]
    resp = json.dumps(data, cls=DjangoJSONEncoder)
    return HttpResponse(resp)
