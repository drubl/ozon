from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=512)
    price = models.IntegerField()
    first_image = models.CharField(max_length=256)
    second_image = models.CharField(max_length=256)
    weight = models.IntegerField()

    def __str__(self):
        return f'Продукт {self.title}'

class Customer(models.Model):
    #login = models.CharField('Логин', max_length=64, unique=True)
    password = models.CharField('Пароль', max_length=128)
    phone = models.CharField('Телефон', max_length=64, unique=True)
    email = models.EmailField('Email', max_length=64, unique=True)
    name = models.CharField('Имя', max_length=64)
    birthday = models.DateField('Пароль')
    gender = models.CharField('Пол', max_length=32)

    def __str__(self):
        return f'Покупатель {self.name}'


class Cart(models.Model):
    purchases = models.ManyToManyField(Product, through='Purchase')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #корзины many-to-one
    is_checkout = models.BooleanField('Оформлена') #Оформленная ли корзина

    def get_total_price(self):
        total_price = 0
        for purchase in self.purchase_set.all():
            total_price += purchase.get_price()
        return total_price

    def get_total_weight(self):
        total_weight = 0
        for purchase in self.purchase_set.all():
            total_weight += purchase.get_weight()
        return total_weight

    def get_total_count(self):
        return len(self.purchase_set.all())

    def __str__(self):
        return f'Корзина {self.customer.name}'


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    count = models.IntegerField('Количество')

    def get_price(self):
        return self.product.price * self.count
    
    def get_weight(self):
        return self.product.weight * self.count

    def __str__(self):
        return f'Покупка "{self.product.title}" в корзине "{self.cart.customer.name}", "{self.count}" штук'