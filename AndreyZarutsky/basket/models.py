from django.db import models
from customers.models import Customer
from products.models import Product


class Basket(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    totalPrice = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    processed = models.BooleanField(default=False)
    orders = models.ManyToManyField(
        Product,
        through='Order',

    )

    def __str__(self):
        return f'{self.user_id.name} basket'

    class Meta:
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    count = models.IntegerField()

    def get_weight(self):
        return self.product.weight * self.count

    def __str__(self):
        return f'{self.basket.user_id} orders-'

