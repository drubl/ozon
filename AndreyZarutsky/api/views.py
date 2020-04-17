from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BasketSerializer
from api.api_tools import check_busket, create_customer_basket


from products.infrastructure.models import Product
from customers.infrastructure.models import Customer
from basket.infrastructure.models import Basket, Order


# class TESTPermission(APIView):
#     # permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         # request.session['order'] = []
#         # request.session['order'].append(('homa', 2))
#         print(dict(request.session))
#         # print(request.session.session_key)
#         # print(request.session['order'])
#         # print(bool(request.session.get('basket_id')))
#         print(request.user.is_anonymous)
#         print(request.user.id)
#         print(request.user)
#         print(request.user.auth_token)
#         print(request.auth)
#         return Response('Вы авторизированный пользователь.')
#
#
# class create_customer_test(APIView):
#     authentication_classes = ()
#     permission_classes = ()
#     def post(self, request):
#         serializer = CustomersSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             user_data = serializer.data.pop('user')
#             print(User.objects.set_.user_data["password"])
#
#         return Response(serializer.error_messages,
#                         status=status.HTTP_400_BAD_REQUEST)


# class LoginCustomer(APIView):
#     permission_classes = ()
#
#     def post(self, request,):
#         print(request.data.items())
#         username = request.data.get("username")
#         password = request.data.get("password")
#         print(username,password)
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user:
#             customer = User.objects.select_related('customer').get(username=user).customer
#             basket = customer.basket_set.all()[0]
#             if not request.session.get('basket_id'):
#                 request.session['basket_id'] = basket.id
#                 request.session['customer_id'] = customer.id
#                 request.COOKIES['user_id'] = customer.id
#                 print('COOKIE', request.COOKIES['user_id'])
#                 return Response({"token": user.auth_token.key, "id": customer.id})
#             if request.session.get('basket_id'):
#                 Order.objects.filter(basket_id=request.session.get('basket_id')).update(basket_id=basket.id)
#                 request.COOKIES['user_id'] = customer.id
#                 print('COOKIE',request.user)
#                 return Response({"token": user.auth_token.key, "id": customer.id})
#             # print('session.items()',request.session.keys())
#             # return Response({"token": user.auth_token.key})
#         else:
#             return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)



# class RegisterCusomer(APIView):
#     authentication_classes = ()
#     permission_classes = ()
#     def post(self, request):
#         serializer = CustomersSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             if check_email(User, serializer):
#                 return Response('Пользователь с таким email уже зарегистрирован',
#                                 status=status.HTTP_400_BAD_REQUEST)
#             user_data = serializer.data.pop('user')
#             user = UserSerializer.create(UserSerializer(), validated_data=user_data)
#             print(f'USER CREATE {user}')
#             if request.session.get('basket_id') and request.session.get('customer_id'):
#                 Customer.objects.filter(id=request.session['customer_id']).update(user=user)
#                 customer = Customer.objects.get(id=request.session['customer_id'])
#                 print(f'CUSTOMER UPDATE')
#             else:
#                 customer, created = Customer.objects.update_or_create(user=user,
#                                                                   phone=serializer.data.pop('phone'))
#                 Basket.objects.create(user_id=customer)
#             return Response(f'Register {customer.user.username}', status=status.HTTP_201_CREATED)
#         return Response(serializer.error_messages,
#                         status=status.HTTP_400_BAD_REQUEST)


class Processed(APIView):
    def post(self,request, user_id):
        basket = check_busket(user_id)
        if basket.order_set.count() == 0 :
            return Response('Ошибка! Ваша корзина пуста!')
        basket.processed = True
        basket.save()
        return Response('Заказ оформлен!')



