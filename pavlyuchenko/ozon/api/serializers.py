from rest_framework import serializers

from api.models import Product

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=512)
    price = serializers.IntegerField()
    firstPhoto = serializers.CharField(max_length=256, source='first_image')
    secondPhoto = serializers.CharField(max_length=256, source='second_image')
    weight = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

