from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=512)
    price = models.IntegerField()
    first_image = models.CharField(max_length=256)
    second_image = models.CharField(max_length=256)
    weight = models.IntegerField()

    def __repr__(self):
        return f'<Product {self.title}>'

class Customer(models.Model):
    #login = models.CharField('Логин', max_length=64, unique=True)
    password = models.CharField('Пароль', max_length=128)
    phone = models.CharField('Телефон',max_length=64, unique=True)
    email = models.EmailField('Email',max_length=64, unique=True)
    name = models.CharField('Имя',max_length=64)
    birthday = models.DateField('Пароль')
    gender = models.CharField('Пол', max_length=32)

    def __repr__(self):
        return f'<Costumer {self.name}>'