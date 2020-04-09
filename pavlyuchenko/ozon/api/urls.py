"""ozon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from api.views import ProductView
from api.views import ProductDetailView
from api.views import CustomerDetailView
from api.views import CustomerView
from api.views import LoginView
from api.views import CartView
from api.views import PuchaseView


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('products/', ProductView.as_view()),
    path('customer/', CustomerView.as_view()),
    path('puchase/', PuchaseView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('customer/<int:id>/', CustomerDetailView.as_view()),
    path('customer/<int:id>/cart', CartView.as_view()),
]
