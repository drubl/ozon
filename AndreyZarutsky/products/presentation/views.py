from rest_framework import generics
from rest_framework.response import Response


from products.infrastructure.models import Product
from products.presentation.serializers import ProductsSerializer


class ProductsSet(generics.CreateAPIView):
    serializer_class = ProductsSerializer


class ProductsView(generics.ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    def list(self,request):
        queryset = self.get_queryset()
        serializer = ProductsSerializer(queryset, many=True)
        return Response({'Product': serializer.data})


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()