from datetime import datetime
from django.test import TestCase
from django.shortcuts import resolve_url as r
from dress.core.models import Customer
from .data import CUSTOMER_DICT


class CustomerModelTest(TestCase):

    def setUp(self):
        self.obj = Customer(**CUSTOMER_DICT)
        self.obj.save()

    def test_create(self):
        self.assertTrue(Customer.objects.exists())

    def test_created_at(self):
        ''' Customer must have an auto created_at attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('Mariana Cruz', str(self.obj))

    def test_get_absolute_url(self):
        url = r('core:customer_detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())
