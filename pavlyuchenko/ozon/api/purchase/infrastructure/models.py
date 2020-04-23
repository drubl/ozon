from django.db import models

class Purchase(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    count = models.IntegerField('Количество')

    def get_price(self):
        return self.product.get_price() * self.count
    
    def get_weight(self):
        return self.product.weight * self.count

    def __str__(self):
        return f'Покупка "{self.product.title}" в корзине "{self.cart.customer.name}", "{self.count}" штук'