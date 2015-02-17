from django.contrib import admin

from order.models import Customer, Product, Stock, Order

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Order)
