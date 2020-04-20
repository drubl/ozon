from django.urls import path
from auth.presentation.views import LoginCustomer

urlpatterns =[
    path('', LoginCustomer.as_view())
]