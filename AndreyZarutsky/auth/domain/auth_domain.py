from customers.infrastructure.models import Customer
from basket.infrastructure.models import Basket, Order
from basket.domain.basket_layer import get_customer
from django.contrib.auth.models import User


def update_login_orders(customer_id: int, basket_id: int):
    customer = get_customer(customer_id)
    # basket = customer.basket_set.get()
    Order.objects.filter(basket_id=basket_id).update(basket_id=basket_id)


def get_customer_basket_login(user: object):
    customer = User.objects.select_related('customer').get(username=user).customer
    basket = customer.basket_set.all()[0]
    return customer.id, basket.id


def register_customer(user: object, customer_id: int = None, serializer: object = None):

    if customer_id:
        Customer.objects.filter(id=customer_id).update(user=user)
        return 'Register'
    else:
        customer, created = Customer.objects.update_or_create(user=user,
                                                          phone=serializer.data.pop('phone'))
        Basket.objects.create(user_id=customer)
        return 'Register'
