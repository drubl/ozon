from django.urls import path
from .views import LoginCustomer

urlpatterns =[
    path('', LoginCustomer.as_view())
]