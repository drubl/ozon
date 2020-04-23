from django.core.exceptions import ObjectDoesNotExist
from api.customer.infrastructure.models import Customer
from api.product.infrastructure.models import Product
from api.purchase.infrastructure.models import Purchase

def get_anonymous_customer(anonymous_customer_id):
    ''' Получение покупателя по id. '''
    anonymous_customer = Customer.objects.get(pk=anonymous_customer_id)
    return anonymous_customer

def create_anonymous_customer():
    ''' Создание покупателя. '''
    anonymous_customer = Customer.objects.create()
    return anonymous_customer

def get_purchase(cart, purchase_id):
    try:
        return cart.purchase_set.get(pk=purchase_id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist(f'Purchase {purchase_id} does not exist')

def get_product(product_id):
    try:
        return Product.objects.get(pk=product_id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist(f'Product {product_id} does not exist')

def delete_purchase_from_cart(customer, purchase_id):
    cart = customer.get_dont_checkout_cart()
    purchase = get_purchase(cart, purchase_id)
    purchase.delete()

def change_count_product_in_purchase(customer, new_count):
    if new_count:
        cart = customer.get_dont_checkout_cart()
        purchase = get_purchase(cart, purchase_id)
        purchase.count = int(new_count)
        purchase.save()
    else:
        raise ValueError('Count does not exist or not integer')

def add_product_to_cart(customer, product_id, count):
    cart = customer.get_dont_checkout_cart()
    wont_to_add_product = get_product(product_id)
    for purchase in cart.purchase_set.all():
        if purchase.product == wont_to_add_product:
            purchase.count += int(count)
            purchase.save()
            return None    
    purchase = Purchase.objects.create(product=wont_to_add_product, cart=cart, count=count)
