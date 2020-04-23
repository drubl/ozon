from django.urls import path
from auth.presentation.views import LoginCustomer, LogoutCustomer

urlpatterns =[
    path('', LoginCustomer.as_view()),
    path('out', LogoutCustomer.as_view())
]