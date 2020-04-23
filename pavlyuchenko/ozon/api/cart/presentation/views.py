from django.db.models import Q

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.product.infrastructure.models import Product
from api.cart.domain.logic import get_cart_object, checkout_cart, get_anonymous_customer, create_anonymous_customer

from .serializers import CartSerializer

class CartView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        ''' Получение корзины. '''
        if request.user.is_anonymous:
            if anonymous_customer_id := request.session.get('anon_customer_id'):
                customer = get_anonymous_customer(anonymous_customer_id)
            else:
                customer = create_anonymous_customer()
                request.session['session'] = customer.id
        else:
            customer = request.user.customer
        cart = get_cart_object(customer)  
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    def post(self, request):
        ''' Оформление корзины. '''
        if request.user.is_anonymous:
            return Response('Need a register or login user', status=status.HTTP_401_UNAUTHORIZED)
        checkout_cart(request.user.customer)
        return Response('OK')
        