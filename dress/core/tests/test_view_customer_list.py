from django.test import TestCase
from django.shortcuts import resolve_url as r
from dress.core.models import Customer
from .data import CUSTOMER_DICT


class CustomerListGet(TestCase):

    def setUp(self):
        self.obj = Customer.objects.create(**CUSTOMER_DICT)
        self.resp = self.client.get(r('core:customer_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/customer_list.html')

    def test_html(self):
        contents = [
            (1, 'Mariana Cruz'),
            (1, 'm.cruz@example.com'),
            (2, 'São Paulo'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)


class CustomerGetEmpty(TestCase):

    def test_get_empty(self):
        response = self.client.get(r('core:customer_list'))

        self.assertContains(response, 'Sem itens na lista.')
