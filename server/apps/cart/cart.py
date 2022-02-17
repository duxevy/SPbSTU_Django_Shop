from django.db import models
from django.conf import settings
from apps.store.models import Product


class Cart(object):
    def __init__(self, request):
        # Хранение сессии, чтобы сделать их доступными для других методов класса
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        # Iterator through elements in cart and get products from database
        product_ids = self.cart.keys()
        products = Product.object.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Count products in cart
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        # Добавление продукта в корзину
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Session update
        self.session[settings.CART_SESSION_ID] = self.cart
        # Mark session as 'changed'
        self.session.modified = True

    def remove(self):
        # Delete product from cart
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # To delete cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
