from rest_framework import generics


from products.models import Product
from customers.models import Customer
from .serializers import ProductsSerializer, CustomersSerializer


class ProductsSet(generics.CreateAPIView):
    serializer_class = ProductsSerializer


class ProductsView(generics.ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()


class CustomerCreate(generics.CreateAPIView):
    serializer_class = CustomersSerializer


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomersSerializer
    queryset = Customer.objects.all()