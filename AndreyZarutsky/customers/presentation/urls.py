from django.urls import path
from customers.presentation.views import CustomerCreate, CustomerDetailView, RegisterCustomer

urlpatterns =[
    path('', CustomerCreate.as_view()),
    path('<int:pk>/', CustomerDetailView.as_view()),
    path('create', RegisterCustomer.as_view()),
]