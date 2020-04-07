from django.urls import path
from .views import ProductsView,ProductsId


urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('products/<int:pk>', ProductsId.as_view())
]