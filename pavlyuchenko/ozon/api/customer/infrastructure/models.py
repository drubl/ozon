from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from api.cart.infrastructure.models import Cart

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=64, blank=True)
    email = models.EmailField('Email', max_length=64, blank=True)
    name = models.CharField('Имя', max_length=64, blank=True)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    gender = models.CharField('Пол', max_length=32, blank=True)

    def get_dont_checkout_cart(self):
        try:
            cart = self.cart_set.get(is_checkout=False)
        except ObjectDoesNotExist:
            cart = Cart.objects.create(customer=self)
        return cart

    def __str__(self):
        return f'Покупатель {self.name}'