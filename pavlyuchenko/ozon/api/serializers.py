from rest_framework import serializers

from api.models import Product
from api.models import Customer
from api.models import Cart
from api.models import Purchase


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=512)
    price = serializers.IntegerField()
    firstPhoto = serializers.CharField(max_length=256, source='first_image')
    secondPhoto = serializers.CharField(max_length=256, source='second_image')
    weight = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.first_image = validated_data.get('firstPhoto', instance.first_image)
        instance.second_image = validated_data.get('secondPhoto', instance.second_image)
        instance.weight = validated_data.get('weight', instance.weight)

        instance.save()
        return instance

class CustomerSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'password', 'email', 'birthday', 'gender']

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.gender = validated_data.get('gender', instance.gender)

        instance.save()
        return instance


class PurchaseSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    price = serializers.IntegerField(read_only=True, source='get_price')
    class Meta:
        model = Purchase
        fields = ['id', 'product', 'count', 'price']


class CartSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(many=True, read_only=True)
    total_price = serializers.IntegerField(source='get_total_price')
    total_weight = serializers.IntegerField(source='get_total_weight')
    count_purchase = serializers.IntegerField(source='get_total_count')
    class Meta:
        model = Cart
        fields = ['id', 'is_checkout', 'purchase', 'total_price', 'total_weight', 'count_purchase'] 
