from django.urls import path
from . import views


urlpatterns = [
    path('catboost/', views.CatBoost.as_view(), name='catboost'),
]
