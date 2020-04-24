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
    if filter_dict.get('price'):
        products = products.filter(price=filter_dict.get('price'))
    elif filter_dict.get('weight'):
        pass
    elif filter_dict.get('is_discount'):
        pass

    return products

def sorting(products, sorted_fields):
    if sorted_fields:
        sorted_fields = sorted_fields.split(',')
        return products.order_by(*sorted_fields)
    return products
