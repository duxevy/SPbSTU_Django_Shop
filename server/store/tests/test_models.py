from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    def test_category_url(self):
        data = self.data1
        response = self.client.post(
            reverse('category_list', args=[data.slug]))
        self.assertEqual(response.status_code, 200)


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        self.data1 = Product.objects.create(
            category_id=1,
            title='django beginners',
            slug='django-beginners',
            price='20000',
            image='django')
        self.data2 = Product.objects.create(
            category_id=1,
            title='django adv',
            slug='django-adv',
            price='40000',
            image='django',
            in_stock=False)

    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')

    def test_products_url(self):
        data = self.data1
        url = reverse('product_detail', args=[data.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('product_detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

    def test_products_custom_manager_basic(self):
        data = Product.products.all()
        self.assertEqual(data.count(), 1)
