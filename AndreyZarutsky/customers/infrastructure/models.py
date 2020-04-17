from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    genderList = [('M', 'male'), ('F', 'female')]
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=30,blank=True)
    name = models.CharField(max_length=100)
    birthday = models.DateField(auto_now_add=True, blank=True)
    gender = models.CharField(max_length=2, choices=genderList)

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return 'anonymous'

    class Meta:
        verbose_name_plural = 'Клиенты'
