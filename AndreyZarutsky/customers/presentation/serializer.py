from rest_framework import serializers
from customers.infrastructure.models import Customer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        print(validated_data['password'])
        # password = User.set_password(validated_data['password'])
        email = validated_data['email']
        user = User(username=username, email=email)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class CustomersSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ('user', 'phone')