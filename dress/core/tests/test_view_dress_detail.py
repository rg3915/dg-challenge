from django.test import TestCase
from django.shortcuts import resolve_url as r
from dress.core.models import Dress
from .data import DRESS_DICT


class DressDetailGet(TestCase):

    def setUp(self):
        self.obj = Dress.objects.create(**DRESS_DICT)
        self.resp = self.client.get(r('core:dress_detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'core/dress_detail.html')

    def test_context(self):
        dress = self.resp.context['dress']
        self.assertIsInstance(dress, Dress)

    def test_html(self):
        contents = (self.obj.dress_model,
                    self.obj.stylist,
                    self.obj.color,
                    self.obj.dress_height,
                    self.obj.dress_size,
                    )

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class DressDetailNotFound(TestCase):

    def test_not_found(self):
        resp = self.client.get(r('core:dress_detail', 0))
        self.assertEqual(404, resp.status_code)
