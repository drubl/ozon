from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# from api.product.infrastructure.models import Product
from api.category.domain.logic import get_category_products, filtering, sorting
from api.category.infrastructure.models import Category
from api.product.presentation.serializers import ProductSerializer
from .serializers import CategorySerializer

class CategoryView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'categories': serializer.data})

class CategoryDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, category_slug):
        search_query = request.GET.get('search')
        filter_dict = request.GET.dict()
        sorted_fields = request.GET.get('sorted')
        try:
            products = get_category_products(category_slug, search_query)
            products = filtering(products, filter_dict)
            products = sorting(products, sorted_fields)
        except ValueError as exc:
            return Response(str(exc))
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})