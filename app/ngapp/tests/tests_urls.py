from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ngapp.views import index, rate, popular

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_rate_url_is_resolved(self):
        url = reverse('rates', args=[1])
        self.assertEquals(resolve(url).func, rate)

    def test_popular_url_is_resolved(self):
        url = reverse('popular')
        self.assertEquals(resolve(url).func, popular)
