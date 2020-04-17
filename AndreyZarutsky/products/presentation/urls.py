from django.urls import path

from products.presentation.views import ProductDetailView, ProductsSet, ProductsView

urlpatterns = [
        path('', ProductsView.as_view()),
        path('<int:pk>/', ProductDetailView.as_view()),
        path('create', ProductsSet.as_view()),
]