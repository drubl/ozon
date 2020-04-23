from django.urls import path

from .views import CategoryDetailView


urlpatterns = [
    path('category/<slug:category_slug>/', CategoryDetailView.as_view()),
]