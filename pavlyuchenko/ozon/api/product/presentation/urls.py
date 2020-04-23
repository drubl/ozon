from django.urls import path

from .views import ProductView
from .views import ProductDetailView


urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
]