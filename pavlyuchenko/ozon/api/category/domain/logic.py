from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# from api.product.infrastructure.models import Product
from api.category.infrastructure.models import Category

def get_category_products(category_slug, search_query):
    try:
        category = Category.objects.get(slug=category_slug)
    except ObjectDoesNotExist:
        raise ValueError('Category does not exist')

    if search_query:
        return category.products.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    return category.products.all()

def filtering(products, filter_dict):
    price = filter_dict.get('price')
    weight = filter_dict.get('weight')
    is_discount = filter_dict.get('is_discount')
    products = price_filter(products, price)
    products = weight_filter(products, weight)
    if is_discount == 't':
        products = products.filter(discount__gt=0)

    return products

def price_filter(products, price):
    if price:
        price = price.split('-')
        print(price)
        if price[0]:
            products = products.filter(final_price__gte=price[0])
        try:
            products = products.filter(final_price__lte=price[1])
        except IndexError:
            pass
    return products

def weight_filter(products, weight):
    if weight:
        weight = weight.split('-')
        if weight[0]:
            products = products.filter(weight__gte=weight[0])
        try:
            products = products.filter(weight__lte=weight[1])
        except IndexError:
            pass
    return products

def sorting(products, sorted_fields):
    if sorted_fields:
        sorted_fields = sorted_fields.split(',')
        return products.order_by(*sorted_fields)
    return products