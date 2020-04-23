from rest_framework import serializers

from api.purchase.presentation.serializers import PurchaseSerializer
from api.cart.infrastructure.models import Cart

class CartSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(many=True, read_only=True)
    totalPrice = serializers.IntegerField(source='get_total_price')
    totalWeight = serializers.IntegerField(source='get_total_weight')
    countPurchases = serializers.IntegerField(source='get_total_count_purchases')
    countProducts = serializers.IntegerField(source='get_total_count_products')

    class Meta:
        model = Cart
        fields = ['id', 'is_checkout', 'purchase', 'totalPrice', 'totalWeight', 'countPurchases', 'countProducts'] 