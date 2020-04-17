from django.db import models
from django.db.models import Sum
from customers.infrastructure.models import Customer
from products.infrastructure.models import Product


class Basket(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    totalPrice = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    totalWeight = models.IntegerField(default=0)
    totalCount = models.IntegerField(default=0)
    processed = models.BooleanField(default=False)
    orders = models.ManyToManyField(
        Product,
        through='Order',
    )

    def get_total_price(self):
        total = self.orders.all().aggregate(Sum('price'))
        print(total['price__sum'])
        return total['price__sum']

    def get_total_weight(self):
        total = self.orders.all().aggregate(Sum('weight'))
        print(total['weight__sum'])
        return total['weight__sum']

    def get_total_count(self):
        total = self.order_set.aggregate(Sum('count'))
        print(total['count__sum'])
        return total['count__sum']

    def __str__(self):
        if self.user_id:
            return f'{self.user_id} basket'
        else:
            return 'anonymous basket'

    class Meta:
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    count = models.IntegerField()

    def get_weight(self):
        return self.product.weight * self.count

    def __str__(self):
        if self.basket.user_id:
            return f'{self.basket.user_id} orders-'
        else:
            return "anonymous order"

