from django.urls import path
from basket.presentation.views import BasketShow, AddRemUpdOrder, Processed

urlpatterns =[
    path('cart/', BasketShow.as_view()),
    path('cart/<int:product_id>', AddRemUpdOrder.as_view()),
    path('cart/checkout', Processed.as_view())
]