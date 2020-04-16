from django.urls import path

from api.views import ProductView
from api.views import ProductDetailView
from api.views import CustomerDetailView
from api.views import CustomerView
from api.views import LoginView
from api.views import CartView
from api.views import PurchaseView


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('products/', ProductView.as_view()),
    path('customer/', CustomerView.as_view()),
    path('purchase/', PurchaseView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('customer/<int:id>/', CustomerDetailView.as_view()),
    path('customer/<int:id>/cart/', CartView.as_view()),
    path('customer/<int:customer_id>/cart/<int:product_id>/', PurchaseView.as_view()),
]
