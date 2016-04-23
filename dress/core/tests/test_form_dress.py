from django.test import TestCase
from dress.core.forms import DressForm
from .data import DRESS_DICT


class DressFormTest(TestCase):

    def test_form_has_fields(self):
        ''' Form must have 5 fields '''
        form = DressForm()
        expected = ['dress_model', 'stylist',
                    'color', 'dress_height', 'dress_size']
        self.assertSequenceEqual(expected, list(form.fields))

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        data = dict(**DRESS_DICT, **kwargs)
        form = DressForm(data)
        form.is_valid()
        return form
