from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=512)
    price = models.IntegerField()
    first_image = models.CharField(max_length=256)
    second_image = models.CharField(max_length=256)
    weight = models.IntegerField()

    def __str__(self):
        return f'<Продукт {self.title}>'

class Customer(models.Model):
    #login = models.CharField('Логин', max_length=64, unique=True)
    password = models.CharField('Пароль', max_length=128)
    phone = models.CharField('Телефон',max_length=64, unique=True)
    email = models.EmailField('Email',max_length=64, unique=True)
    name = models.CharField('Имя',max_length=64)
    birthday = models.DateField('Пароль')
    gender = models.CharField('Пол', max_length=32)

    def __str__(self):
        return f'<Покупатель {self.name}>'


class Cart(models.Model):
    purchases = models.ManyToManyField(Product, through='Purchase', through_fields=('cart','product'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #корзины many-to-one
    is_checkout = models.BooleanField('Оформлена') #Оформленная ли корзина

    def __str__(self):
        return f'<Корзина {self.customer.name}>'


class Purchase(models.Model):
    # Одна покупка может быть только в одной корзине. Покупка это товар и его количество
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    count = models.IntegerField('Количество')

    def get_price(self):
        return self.product.price * self.count
    
    def get_weight(self):
        return self.product.weight * self.count

    def __str__(self):
        return f'<Покупка {self.product.title} в корзине {self.cart.customer.name} {self.count} штук>'