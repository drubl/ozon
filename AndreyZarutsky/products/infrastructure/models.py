import decimal
from django.db import models
from categories.infrastructure.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField('Название',  max_length=200, unique=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    description = models.TextField('Описание', max_length=1000)
    firstPhoto = models.CharField(max_length=255, blank=True)
    secondPhoto = models.CharField(max_length=255, blank=True)
    weight = models.IntegerField('Вес')
    discount = models.SmallIntegerField('Скидка в процентах', default=0)
    final_price = models.DecimalField('Финальная цена', max_digits=10, decimal_places=2 , default=0)

    def save(self, *args, **kwargs):
        if self.discount > 0:
            self.final_price = self.price * decimal.Decimal(((100 - self.discount)/100))
        else:
            self.final_price = self.price
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
