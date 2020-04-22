from django.contrib import admin
from basket.infrastructure.models import Basket, Order

admin.site.register(Order)
admin.site.register(Basket)