class AddRemUpdOrder(generics.UpdateAPIView, APIView):

    def post(self, request, user_id, product_id):
        if request.user.is_anonymous:
            print('попался анонимус')
            if not request.session.get('basket_id'):
                customer, basket = create_customer_basket(Customer, Basket)
                request.session['basket_id'] = basket.id
                request.session['customer_id'] = customer.id
                Order.objects.create(product=Product.objects.get(id=product_id), basket=basket, count=1)
                print(request.session['basket_id'])
                print(f'Customer = {customer}, basket = {basket}')
                return Response(f'"{Product.objects.get(pk=product_id).title}" добавлен в вашу корзину')
            else:
                basket = Basket.objects.get(pk=request.session.get('basket_id'))
                order = basket.order_set.all()
                target_product = order.filter(product_id=product_id)
                if not target_product:
                    Order.objects.create(product=Product.objects.get(id=product_id), basket=basket, count=1)
                    return Response(f'"{Product.objects.get(pk=product_id).title}" добавлен в вашу корзину')
        basket = check_busket(Customer, Basket, user_id)
        order = basket.order_set.all()
        target_product = order.filter(product_id=product_id)
        if not target_product:
            Order.objects.create(product=Product.objects.get(id=product_id),basket=basket,count=1)
            return Response(f'"{Product.objects.get(pk=product_id).title}" добавлен в вашу корзину')

    def update(self, request, user_id, product_id):
        if request.user.is_anonymous:
            print('попался анонимус')
            if request.session.get('basket_id'):
                print(request.session.items())
                print(request.session['basket_id'])
                print(request.session['customer_id'])
                basket = Basket.objects.get(pk=request.session.get('basket_id'))
                order = basket.order_set.all()
                target_product = order.filter(product_id=product_id)
                if target_product:
                    target_product[0].count += 1
                    target_product[0].save()
                    return Response('added')
            return Response()
        basket = check_busket(Customer, Basket, user_id)
        order = basket.order_set.all()
        target_product = order.filter(product_id=product_id)
        if target_product:
            target_product[0].count += 1
            target_product[0].save()
            return Response('added')


    def delete(self,request, user_id, product_id):
        if request.user.is_anonymous:
            print('попался анонимус')
            if request.session.get('basket_id'):
                print(request.session.items())
                print(request.session['basket_id'])
                print(request.session['customer_id'])
                basket = Basket.objects.get(pk=request.session.get('basket_id'))
                basket.order_set.filter(product_id=product_id).delete()
                return Response('delete')
        basket = check_busket(Customer, Basket, user_id)
        basket.order_set.filter(product_id=product_id).delete()
        return Response('delete')


def item_in_order_del(request, user_id, product_id):
    basket = Customer.objects.get(pk=1).basket_set.get()
    basket.order_set.filter(product_id=product_id).delete()
    return HttpResponse()


class BasketShow(APIView):

    def get(self, request, user_id):
        print(request.user.is_anonymous)
        if request.user.is_anonymous:
            print('попался анонимус')
            if request.session.get('basket_id'):
                basket = Basket.objects.get(pk=request.session.get('basket_id'))
                basket.order = basket.order_set.all()
                serializer = BasketSerializer(basket)
                return Response({f'корзина ': serializer.data})
        customer = Customer.objects.get(pk=user_id)
        basket = customer.basket_set.first()
        if basket.processed :
            return Response('Корзина пуста')
        basket.order = basket.order_set.all()
        serializer = BasketSerializer(basket)
        return Response({f'корзина {customer}': serializer.data})



# class ProductsSet(generics.CreateAPIView):
#     serializer_class = ProductsSerializer
#
#
# class ProductsView(generics.ListAPIView):
#     serializer_class = ProductsSerializer
#     queryset = Product.objects.all()
#     def list(self,request):
#         queryset = self.get_queryset()
#         serializer = ProductsSerializer(queryset, many=True)
#         return Response({'Product': serializer.data})
#
#
# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductsSerializer
#     queryset = Product.objects.all()


# class CustomerCreate(generics.CreateAPIView):
#     serializer_class = CustomersSerializer
#
#
# class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CustomersSerializer
#     queryset = Customer.objects.all()
#     def get(self,request,pk):
#         queryset = self.get_queryset()
#         serializer = CustomersSerializer(queryset.get(pk=pk))
#         return Response({'Customer': serializer.data})