from django.test import TestCase
from django.shortcuts import resolve_url as r
from dress.core.models import Dress
from .data import DRESS_DICT


class DressListGet(TestCase):

    def setUp(self):
        self.obj = Dress.objects.create(**DRESS_DICT)
        self.resp = self.client.get(r('core:dress_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/dress_list.html')

    def test_html(self):
        contents = [
            (1, 'Maddie'),
            (1, 'Roberto Cavalli'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)


class DressGetEmpty(TestCase):

    def test_get_empty(self):
        response = self.client.get(r('core:dress_list'))

        self.assertContains(response, 'Sem itens na lista.')
