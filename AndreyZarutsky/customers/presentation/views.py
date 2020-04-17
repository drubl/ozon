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



class LoginCustomer(APIView):
    permission_classes = ()

    def post(self, request,):
        print(request.data.items())
        username = request.data.get("username")
        password = request.data.get("password")
        print(username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            customer = User.objects.select_related('customer').get(username=user).customer
            basket = customer.basket_set.all()[0]
            if not request.session.get('basket_id'):
                request.session['basket_id'] = basket.id
                request.session['customer_id'] = customer.id
                request.COOKIES['user_id'] = customer.id
                print('COOKIE', request.COOKIES['user_id'])
                return Response({"token": user.auth_token.key, "id": customer.id})
            if request.session.get('basket_id'):
                Order.objects.filter(basket_id=request.session.get('basket_id')).update(basket_id=basket.id)
                request.COOKIES['user_id'] = customer.id
                print('COOKIE',request.user)
                return Response({"token": user.auth_token.key, "id": customer.id})
            # print('session.items()',request.session.keys())
            # return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterCustomer(APIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self, request):
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            if check_email(User, serializer):
                return Response('Пользователь с таким email уже зарегистрирован',
                                status=status.HTTP_400_BAD_REQUEST)
            user_data = serializer.data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            print(f'USER CREATE {user}')
            if request.session.get('basket_id') and request.session.get('customer_id'):
                Customer.objects.filter(id=request.session['customer_id']).update(user=user)
                customer = Customer.objects.get(id=request.session['customer_id'])
                print(f'CUSTOMER UPDATE')
            else:
                customer, created = Customer.objects.update_or_create(user=user,
                                                                  phone=serializer.data.pop('phone'))
                Basket.objects.create(user_id=customer)
            return Response(f'Register {customer.user.username}', status=status.HTTP_201_CREATED)
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