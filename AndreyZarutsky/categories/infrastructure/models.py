from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=127)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def get_all_product(self):
        return self.product_set.all()


    def __str__(self):
        return self.name
