from django.urls import path

from .views import PurchaseView


urlpatterns = [
    path('customer/cart/<int:product_id>/', PurchaseView.as_view()),
]