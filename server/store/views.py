from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    return render(request, 'home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'products/category.html', {'category': category})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'products/single.html', {'product': product})


def contact(request):
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')
