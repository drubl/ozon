from rest_framework.response import Response
from rest_framework.views import APIView
from categories.presentation.serializers import OneCategorySerializer, CategorySerializer
from categories.domain.categories_domain import get_ser_data, get_all_category


class Category(APIView):
    def get(self,request):
        category = get_all_category()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class OneCategoryAndAllProductIn(APIView):
    def get(self, request, category_name):
        category = get_ser_data(category_name)
        serializer = OneCategorySerializer(category)
        return Response(serializer.data)