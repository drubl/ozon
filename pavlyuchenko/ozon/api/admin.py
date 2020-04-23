from django.contrib import admin

from api.cart.infrastructure.models import Cart
from api.customer.infrastructure.models import Customer
from api.purchase.infrastructure.models import Purchase
from api.product.infrastructure.models import Product
from api.category.infrastructure.models import Category

admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Category)