from datetime import datetime
from django.test import TestCase
from django.shortcuts import resolve_url as r
from dress.core.models import Dress
from .data import DRESS_DICT


class DressModelTest(TestCase):

    def setUp(self):
        self.obj = Dress(**DRESS_DICT)
        self.obj.save()

    def test_create(self):
        self.assertTrue(Dress.objects.exists())

    def test_created_at(self):
        ''' Dress must have an auto created_at attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('Maddie', str(self.obj))

    def test_get_absolute_url(self):
        url = r('core:dress_detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())
