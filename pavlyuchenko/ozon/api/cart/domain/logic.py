from api.customer.infrastructure.models import Customer

def get_anonymous_customer(anonymous_customer_id):
    ''' Получение покупателя из сессии. '''
    anonymous_customer = Customer.objects.get(pk=anonymous_customer_id)
    return anonymous_customer

def create_anonymous_customer():
    ''' Создание анонимного покупателя и запись его в сессию. '''
    anonymous_customer = Customer.objects.create()
    return anonymous_customer

def checkout_cart(customer):
    cart = customer.get_dont_checkout_cart()
    cart.is_checkout = True
    cart.save()

def get_cart_object(customer):
    cart = customer.get_dont_checkout_cart()  
    cart.purchase = cart.purchase_set.all()
    return cart