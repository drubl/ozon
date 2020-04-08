from django.db import models


class Product(models.Model):
    title = models.CharField('Название',  max_length=200, unique=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    description = models.TextField('Описание', max_length=1000)
    firstPhoto = models.CharField(max_length=255, blank=True)
    secondPhoto = models.CharField(max_length=255, blank=True)
    weight = models.IntegerField('Вес')

    def __str__(self):
        return self.title
