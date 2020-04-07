from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status

from api.models import Product
from api.serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request):
        search_query = request.GET.get('search')
        if search_query is not None:
            products = Product.objects.all().filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})

    def post(self, request):
        pass
        


class ProductDetailView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(pk=id)
        except:
            error = {'error': f'Product with id {id} not found'}
            return Response(error, status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)