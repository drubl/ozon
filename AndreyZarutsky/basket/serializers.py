from rest_framework import serializers
from basket.infrastructure.models import Basket, Order

from products.presentation.serializers import ProductsSerializer


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