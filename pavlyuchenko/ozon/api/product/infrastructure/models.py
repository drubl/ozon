from django.db import models
from api.category.infrastructure.models import Category

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=512)
    price = models.IntegerField()
    first_image = models.CharField(max_length=256)
    second_image = models.CharField(max_length=256)
    weight = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)

    def __str__(self):
        return f'Продукт {self.title}'
