import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from catboost import CatBoostRegressor
import snntorch as snn
from snntorch import surrogate
from snntorch import functional as SF
from snntorch import utils
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import torch.nn.functional as F
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MedicalCostsDataset
from .serializers import MedicalCostsDatasetSerializer, TrainSerializer, PredictSerializer


MODEL_NAME = 'CatboostRegressor_MedicalCostsDataset.pkl'
MODEL_PATH = settings.BASE_DIR / 'api' / 'storage' / MODEL_NAME


class MedicalCostsDatasetList(generics.ListAPIView):
    queryset = MedicalCostsDataset.objects.all()
    serializer_class = MedicalCostsDatasetSerializer


class TrainCatboostRegressor(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TrainSerializer(data=request.data)

        if serializer.is_valid():
            seed = serializer.validated_data['seed']

            dataset = list(MedicalCostsDataset.objects.values_list(
                'age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'
            ))
            x_train = [v[:-1] for v in dataset]
            y_train = [v[-1] for v in dataset]
            
            model = CatBoostRegressor(random_seed=seed, silent=True, allow_writing_files=False)
            model.fit(
                x_train,
                y_train,
                cat_features = [0, 1, 3, 4, 5],
            )
            joblib.dump(model, MODEL_PATH)

            return Response({
                'model': 'CatBoostRegressor',
                'task': 'Regressor',
                'seed': seed,
                'save': MODEL_NAME,
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictCatboostRegressor(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PredictSerializer(data=request.data)
        
        if serializer.is_valid() and os.path.exists(MODEL_PATH):
            x_pred = list(serializer.validated_data.values())
            
            model = joblib.load(MODEL_PATH)
            prediction = model.predict(x_pred)

            return Response({
                'prediction': prediction,
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


