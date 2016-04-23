from django.test import TestCase
from django.shortcuts import resolve_url as r
from dress.core.models import Customer
from .data import CUSTOMER_DICT


class CustomerDetailGet(TestCase):

    def setUp(self):
        self.obj = Customer.objects.create(**CUSTOMER_DICT)
        self.resp = self.client.get(r('core:customer_detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'core/customer_detail.html')

    def test_context(self):
        customer = self.resp.context['customer']
        self.assertIsInstance(customer, Customer)

    def test_html(self):
        contents = (self.obj.full_name,
                    self.obj.email,
                    self.obj.phone,
                    self.obj.address,
                    self.obj.complement,
                    self.obj.district,
                    self.obj.city,
                    self.obj.uf,
                    self.obj.cep,
                    self.obj.bust,
                    self.obj.hip,
                    self.obj.waist,
                    self.obj.heel,
                    self.obj.person_size,
                    )

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class CustomerDetailNotFound(TestCase):

    def test_not_found(self):
        resp = self.client.get(r('core:customer_detail', 0))
        self.assertEqual(404, resp.status_code)
