from django.db.models import Q

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.product.infrastructure.models import Product
from api.product.domain.logic import get_all_or_search_products
from api.product.domain.logic import get_product_data
from .serializers import ProductSerializer


class ProductView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        search_query = request.GET.get('search', '')
        products = get_all_or_search_products(search_query)
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})


class ProductDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, id):
        ''' Получение данных одного продукта. '''
        try:
            product = get_product_data(id)
        except Exception as exc:
            return Response(str(exc))
        serializer = ProductSerializer(product)
        return Response(serializer.data)

