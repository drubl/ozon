from rest_framework import serializers
from products.infrastructure.models import Product

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'price', 'description','firstPhoto','secondPhoto', 'weight')