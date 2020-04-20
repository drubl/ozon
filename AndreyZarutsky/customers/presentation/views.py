from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status

from customers.presentation.serializer import CustomersSerializer, UserSerializer
from customers.infrastructure.models import Customer
from customers.domain.customer_domain import register_customer


class RegisterCustomer(APIView):

    def post(self, request):
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            if check_email(serializer):
                return Response('Пользователь с таким email уже зарегистрирован',
                                status=status.HTTP_400_BAD_REQUEST)
            user_data = serializer.data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            result = register_customer(
                user,
                customer_id=request.session.get('customer_id'),
                serializer=serializer
            )
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