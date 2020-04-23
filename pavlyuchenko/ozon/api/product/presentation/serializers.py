from rest_framework import serializers
from api.product.infrastructure.models import Product

class ProductSerializer(serializers.ModelSerializer):
    firstPhoto = serializers.CharField(max_length=256, source='first_image')
    secondPhoto = serializers.CharField(max_length=256, source='second_image')
    category = serializers.CharField(source='category.title')
    is_discount = serializers.BooleanField()
    old_price = serializers.IntegerField(source='price')
    price = serializers.IntegerField(source='get_price')

    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'is_discount', 'description', 'old_price', 'price', 'firstPhoto', 'secondPhoto', 'weight']

    def create(self, validated_data): #TODO delete
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):#TODO delete
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.first_image = validated_data.get('firstPhoto', instance.first_image)
        instance.second_image = validated_data.get('secondPhoto', instance.second_image)
        instance.weight = validated_data.get('weight', instance.weight)

        instance.save()
        return instance