from rest_framework import serializers

from api.product.presentation.serializers import ProductSerializer

from api.purchase.infrastructure.models import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    price = serializers.IntegerField(read_only=True, source='get_price')
    weight = serializers.IntegerField(read_only=True, source='get_weight')
    class Meta:
        model = Purchase
        fields = ['id', 'product', 'count', 'price', 'weight']