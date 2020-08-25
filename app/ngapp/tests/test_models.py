from django.test import TestCase

class TestModels(TestCase):

    def setUp(self):
        self.car1 = Car.objects.create(mark='Audi', model='A5')