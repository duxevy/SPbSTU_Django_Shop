from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='admin')
        Category.objects.create(
            name='django',
            slug='django')
        Product.objects.create(
            category_id=1,
            title='django beginners',
            slug='django-beginners',
            price='20000',
            image='django')

    def test_product_detail_url(self):
        response = self.c.get(
            reverse('product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        response = self.c.get(
            reverse('category_list', args=['django']))
        self.assertEqual(response.status_code, 200)
