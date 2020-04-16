from rest_framework import serializers
from customers.models import Customer
from products.models import Product
from basket.models import Basket, Order
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        print(validated_data['password'])
        # password = User.set_password(validated_data['password'])
        email = validated_data['email']
        user = User(username=username, email=email)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class CustomersSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ('user', 'phone')


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title', 'price', 'description','firstPhoto','secondPhoto', 'weight')



class OrderSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()
    weight = serializers.IntegerField(source='get_weight')
    class Meta:
        model = Order
        fields = ('product', 'count', 'weight')

class BasketSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField()
    order = OrderSerializer(many=True, read_only=True)
    totalCount = serializers.IntegerField(source='get_total_count')
    totalWeight = serializers.IntegerField(source='get_total_weight')
    totalPrice = serializers.DecimalField(max_digits=10, decimal_places=2,source='get_total_price')
    class Meta:
        model = Basket
        fields = ('user_id', 'order', 'totalCount','totalWeight', 'totalPrice')