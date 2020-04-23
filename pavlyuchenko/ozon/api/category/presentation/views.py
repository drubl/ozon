from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# from api.product.infrastructure.models import Product
from api.category.domain.logic import get_category_products
from api.product.presentation.serializers import ProductSerializer

# class CategoryView(APIView):
#     permission_classes = [AllowAny]
#     def get(self, request):
#         categories = Category.objects.all()
#         return categories

class CategoryDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, category_slug):
        search_query = request.GET.get('search', '')
        try:
            products = get_category_products(category_slug, search_query)
        except ValueError as exc:
            return Response(str(exc))
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})