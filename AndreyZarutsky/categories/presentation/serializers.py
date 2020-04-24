from rest_framework import serializers
from categories.infrastructure.models import Category
from products.presentation.serializers import ProductsSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OneCategorySerializer(serializers.ModelSerializer):
    products = ProductsSerializer(source='get_all_product', many=True)
    class Meta:
        model = Category
        fields = ('name', 'products')
        verbose_name = 'Содержимое категории'