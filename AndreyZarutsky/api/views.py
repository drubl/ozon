from rest_framework.response import Response
from rest_framework.views import APIView
from django.http.response import HttpResponse


from products.models import Product
from .serializers import ProductsSerializer


class ProductsView(APIView):
    def get(self, request):
        search = request.GET.get('search', '')
        if search:
            products = Product.objects.filter(title__icontains=search)
        else:
            products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response({'products': serializer.data})


class ProductsId(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except:
            return HttpResponse(f'<h3>Произошла ошибка. Товар с id "{pk}" не найден.</h3>')
        serializer = ProductsSerializer(product)
        return Response({'product': serializer.data})
