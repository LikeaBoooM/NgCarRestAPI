from django.test import TestCase
from ngapp.forms import NewCarForm, NewRateForm

class TestForms(TestCase):

    def test_new_car_form_valid_data(self):
        form = NewCarForm(data={
            'mark' : 'Audi',
            'model' : 'A5'
        })

        self.assertTrue(form.is_valid())

    def test_new_car_form_no_data(self):
        form = NewCarForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)