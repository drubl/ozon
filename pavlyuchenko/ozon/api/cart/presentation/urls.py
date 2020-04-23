from django.urls import path

from .views import CartView


urlpatterns = [
    path('customer/cart/', CartView.as_view()),
]