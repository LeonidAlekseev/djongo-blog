from django.urls import path
from . import views


urlpatterns = [
    path('catboost/', views.CatBoost.as_view(), name='catboost'),
    path('snntorch/', views.SNNTorch.as_view(), name='snntorch'),
]
