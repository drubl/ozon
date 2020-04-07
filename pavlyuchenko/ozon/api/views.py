from django.shortcuts import render
from django.db.models import Q
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status

from api.models import Product
from api.serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            products = Product.objects.all().filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})

    def post(self, request):
        product = request.POST
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            saved_product = serializer.save()
        return Response({'Product created': saved_product.title}) 


class ProductDetailView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(pk=id)
        except:
            error = {'error': f'Product with id {id} not found'}
            return Response(error, status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        saved_product = get_object_or_404(Product.objects.all(), pk=id) ## TODO Выбрать один стиль вызова 404 ошибки
        data = request.data
        serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            saved_product = serializer.save()

        return Response({'Product was changed': saved_product.title})

    def delete(self, request, id):
        product = get_object_or_404(Product.objects.all(), pk=id)
        product.delete()

        return Response({'Product was delted': product.title})

class CustomerView(APIView):
    pass

