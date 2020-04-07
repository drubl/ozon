from rest_framework import serializers


class ProductsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=1000)