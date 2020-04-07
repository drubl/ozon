from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=512)
    price = models.IntegerField()
    first_image = models.CharField(max_length=256)
    second_image = models.CharField(max_length=256)
    weight = models.IntegerField()



