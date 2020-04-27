from django.db import models
from api.category.infrastructure.models import Category

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=512)
    price = models.IntegerField(blank=True)
    old_price = models.IntegerField()
    discount = models.IntegerField('Скидка', default=0, blank=True)
    first_image = models.CharField(max_length=256)
    second_image = models.CharField(max_length=256)
    weight = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)

    def save(self, *args, **kwargs):
        self.price = self.old_price - self.discount/100*self.price
        super().save(*args, **kwargs)
        
    def get_price(self):
        return self.price

    def is_discount(self):
        if self.discount:
            return True
        return False

    def __str__(self):
        return f'Продукт {self.title}'
