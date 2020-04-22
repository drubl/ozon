from customers.infrastructure.models import Customer
from basket.infrastructure.models import Basket
from django.contrib.auth.models import User


def register_customer(user: object, customer_id: int = None, serializer: object = None):

    if customer_id:
        Customer.objects.filter(id=customer_id).update(user=user)
        return 'Register'
    else:
        customer, created = Customer.objects.update_or_create(user=user,
                                                          phone=serializer.data.pop('phone'))
        Basket.objects.create(user_id=customer)
        return 'Register'


def check_email(User, serilalizedData):

    """ checks if the user is registered with this email"""

    email = serilalizedData.data['user']['email']
    check = User.objects.filter(email=email)
    if check:
        return True
    return False