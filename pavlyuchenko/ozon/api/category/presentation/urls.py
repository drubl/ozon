from django.urls import path

from .views import CategoryView
from .views import CategoryDetailView


urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('category/<slug:category_slug>/', CategoryDetailView.as_view()),
]