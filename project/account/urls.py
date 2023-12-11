
from django.urls import path
from .views import UserRegisterView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = "register"),
]



