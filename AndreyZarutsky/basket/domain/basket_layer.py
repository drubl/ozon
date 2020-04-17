from customers.infrastructure.models import Customer
from basket.infrastructure.models import Basket, Order, Product
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND


def processed_basket(customer_id: int):

    """ Place on order """

    basket = check_busket(customer_id)
    if basket.order_set.count() == 0:
        return 'Ошибка! Ваша корзина пуста!', HTTP_404_NOT_FOUND
    basket.processed = True
    basket.save()
    return 'Заказ оформлен!', HTTP_201_CREATED


def show_basket(anonymous: bool = True, customer_id: int = None):

    """ Show customer basket """

    if anonymous:
        print('попался анонимус')
        if customer_id:
            basket = get_basket(customer_id=customer_id)
            return basket, 'anonymous'
        else:
            return False, False
    customer = get_customer(user_id=customer_id)
    basket = get_basket(customer_id=customer_id)
    if basket.processed:
        return False, False
    return basket, customer.user.username


def add_product_to_basket(product_id: int, anonymous: bool = True, customer_id: int = None):

    """ Add product to basket to POST query"""

    if not anonymous:
        basket = check_busket(customer_id)
        if not check_the_product_in_order(basket.id, product_id):
            Order.objects.create(product=Product.objects.get(id=product_id), basket=basket, count=1)
            return {'customer_id': customer_id,
                    'response': f'"{Product.objects.get(pk=product_id).title}" добавлен в вашу корзину'}

    if not customer_id:
        customer_id, product_name = create_customer_basket_order(product_id)
        return {'customer_id': customer_id,
                'response': f'"{product_name}" добавлен в вашу корзину'}
    else:
        basket = check_busket(customer_id)
        if not check_the_product_in_order(basket.id,product_id):
            Order.objects.create(product=Product.objects.get(id=product_id), basket=basket, count=1)
            return {'customer_id': customer_id,
                    'response': f'"{Product.objects.get(pk=product_id).title}" добавлен в вашу корзину'}


def increase_quantity(product_id: int, anonymous: bool = True, customer_id: int = None):
    if anonymous:
        print('попался анонимус')
        if customer_id:
            basket = get_basket(customer_id)
            order = basket.order_set.all()
            target_product = order.filter(product_id=product_id)
            if target_product:
                target_product[0].count += 1
                target_product[0].save()
                return 'added'
        return 'Error'
    basket = check_busket(customer_id)
    order = basket.order_set.all()
    target_product = order.filter(product_id=product_id)
    if target_product:
        target_product[0].count += 1
        target_product[0].save()
        return 'added'


def delete_product_in_basket(product_id, anonymous: bool = True, customer_id: int = None):
    if anonymous:
        print('попался анонимус')
        if customer_id:
            basket = get_basket(customer_id)
            basket.order_set.filter(product_id=product_id).delete()
            return 'delete'
    basket = check_busket(Customer, Basket, user_id)
    basket.order_set.filter(product_id=product_id).delete()
    return 'delete'


def check_the_product_in_order(basket_id: int, product_id: int):
    basket = Basket.objects.get(pk=basket_id)
    order = basket.order_set.all()
    target_product = order.filter(product_id=product_id)
    return True if target_product else False


def get_customer(user_id):

    """ return Customer by id"""

    customer = Customer.objects.get(pk=user_id)
    return customer


def get_basket(customer_id: int = None):

    """ Retrieve all items from the basket"""

    if customer_id:
        customer = get_customer(customer_id)
        basket = customer.basket_set.get()
        basket.order = basket.order_set.all()
    return basket


def create_customer_basket_order(product_id: int):

    """ Create anonymous customer and basket and oder for him """

    customer = Customer()
    customer.save()
    basket = Basket(user_id=customer)
    basket.save()
    Order.objects.create(product=Product.objects.get(id=product_id), basket=basket, count=1)
    product = Product.objects.get(pk=product_id).title
    return (customer.id, product)


def check_busket(customer_id: int):
    try:
        basket = Customer.objects.get(pk=customer_id).basket_set.get()
        if not basket.processed:
            return basket
    except ObjectDoesNotExist:
        print('CREATE NEW BASKET')
        basket = Basket.objects.create(user_id=Customer.objects.get(pk=customer_id))
        return basket

    basket = Basket.objects.create(user_id=customer_id)
    return basket