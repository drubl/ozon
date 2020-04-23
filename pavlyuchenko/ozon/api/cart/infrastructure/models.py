from django.db import models
# from api.product.infrastructure.models import Product

class Cart(models.Model):
    purchases = models.ManyToManyField('Product', through='Purchase')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    is_checkout = models.BooleanField('Оформлена', default=False)

    def get_total_price(self):
        total_price = 0
        for purchase in self.purchase_set.all():
            total_price += purchase.get_price()
        return total_price

    def get_total_weight(self):
        total_weight = 0
        for purchase in self.purchase_set.all():
            total_weight += purchase.get_weight()
        return total_weight

    def get_total_count_purchases(self):
        return len(self.purchase_set.all())

    def get_total_count_products(self):
        total_count = 0
        for purchase in self.purchase_set.all():
            total_count += purchase.count
        return total_count


    def __str__(self):
        return f'Корзина {self.customer.name}'