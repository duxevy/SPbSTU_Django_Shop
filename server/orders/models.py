from django.core.validators import RegexValidator
from django.db import models

from store.models import Product


class Order(models.Model):
    postCodeRegex = RegexValidator(regex=r'^[0-9]{6}')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    emailRegex = RegexValidator(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    full_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, validators=[emailRegex])
    address1 = models.CharField(max_length=250, blank=False)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=20, blank=False)
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, blank=False)
    post_code = models.PositiveIntegerField(blank=False, validators=[postCodeRegex])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ',
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
