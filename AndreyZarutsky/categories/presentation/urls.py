from django.urls import path
from categories.presentation.views import OneCategoryAndAllProductIn, Category

urlpatterns = [
    path('', Category.as_view()),
    path('<str:category_name>', OneCategoryAndAllProductIn.as_view())
]