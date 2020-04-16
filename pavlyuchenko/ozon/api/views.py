from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from rest_framework.generics import CreateAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import SessionAuthentication

from api.models import Product
from api.models import Customer
from api.models import Purchase

from api.serializers import ProductSerializer
from api.serializers import CustomerSerializer
from api.serializers import CartSerializer
from api.serializers import PurchaseSerializer
from api.serializers import UserSerializer


def has_anonymous_customer(request):
    anonymous_customer = request.session.get('anon_customer_id')
    if anonymous_customer is not None:
        return True
    return False

def get_anonymous_customer(request):
    anonymous_customer_id = request.session['anon_customer_id']
    anonymous_customer = Customer.objects.get(pk=anonymous_customer_id)
    return anonymous_customer

def create_anonymous_customer(request):
    print('Мы пытались создать кастомера и записать его в сессию')
    anonymous_customer = Customer.objects.create()
    request.session['anon_customer_id'] = anonymous_customer.id
    print(anonymous_customer, request.session['anon_customer_id'])
    return anonymous_customer

def get_or_create_anonymous_customer(request):
    ''' Возвращает покупателя из сессии или создает нового. '''
    if request.session.get('anon_customer_id') is None:
        print("Решили создать кастомера")
        return create_anonymous_customer(request)
    else:
        print('Решили взять из сессии')
        return get_anonymous_customer(request)

def delete_anonymous_customer_session(request):
    try:
        del request.session['anon_customer_id']
    except:
        pass

def get_customer(request):
    ''' Получение покупателя: из сессии, создание нового или получение у авторизированного пользователя. '''
    if request.user.is_anonymous:
        return get_or_create_anonymous_customer(request)
    else:
        return request.user.customer

def add_purchases_from_anonymous_customer(request, user):
    ''' Добавление всех покупок невторизированного пользователя при входе на сайт, т.е совмещение всех его покупок. '''
    auth_customer = user.customer
    auth_customer_cart = auth_customer.get_dont_checkout_cart()
    auth_customer_purchases = auth_customer_cart.purchase_set.all()

    anonymous_customer = get_anonymous_customer(request)
    anonymous_customer_cart = anonymous_customer.get_dont_checkout_cart()
    anonymous_customer_purchases = anonymous_customer_cart.purchase_set.all()

    for auth_customer_purchase in auth_customer_purchases:
        auth_customer_product = auth_customer_purchase.product
        for anonymous_customer_purchase in anonymous_customer_purchases:
            anonymous_customer_product = anonymous_customer_purchase.product
            if auth_customer_product.id == anonymous_customer_product.id:
                auth_customer_purchase.count += anonymous_customer_purchase.count
                auth_customer_purchase.save()
                anonymous_customer_purchase.delete()
                break

    for anonymous_customer_purchase in anonymous_customer_purchases:
        auth_customer_cart.purchase_set.add(anonymous_customer_purchase)
        print("Товара не было в корзине авторизированного пользователя и мы добавлили его из анонимного покупателя")

        
class TESTView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        if has_anonymous_customer(request):
            print(get_customer(request).id)
        return Response({'': has_anonymous_customer(request)})

class ProductView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, id):
        ''' Получение одного продукта. '''
        product = get_object_or_404(Product.objects.all(), pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        ''' Изменение продукта. '''
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


class CustomerDetailView(APIView): #TODO rename
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customer = request.user.customer
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def delete(self, request):
        customer = request.user.customer
        customer.delete()
        return Response({'Customer was deleted': customer.name})

    def put(self, request):
        saved_customer = request.user.customer
        data = request.data
        serializer = CustomerSerializer(instance=saved_customer, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_customer = serializer.save()
        return Response({'Product was edit': saved_customer.name})


class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data

        if request.session.get('anon_customer_id', '') == '': #TODO refactor
            customer_serializer = CustomerSerializer(data=customer_data)
            if customer_serializer.is_valid(raise_exception=True):
                customer = customer_serializer.create(validated_data=customer_data)
        else:
            user_data = data.pop('user')
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid(raise_exception=True):
                user = user_serializer.create(validated_data=user_data)

            customer = get_anonymous_customer(request)
            customer_serializer = CustomerSerializer(instance=customer, data=data, partial=True)
            if customer_serializer.is_valid():
                customer.user = user
                customer = customer_serializer.save()
            delete_anonymous_customer_session(request)

            login(request, user=user)

        return Response({'Customer was created': customer.name})   


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            if has_anonymous_customer(request):
                add_purchases_from_anonymous_customer(request, user)
                login(request, user)
                return Response({"user": user.username})
            else:
                login(request, user)
                return Response({'user': user.username})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        logout(request)
        return Response(str(request.user.is_anonymous))


class PurchaseView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        purchase = Purchase.objects.all()
        serializer = PurchaseSerializer(purchase, many=True)
        return Response({'purchase': serializer.data})

    def post(self, request, product_id):
        ''' Добавление товара в корзину. '''
        customer = get_customer(request)
        cart = customer.get_dont_checkout_cart()
        wont_to_add_product = get_object_or_404(Product.objects.all(), pk=product_id)
        count_add_product = request.GET.get('count', 1)

        for purchase in cart.purchase_set.all():
            if purchase.product == wont_to_add_product:
                purchase.count += int(count_add_product)
                purchase.save()
                return Response({'Purchase': purchase.id}) #TODO 32-36 abstract in new func
        purchase = Purchase.objects.create(product=wont_to_add_product, cart=cart, count=count_add_product)

        return Response({'Purchase': purchase.id})

    def delete(self, request, product_id):
        customer = get_customer(request)
        cart = customer.get_dont_checkout_cart()
        purchase = get_object_or_404(cart.purchase_set.all(), pk=product_id)
        purchase.delete()
        return Response({'Purchase': product_id})

    def put(self, request, product_id):
        new_count = request.GET.get('count', '1')
        if new_count:
            customer = get_customer(request)
            cart = customer.get_dont_checkout_cart()
            purchase = get_object_or_404(cart.purchase_set.all(), pk=product_id)
            purchase.count = new_count
            purchase.save()
            return Response({'Purchase': purchase})
        else:
            return Response({'Need a new count of product': ''})


class CartView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        ''' Получение корзины. '''
        customer = get_customer(request)
        cart = customer.get_dont_checkout_cart()  
        cart.purchase = cart.purchase_set.all()  
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    def post(self, request):
        ''' Оформление корзины. '''
        if request.user.is_anonymous:
            return Response({'Need a register or logout user': ''}, status=status.HTTP_401_UNAUTHORIZED)

        customer = request.user.customer
        cart = customer.get_dont_checkout_cart()
        cart.is_checkout = True
        cart.save()
        return Response({'Cart has been checkout': cart.id})



