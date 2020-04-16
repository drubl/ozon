from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Product
from api.models import Customer
from api.models import Cart
from api.models import Purchase

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProductSerializer(serializers.ModelSerializer):
    firstPhoto = serializers.CharField(max_length=256, source='first_image')
    secondPhoto = serializers.CharField(max_length=256, source='second_image')

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'firstPhoto', 'secondPhoto', 'weight']

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
    birthday = serializers.DateField()
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'email', 'birthday', 'gender', 'user']

    def create(self, validated_data):
        user = UserSerializer.create(UserSerializer, validated_data=validated_data.pop('user'))
        customer = Customer.objects.create(user=user, **validated_data)
        return customer

    def update(self, instance, validated_data, user):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.gender = validated_data.get('gender', instance.gender)

        instance.user = validated_data.get('')

        instance.save()
        return instance


class PurchaseSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    price = serializers.IntegerField(read_only=True, source='get_price')
    weight = serializers.IntegerField(read_only=True, source='get_weight')
    class Meta:
        model = Purchase
        fields = ['id', 'product', 'count', 'price', 'weight']


class CartSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(many=True, read_only=True)
    totalPrice = serializers.IntegerField(source='get_total_price')
    totalWeight = serializers.IntegerField(source='get_total_weight')
    countPurchases = serializers.IntegerField(source='get_total_count_purchases')
    countProducts = serializers.IntegerField(source='get_total_count_products')

    class Meta:
        model = Cart
        fields = ['id', 'is_checkout', 'purchase', 'totalPrice', 'totalWeight', 'countPurchases', 'countProducts'] 
