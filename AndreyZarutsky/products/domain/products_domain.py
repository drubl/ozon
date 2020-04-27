from products.infrastructure.models import Product


def sorting_and_ordering_handler(queries: dict):
    prepared_data = Product.objects.all()
    for prop,param in queries.items():
        if prop == 'order':
            prepared_data = odered_handler(param, prepared_data)
        if prop == 'price':
            prepared_data = filter_price(param, prepared_data)
    return prepared_data


def filter_price(param: str, queryset: object):
    param_list = param.split('-')
    low = float(param_list[0]) if param_list[0] else queryset.order_by('price').first().price
    high = float(param_list[1]) if param_list[1] else queryset.order_by('price').last().price
    return queryset.filter(price__gte=low).filter(price__lte=high)


def odered_handler(param, queryset):
    return queryset.order_by(f'{param}')
