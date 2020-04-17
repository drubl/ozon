from django.urls import path
from customers.presentation.views import CustomerCreate, CustomerDetailView, RegisterCustomer, LoginCustomer

urlpatterns =[
    path('', CustomerCreate.as_view()),
    path('<int:pk>/', CustomerDetailView.as_view()),
    path('create', RegisterCustomer.as_view()),
    path('login', LoginCustomer.as_view()),
]