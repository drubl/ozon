from rest_framework import serializers
from customers.models import Customer
from products.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
