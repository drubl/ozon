from django.urls import path

from api.views import ProductView
from api.views import ProductDetailView
from api.views import CustomerDetailView
from api.views import RegisterView
from api.views import LoginView
from api.views import LogoutView
from api.views import CartView
from api.views import PurchaseView

from api.views import TESTView


urlpatterns = [
    path('test/', TESTView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('products/', ProductView.as_view()),
    path('register/', RegisterView.as_view()),
    path('purchase/', PurchaseView.as_view()), #not for api
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('customer/', CustomerDetailView.as_view()),
    path('customer/cart/', CartView.as_view()),
    path('customer/cart/<int:product_id>/', PurchaseView.as_view()),
]

# urlpatterns = [
#     path('login/', LoginView.as_view()),
#     path('logout/', LogoutView.as_view()),
#     path('products/', ProductView.as_view()),
#     path('customer/', RegisterView.as_view()),
#     path('purchase/', PurchaseView.as_view()),
#     path('products/<int:id>/', ProductDetailView.as_view()),
#     path('customer/<int:id>/', CustomerDetailView.as_view()),
#     path('customer/<int:id>/cart/', CartView.as_view()),
#     path('customer/<int:customer_id>/cart/<int:product_id>/', PurchaseView.as_view()),
# ]
