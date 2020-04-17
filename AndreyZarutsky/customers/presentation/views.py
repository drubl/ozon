from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from api.api_tools import check_email
from customers.presentation.serializer import CustomersSerializer, UserSerializer

from customers.infrastructure.models import Customer
from basket.infrastructure.models import Basket, Order
from django.contrib.auth.models import User

from customers.domain.customer_domain import register_customer, get_customer_basket_login, update_login_orders


class LoginCustomer(APIView):

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            customer_id, basket_id = get_customer_basket_login(user=user)
            if request.session.get('customer_id'):
                update_login_orders(basket_id=basket_id, customer_id=request.session.get('customer_id'))
                request.COOKIES['user_id'] = customer.id
                return Response({"token": user.auth_token.key, "id": customer.id})
            if not request.session.get('customer'):
                request.session['customer_id'] = customer.id
                request.COOKIES['customer_id'] = customer.id
                return Response({"token": user.auth_token.key, "id": customer.id})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterCustomer(APIView):

    def post(self, request):
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            if check_email(User, serializer):
                return Response('Пользователь с таким email уже зарегистрирован',
                                status=status.HTTP_400_BAD_REQUEST)
            user_data = serializer.data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            result = register_customer(user, customer_id=request.session.get('customer_id'))
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class CustomerCreate(generics.CreateAPIView):
    serializer_class = CustomersSerializer


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomersSerializer
    queryset = Customer.objects.all()
    def get(self,request,pk):
        queryset = self.get_queryset()
        serializer = CustomersSerializer(queryset.get(pk=pk))
        return Response({'Customer': serializer.data})