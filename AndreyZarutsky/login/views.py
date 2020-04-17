from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status

from django.contrib.auth.models import User
from basket.infrastructure.models import Order
from customers.infrastructure.models import Customer



class LoginCustomer(APIView):
    permission_classes = ()

    def post(self, request):
        print(request.data.items())
        username = request.data.get("username")
        password = request.data.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            customer = User.objects.select_related('customer').get(username=user).customer
            basket = customer.basket_set.all()[0]
            if not request.session.get('customer_id'):
                request.session['customer_id'] = customer.id
                print(request.session['basket_id'],request.session['customer_id'])
                return Response({"token": user.auth_token.key, "id": customer.id})
            if request.session.get('customer_id'):
                anonymous_basket = Customer.objects.get(pk=request.session.get('customer_id')).basket_set.get()
                Order.objects.filter(basket_id=anonymous_basket.id).update(basket_id=basket.id)
                request.session['customer_id'] = customer.id
                request.COOKIES['user_id'] = customer.id
                print('COOKIE', request.COOKIES['user_id'])
                return Response({"token": user.auth_token.key, "id": customer.id})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
