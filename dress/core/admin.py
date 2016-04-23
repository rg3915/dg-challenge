from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from .models import Customer, Dress, Order
from .forms import CustomerForm, DressForm, OrderForm


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone', 'city', 'uf',
                    'person_height', 'person_size', 'created')
    date_hierarchy = 'created'
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = (
        # 'uf',
        ('created', DateRangeFilter),
    )
    form = CustomerForm


@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    list_display = ('dress_model', 'stylist', 'color',
                    'dress_height', 'dress_size', 'created')
    date_hierarchy = 'created'
    search_fields = ('dress_model', 'stylist')
    list_filter = (
        'color',
        ('created', DateRangeFilter),
    )
    form = DressForm


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'dress', 'price', 'created')
    date_hierarchy = 'created'
    search_fields = ('customer', 'dress')
    list_filter = (
        ('created', DateRangeFilter),
    )
    form = OrderForm
