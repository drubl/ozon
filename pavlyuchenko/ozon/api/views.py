from django.shortcuts import render
from django.db.models import Q

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status

from api.models import Product
from api.models import Customer
from api.models import Purchase

from api.serializers import ProductSerializer
from api.serializers import CustomerSerializer
from api.serializers import CartSerializer
from api.serializers import PurchaseSerializer


class ProductView(APIView):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            products = Product.objects.all().filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})

    def post(self, request):
        product = request.data
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            saved_product = serializer.save()
        return Response({'Product created': saved_product.title}) 


class ProductDetailView(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product.objects.all(), pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        saved_product = get_object_or_404(Product.objects.all(), pk=id)
        data = request.data
        serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_product = serializer.save()
        return Response({'Product was edit': saved_product.title})

    def delete(self, request, id):
        product = get_object_or_404(Product.objects.all(), pk=id)
        product.delete()
        return Response({'Product was deleted': product.title})


class CustomerDetailView(APIView):
    def get(self, request, id):
        customer = get_object_or_404(Customer.objects.all(), pk=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def delete(self, request, id):
        customer = get_object_or_404(Customer.objects.all(), pk=id)
        customer.delete()
        return Response({'Customer was deleted': customer.name})

    def put(self, request, id):
        saved_customer = get_object_or_404(Customer.objects.all(), pk=id)
        data = request.data
        serializer = CustomerSerializer(instance=saved_customer, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_customer = serializer.save()
        return Response({'Product was edit': saved_customer.name})


class CustomerView(APIView):
    def post(self, request):
        customer = request.data
        serializer = CustomerSerializer(data=customer)
        if serializer.is_valid(raise_exception=True):
            customer = serializer.save()
        return Response({'Customer was created': customer.name})


class LoginView(APIView):
    def post(self, request):
        data_email = request.POST.get('email', '')
        data_password = request.POST.get('password', '')
        if data_email and data_password:
            customer = get_object_or_404(Customer.objects.all(),email=data_email)
            if customer.password == data_password:
                return Response({'id': customer.id})
            return Response({'Not right password': ''})
        return Response({'Does not exist email or password': ''})


class LogoutView(APIView):
    pass


class PurchaseView(APIView):
    def get(self, request):
        purchase = Purchase.objects.all()
        serializer = PurchaseSerializer(purchase, many=True)
        return Response({'purchase': serializer.data})

    def post(self, request, customer_id, product_id):
        customer = get_object_or_404(Customer.objects.all(), pk=customer_id)
        cart = customer.get_dont_checkout_cart()
        wont_to_add_product = get_object_or_404(Product.objects.all(), pk=product_id)
        count_add_product = request.POST.get('count', 1)

        for purchase in cart.purchase_set.all():
            if purchase.product == wont_to_add_product:
                purchase.count += int(count_add_product)
                purchase.save()
                return Response({'Purchase': purchase.id}) #TODO 32-36 abstract in new func
        purchase = Purchase.objects.create(product=wont_to_add_product, cart=cart, count=count_add_product)
        return Response({'Purchase': purchase.id})

    def delete(self, request, customer_id, product_id):
        customer = get_object_or_404(Customer.objects.all(), pk=customer_id)
        cart = customer.get_dont_checkout_cart()
        purchase = get_object_or_404(cart.purchase_set.all(), pk=product_id)
        return Response({'Purchase': product_id})

    def put(self, request, customer_id, product_id):
        new_count = request.GET.get('count', '')
        if new_count:
            customer = get_object_or_404(Customer.objects.all(), pk=customer_id)
            cart = customer.get_dont_checkout_cart()
            purchase = get_object_or_404(cart.purchase_set.all(), pk=product_id)
            purchase.count = new_count
            purchase.save()
            return Response({'Purchase': purchase})
        else:
            return Response({'Need a new count of product': ''})


class CartView(APIView):
    def get(self, request, id):
        customer = get_object_or_404(Customer.objects.all(), pk=id)
        cart = customer.get_dont_checkout_cart()  
        cart.purchase = cart.purchase_set.all()  
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    def post(self, request, id):
        customer = get_object_or_404(Customer.objects.all(), pk=id)
        cart = customer.get_dont_checkout_cart()
        cart.is_checkout = True
        cart.save()
        return Response({'Cart has been checkout': cart.id})



