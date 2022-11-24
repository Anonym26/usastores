from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    Класс OrderItemInline.
    Включает модель OrderItem в качестве inline встроенного в класс OrderAdmin.
    """
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    """
    Класс OrderAdmin.
    """
    list_display = ['id', 'customer', 'first_name', 'last_name', 'email', 'phone_number',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', 'status']
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['email', 'phone_number',
                     'address', 'status']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
