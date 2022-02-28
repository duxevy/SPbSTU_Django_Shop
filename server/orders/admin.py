from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name',
                    'email',
                    'address1',
                    'address2',
                    'city',
                    'phone',
                    'post_code',
                    'created']
    list_filter = ['created']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
