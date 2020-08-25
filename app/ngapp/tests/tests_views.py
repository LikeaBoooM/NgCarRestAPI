from django.test import TestCase, Client
from django.urls import reverse
from ngapp.models import Car, Rate
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.rate_url = reverse('rates', args=[1])
        self.car1 = Car.objects.create(mark='Audi',model='A5')
        self.cars = Car.objects.all().count()
        car_1 = Car.objects.filter(model='A5').first()

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ngapp/home.html')

    def test_index_POST(self):
        response = self.client.post(self.index_url, {
            'mark' : 'Audi',
            'model' : 'A5',
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.car1.mark, 'Audi')
        self.assertEquals(self.car1.model, 'A5')

    def test_index_POST_no_data(self):
        response = self.client.post(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.cars, 1) ## we are setting one car at setUP
    
    def test_rate_GET(self):
        response = self.client.get(self.rate_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ngapp/rate.html')

    def test_rate_POST_add_car(self):
        Rate.objects.create(grade=5, car=self.car1)

        response = self.client.post(self.rate_url, {
            'car' : 'Audi A5',
            'grade' : '5'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.car1.mark, 'Audi')