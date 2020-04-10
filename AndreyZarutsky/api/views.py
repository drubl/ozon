from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductsSerializer, CustomersSerializer, BasketSerializer, \
    OrderSerializer


from products.models import Product
from customers.models import Customer
from basket.models import Basket, Order


class Processed(APIView):
    def post(self,request, user_id):
        basket = check_busket(user_id)
        if basket.order_set.count() == 0 :
            return Response('Ошибка! Ваша корзина пуста!')
        basket.processed = True
        basket.save()
        return Response('Заказ оформлен!')


def check_busket(user_id):
    try:
        basket = Customer.objects.get(pk=user_id).basket_set.get()
        if not basket.processed:
            return basket
    except ObjectDoesNotExist:
        print('CREATE NEW BASKET')
        basket = Basket.objects.create(user_id=Customer.objects.get(pk=user_id))
        return basket

    basket = Basket.objects.create(user_id=user_id)
    return basket



class AddRemUpdOrder(generics.UpdateAPIView, APIView):

    def post(self,request, user_id, product_id):
        basket = check_busket(user_id)
        order = basket.order_set.all()
        target_product = order.filter(product_id=product_id)
        if not target_product:
            Order.objects.create(product=Product.objects.get(id=product_id),basket=basket,count=1)
            return Response(f'"{Product.objects.get(pk=product_id).title}" добавлен в вашу корзину')

    def update(self, requets, user_id, product_id):
        basket = check_busket(user_id)
        order = basket.order_set.all()
        target_product = order.filter(product_id=product_id)
        if target_product:
            target_product[0].count += 1
            target_product[0].save()
            return Response('added')


    def delete(self,requets, user_id, product_id):
        basket = check_busket(user_id)
        basket.order_set.filter(product_id=product_id).delete()
        return Response('delete')


def item_in_order_del(request, user_id, product_id):
    basket = Customer.objects.get(pk=1).basket_set.get()
    basket.order_set.filter(product_id=product_id).delete()
    return HttpResponse()


class BasketShow(APIView):
    def get(self, request, user_id):
        customer = Customer.objects.get(pk=user_id)
        basket = customer.basket_set.first()
        if basket.processed :
            return Response('Корзина пуста')
        basket.order = basket.order_set.all()
        serializer = OrderSerializer(basket.order, many=True)
        return Response({f'корзина {customer}': serializer.data})



class ProductsSet(generics.CreateAPIView):
    serializer_class = ProductsSerializer


class ProductsView(generics.ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()


class CustomerCreate(generics.CreateAPIView):
    serializer_class = CustomersSerializer


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomersSerializer
    queryset = Customer.objects.all()