from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import PurchaseSerializer
from api.product.infrastructure.models import Product
from api.purchase.infrastructure.models import Purchase
from api.purchase.domain.logic import get_anonymous_customer
from api.purchase.domain.logic import create_anonymous_customer
from api.purchase.domain.logic import delete_purchase_from_cart
from api.purchase.domain.logic import add_product_to_cart
from api.purchase.domain.logic import change_count_product_in_purchase

class PurchaseView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, product_id):
        ''' Добавление товара в корзину. '''
        count = request.GET.get('count', 1)
        customer = self.get_customer(request)
        print(customer)
        try:
            add_product_to_cart(customer, product_id, count)
        except Exception as exc:
            print(exc)
            return Response(str(exc))
        return Response('OK')

    def delete(self, request, product_id):
        ''' Удаление покупки из корзины. '''
        customer = self.get_customer(request)
        try:
            delete_purchase_from_cart(customer, product_id)
        except Exception as exc:
            return Response(str(exc))
        return Response('OK')

    def put(self, request, product_id):
        ''' Изменение количества товара в покупке. '''
        new_count = request.GET.get('count', '1')
        customer = self.get_customer(request)
        try:
            change_count_product_in_purchase(customer, new_count)
        except Exception as exc:
            return Response(str(exc))
        return Response('OK')

    def get_customer(self, request):
        if request.user.is_anonymous:
            anonymous_customer_id = request.session.get('anon_customer_id')
            if anonymous_customer_id:
                return get_anonymous_customer(anonymous_customer_id)
            else:
                customer = create_anonymous_customer()
                request.session['session'] = customer.id
                return customer
        return request.user.customer