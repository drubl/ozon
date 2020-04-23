from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from rest_framework import status

from .serializers import CustomerSerializer


class CustomerView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customer = request.user.customer
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def delete(self, request):
        user = request.user
        user.delete() #Запрос идет на удаление покупателя, но удаляется пользователь
        return Response('OK')

    def put(self, request):
        saved_customer = request.user.customer
        data = request.data
        serializer = CustomerSerializer(instance=saved_customer, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_customer = serializer.save()
        return Response('OK')