from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.user.domain.logic import add_purchases_from_anonymous_customer, get_anonymous_customer
from api.customer.presentation.serializers import CustomerSerializer
from .serializers import UserSerializer



class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        user_data = data.pop('user')
        anonymous_customer_id = request.session.get('anon_customer_id')
        try:
            user = self.create_user(user_data)
            self.create_customer(anonymous_customer_id, data, user)
        except Exception as exc:
            return Response(str(exc))
        login(request, user=user)
        return Response('OK')

    def create_user(self, user_data):
        user_serializer = UserSerializer(data=user_data)
        try:
            if user_serializer.is_valid(raise_exception=True):
                return user_serializer.create(validated_data=user_data)
        except:
            raise Exception(user_serializer.errors)
    
    def create_customer(self, anonymous_customer_id, data, user):
        if anonymous_customer_id:
            self.create_customer_from_session(data, user)
        else:
            self.create_new_customer(data, user)

    def create_new_customer(self, data, user):
        customer_serializer = CustomerSerializer(data=data)
        try:
            if customer_serializer.is_valid(raise_exception=True):
                return customer_serializer.create(validated_data=data, user=user)
        except:
            raise Exception(user_serializer.errors)

    def create_customer_from_session(self, data, user):
        customer = get_anonymous_customer(anonymous_customer_id)
        customer_serializer = CustomerSerializer(instance=customer, data=data, partial=True)
        if customer_serializer.is_valid(raise_exception=True):
            customer.user = user
            customer = customer_serializer.save()
            del request.session['anon_customer_id']


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username, password = request.data.get('username'), request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            anonymous_customer_id = request.session.get('anon_customer_id')
            if anonymous_customer_id:
                add_purchases_from_anonymous_customer(anonymous_customer_id, user)
            login(request, user)
            response = Response('OK')
            response.set_cookie('is_login', 'True', 43200)
            return response
        else:
            return Response('Bad login or password', status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        logout(request)
        response = Response('OK')
        response.set_cookie('is_login', 'False', 43200)
        return response

class CheckEmailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        email = request.GET.get('email')
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            return Response('false')
        return Response('true')