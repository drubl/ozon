from django.urls import path

from .views import LoginView
from .views import LogoutView
from .views import RegisterView
from .views import CheckEmailView


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('checkemail/', CheckEmailView.as_view()),
]