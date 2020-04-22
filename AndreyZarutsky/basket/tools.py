from django.core.exceptions import ObjectDoesNotExist


def create_customer_basket(customer, basket):

    """ Create anonymous customer and basket for him """

    customer = customer()
    customer.save()
    basket = basket(user_id=customer)
    basket.save()
    return (customer, basket)


def check_busket(customer, basket, user_id):
    try:
        basket = customer.objects.get(pk=user_id).basket_set.get()
        if not basket.processed:
            return basket
    except ObjectDoesNotExist:
        print('CREATE NEW BASKET')
        basket = basket.objects.create(user_id=customer.objects.get(pk=user_id))
        return basket

    basket = basket.objects.create(user_id=user_id)
    return basket