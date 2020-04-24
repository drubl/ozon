from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from products.infrastructure.models import Product
from products.presentation.serializers import ProductsSerializer
from products.domain.products_domain import sorting_and_ordering_handler


class ProductsSet(generics.CreateAPIView):
    serializer_class = ProductsSerializer


class ProductsView(generics.ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

    def list(self,request):
        queryset = self.get_queryset()
        serializer = ProductsSerializer(queryset, many=True)
        if request.GET.dict():
            result = sorting_and_ordering_handler(queries=request.GET.dict())
            serializer = ProductsSerializer(result, many=True)
            return Response({'Product': serializer.data})
        return Response({'Product': serializer.data})


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()