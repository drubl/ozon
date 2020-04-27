from django.urls import path, re_path

from products.presentation.views import ProductDetailView, ProductsSet, ProductsView

urlpatterns = [
        # re_path(r'\?(order_by)', ProductsViewFiltering.as_view()),
        path('', ProductsView.as_view()),
        path('<int:pk>/', ProductDetailView.as_view()),
        path('create', ProductsSet.as_view()),
]