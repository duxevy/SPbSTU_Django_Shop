from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(in_stock=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Категория',
        verbose_name_plural = 'Катигории'

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created', '-in_stock',)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return self.title
