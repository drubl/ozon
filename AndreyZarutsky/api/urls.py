from django.urls import path
from .views import ProductsView,ProductsSet, ProductDetailView, CustomerCreate, CustomerDetailView, \
    BasketShow, AddRemUpdOrder, Processed, RegisterCusomer, \
    create_customer_test, LoginCustomer, TESTPermission


urlpatterns = [
    # path('products/', ProductsView.as_view()),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    # path('products/create', ProductsSet.as_view()),
    # path('customer/', CustomerCreate.as_view()),
    # path('customer/<int:pk>/', CustomerDetailView.as_view()),
    # path('customer/<int:user_id>/cart/', BasketShow.as_view()),
    # path('customer/<int:user_id>/cart/<int:product_id>', AddRemUpdOrder.as_view()),
    # path('customer/<int:user_id>/cart/checkout', Processed.as_view()),
    # path('customer/create', RegisterCusomer.as_view()),
    # path('login', LoginCustomer.as_view()),
    path('testing/email_valid', create_customer_test.as_view()),
    path('testing/permission', TESTPermission.as_view())
]
