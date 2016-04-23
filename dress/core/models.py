from django.db import models
from django.shortcuts import resolve_url as r
from localflavor.br.br_states import STATE_CHOICES
from dress.utils.lists import COLORS


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        'modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(
        u'endereço', max_length=100, null=True, blank=True)
    complement = models.CharField(
        'complemento', max_length=100, null=True, blank=True)
    district = models.CharField(
        'bairro', max_length=100, null=True, blank=True)
    city = models.CharField('cidade', max_length=100, null=True, blank=True)
    uf = models.CharField(
        'UF', max_length=2, choices=STATE_CHOICES, null=True, blank=True)
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)

    class Meta:
        abstract = True


class Customer(TimeStampedModel, Address):
    first_name = models.CharField('nome', max_length=50)
    last_name = models.CharField(
        'sobrenome', max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('telefone', max_length=20)
    person_height = models.DecimalField(
        'altura', max_digits=3, decimal_places=2)
    bust = models.PositiveIntegerField('busto')
    hip = models.PositiveIntegerField('quadril')
    waist = models.PositiveIntegerField('cintura')
    heel = models.PositiveIntegerField('salto')
    person_size = models.PositiveIntegerField('tamanho')

    class Meta:
        ordering = ['first_name']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return ' '.join(filter(None, [self.first_name, self.last_name]))

    full_name = property(__str__)

    def get_absolute_url(self):
        return r('core:customer_detail', pk=self.pk)


class Dress(TimeStampedModel):
    dress_model = models.CharField('modelo', max_length=50)
    stylist = models.CharField('estilista', max_length=50)
    color = models.CharField('cor', max_length=20, choices=COLORS)
    dress_height = models.DecimalField(
        'altura', max_digits=3, decimal_places=2)
    dress_size = models.PositiveIntegerField('tamanho')

    class Meta:
        ordering = ['dress_model']
        verbose_name = 'vestido'
        verbose_name_plural = 'vestidos'

    def __str__(self):
        return self.dress_model

    def get_absolute_url(self):
        return r('core:dress_detail', pk=self.pk)


class Order(TimeStampedModel):
    customer = models.ForeignKey('Customer', verbose_name='cliente')
    dress = models.ForeignKey('Dress', verbose_name='vestido')
    price = models.DecimalField('Aluguel', max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['-created']
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return r('core:order_detail', pk=self.pk)
