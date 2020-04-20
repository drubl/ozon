from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status

from  auth.domain.auth_domain import get_customer_basket_login, update_login_orders


class LoginCustomer(APIView):

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            customer_id, basket_id = get_customer_basket_login(user=user)
            if request.session.get('customer_id'):
                update_login_orders(basket_id=basket_id, customer_id=request.session.get('customer_id'))
                request.COOKIES['user_id'] = customer_id
                return Response({"token": user.auth_token.key, "id": customer_id})
            if not request.session.get('customer'):
                request.session['customer_id'] = customer_id
                request.COOKIES['customer_id'] = customer_id
                return Response({"token": user.auth_token.key, "id": customer_id})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
