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