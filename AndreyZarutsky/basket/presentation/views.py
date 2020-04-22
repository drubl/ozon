from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from basket.serializers import BasketSerializer
from basket.domain.basket_layer import create_customer_basket_order, get_basket, get_customer,\
    add_product_to_basket, show_basket, processed_basket, increase_quantity, delete_product_in_basket


from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]


class BasketShow(APIView):

    def get(self, request):
        basket, customer_name = show_basket(
            anonymous=request.user.is_anonymous,
            customer_id=request.session.get('customer_id')
        )
        if not basket:
            return Response(f'Корзина пуста!')
        serializer = BasketSerializer(basket)
        return Response({f'корзина {customer_name}': serializer.data})


class Processed(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        mess, status = processed_basket(customer_id=request.session.get('customer_id'))
        return Response(mess, status=status)


class AddRemUpdOrder(generics.UpdateAPIView, APIView):

    def post(self, request, product_id):
        resp = add_product_to_basket(product_id,
                                     anonymous=request.user.is_anonymous,
                                     customer_id=request.session.get('customer_id'),
                                    )
        request.session['customer_id'] = resp['customer_id']
        return Response(resp['response'])

    def update(self, request, product_id):
        result = increase_quantity(
            product_id,
            anonymous=request.user.is_anonymous,
            customer_id=request.session.get('customer_id')
        )
        return Response(result)

    def delete(self,request, product_id):
        result = delete_product_in_basket(
            product_id,
            anonymous=request.user.is_anonymous,
            customer_id=request.session.get('customer_id')
        )
        return Response(result)