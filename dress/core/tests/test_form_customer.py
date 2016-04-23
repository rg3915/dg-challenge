from django.test import TestCase
from dress.core.forms import CustomerForm
from .data import CUSTOMER_DICT


class CustomerFormTest(TestCase):

    def test_form_has_fields(self):
        ''' Form must have 16 fields '''
        form = CustomerForm()
        expected = ['first_name', 'last_name', 'email', 'phone',
                    'address', 'complement', 'district', 'city', 'uf', 'cep',
                    'person_height', 'bust', 'hip', 'waist', 'heel',
                    'person_size']
        self.assertSequenceEqual(expected, list(form.fields))

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        data = dict(**CUSTOMER_DICT, **kwargs)
        form = CustomerForm(data)
        form.is_valid()
        return form
