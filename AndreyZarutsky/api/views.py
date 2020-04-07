from rest_framework.response import Response
from rest_framework.views import APIView


from products.models import Products
from .serializers import ProductsSerializer


class ProductsView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response({'products': serializer.data})