from django.urls import path
from . import views


urlpatterns = [
    path('regression/catboost/train/', views.TrainCatboostRegressor.as_view(), name='catboost_train'),
    path('regression/catboost/predict/', views.PredictCatboostRegressor.as_view(), name='catboost_predict'),
    path('regression/catboost/dataset/', views.MedicalCostsDatasetList.as_view(), name='catboost_dataset'),
    path('regression/snntorch/train/', views.TrainSNNTorchRegressor.as_view(), name='snntorch_train'),
    path('regression/snntorch/predict/', views.PredictSNNTorchRegressor.as_view(), name='snntorch_predict'),
    path('regression/snntorch/dataset/', views.LinearDatasetList.as_view(), name='snntorch_dataset'),
]
