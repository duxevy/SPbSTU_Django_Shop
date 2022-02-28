from django.http.response import JsonResponse
from django.shortcuts import render

from basket.basket import Basket
from .forms import OrderCreateForm

from .models import Order, OrderItem


def add(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in basket:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['qty']
                )
            basket.clear()
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'basket': basket,
                   'form': form})
