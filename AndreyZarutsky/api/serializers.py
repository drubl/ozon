from rest_framework import serializers
from customers.models import Customer
from products.models import Product
from basket.models import Basket, Order


class BasketSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField()
    class Meta:
        model = Basket
        fields = ('totalPrice', 'ordered')

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title', 'price', 'description', 'weight')


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()
    weight = serializers.IntegerField(source='get_weight')
    class Meta:
        model = Order
        fields = '__all__'