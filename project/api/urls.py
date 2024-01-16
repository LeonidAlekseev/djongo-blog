from django.urls import path
from . import views


urlpatterns = [
    path('regression/catboost/train/', views.TrainCatboostRegressor.as_view(), name='train'),
    path('regression/catboost/predict/', views.PredictCatboostRegressor.as_view(), name='predict'),
    path('regression/catboost/dataset/', views.MedicalCostsDatasetList.as_view(), name='dataset'),
]
