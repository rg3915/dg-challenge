# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='endereço')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='complemento')),
                ('district', models.CharField(blank=True, max_length=100, null=True, verbose_name='bairro')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='cidade')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('first_name', models.CharField(max_length=50, verbose_name='nome')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='sobrenome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=20, verbose_name='telefone')),
                ('person_height', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='altura')),
                ('bust', models.PositiveIntegerField(verbose_name='busto')),
                ('hip', models.PositiveIntegerField(verbose_name='quadril')),
                ('waist', models.PositiveIntegerField(verbose_name='cintura')),
                ('heel', models.PositiveIntegerField(verbose_name='salto')),
                ('person_size', models.PositiveIntegerField(verbose_name='tamanho')),
            ],
            options={
                'ordering': ['first_name'],
                'verbose_name_plural': 'clientes',
                'verbose_name': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('dress_model', models.CharField(max_length=50, verbose_name='modelo')),
                ('stylist', models.CharField(max_length=50, verbose_name='estilista')),
                ('color', models.CharField(choices=[('amarelo', 'amarelo'), ('azul', 'azul'), ('branco', 'branco'), ('cinza', 'cinza'), ('coral', 'coral'), ('dourado', 'dourado'), ('estampado', 'estampado'), ('laranja', 'laranja'), ('marrom', 'marrom'), ('nude', 'nude'), ('prata', 'prata'), ('preto', 'preto'), ('rosa', 'rosa'), ('roxo', 'roxo'), ('verde', 'verde'), ('vermelho', 'vermelho'), ('vinho', 'vinho')], max_length=20, verbose_name='cor')),
                ('dress_height', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='altura')),
                ('dress_size', models.PositiveIntegerField(verbose_name='tamanho')),
            ],
            options={
                'ordering': ['dress_model'],
                'verbose_name_plural': 'vestidos',
                'verbose_name': 'vestido',
            },
        ),
    ]
