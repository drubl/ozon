from api.customer.infrastructure.models import Customer

def get_anonymous_customer(anonymous_customer_id):
    return Customer.objects.get(pk=anonymous_customer_id)

def add_purchases_from_anonymous_customer(anonymous_customer_id, user):
    ''' Добавление всех покупок невторизированного пользователя авторизированному, т.е совмещение всех его покупок. '''
    auth_customer = user.customer
    auth_customer_cart = auth_customer.get_dont_checkout_cart()
    auth_customer_purchases = auth_customer_cart.purchase_set.all()

    anonymous_customer = get_anonymous_customer(anonymous_customer_id)
    anonymous_customer_cart = anonymous_customer.get_dont_checkout_cart()
    anonymous_customer_purchases = anonymous_customer_cart.purchase_set.all()

    for auth_customer_purchase in auth_customer_purchases:
        auth_customer_product = auth_customer_purchase.product
        for anonymous_customer_purchase in anonymous_customer_purchases:
            anonymous_customer_product = anonymous_customer_purchase.product
            if auth_customer_product.id == anonymous_customer_product.id:
                auth_customer_purchase.count += anonymous_customer_purchase.count
                auth_customer_purchase.save()
                anonymous_customer_purchase.delete()
                break

    for anonymous_customer_purchase in anonymous_customer_purchases:
        auth_customer_cart.purchase_set.add(anonymous_customer_purchase)

