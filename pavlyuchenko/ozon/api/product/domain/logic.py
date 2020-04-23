from django.db.models import Q

from api.product.infrastructure.models import Product

def get_all_or_search_products(search_query):
    if search_query:
        return Product.objects.all().filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    else:
        return Product.objects.all()

def get_product_data(product_id):
    try:
        return Product.objects.get(pk=product_id)
    except:
        raise ValueError(f'Продукт с id {product_id} не найден')