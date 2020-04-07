from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from django.views import View

from api.models import Product
from api.serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request):
        if request.
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})

