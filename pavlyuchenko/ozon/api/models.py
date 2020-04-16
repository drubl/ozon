from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=64, blank=True)
    email = models.EmailField('Email', max_length=64, blank=True)
    name = models.CharField('Имя', max_length=64, blank=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField('Пол', max_length=32, blank=True)

    def get_dont_checkout_cart(self):
        try:
            cart = self.cart_set.get(is_checkout=False)
        except ObjectDoesNotExist:
            cart = Cart.objects.create(customer=self)
        return cart

    def __str__(self):
        return f'Покупатель {self.name}'

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
#     instance.profile.save()


class Cart(models.Model):
    purchases = models.ManyToManyField(Product, through='Purchase')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_checkout = models.BooleanField('Оформлена', default=False)

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

    def get_total_count_purchases(self):
        return len(self.purchase_set.all())

    def get_total_count_products(self):
        total_count = 0
        for purchase in self.purchase_set.all():
            total_count += purchase.count
        return total_count


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