from django.db import models


class Customer(models.Model):
    genderList = [('M', 'male'), ('F', 'female')]
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=2, choices=genderList)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Клиенты'
