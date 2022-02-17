from django.contrib import admin
from django.conf.locale.ru import formats as ru_formats
from .models import Category, Product

ru_formats.DATE_FORMAT = 'd.m.Y H:i:s'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'is_featured', 'date_added']
    list_filter = ['is_featured', 'date_added']
    list_editable = ['price', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
