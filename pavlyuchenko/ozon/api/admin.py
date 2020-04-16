from django.contrib import admin

from api.models import (
    Product,
    Cart,
    Customer,
    Purchase
)

admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Product)