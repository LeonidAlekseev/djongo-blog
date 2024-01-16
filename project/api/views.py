import os
import io
import base64
import joblib
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from catboost import CatBoostRegressor
import torch
from torch.utils.data import DataLoader
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MedicalCostsDataset
from .serializers import MedicalCostsDatasetSerializer, TrainSerializer, PredictSerializer
from .serializers import TrainSNNTorchSerializer, PredictSNNTorchSerializer
from .snn_utils import RegressionDataset, SNNTorchRegressorNet


STORAGE_DIR = settings.BASE_DIR / 'api' / 'storage'
MODEL_NAME = 'CatboostRegressor_MedicalCostsDataset.pkl'
MODEL_PATH = STORAGE_DIR / MODEL_NAME
SNNTORCH_DATASET = None
DEVICE = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
SNNTORCH_MODEL_NAME = 'SNNTorchRegressor_LinearDataset.pt'
SNNTORCH_MODEL_PATH = STORAGE_DIR / SNNTORCH_MODEL_NAME


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
                'task': 'Regression',
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


class LinearDatasetList(APIView):
    def get(self, request, *args, **kwargs):
        if SNNTORCH_DATASET is not None:
            fig = plt.figure(figsize=(16, 8))
            plt.plot(SNNTORCH_DATASET.labels[:, 0, 0], label="Истина")
            plt.title("Целевая функция")
            plt.xlabel("Временной шаг")
            plt.ylabel("Мембранный потенциал")
            plt.legend(loc='best')
            plt.grid()
            target_function_jpg_bytes = io.BytesIO()
            plt.savefig(target_function_jpg_bytes, format='jpg')
            target_function_jpg_bytes.seek(0)
            target_function_jpg_bytes = base64.b64encode(target_function_jpg_bytes.read()).decode()
            return Response({
                'features': SNNTORCH_DATASET.features.squeeze(-1).squeeze(-1),
                'labels': SNNTORCH_DATASET.labels.squeeze(-1).squeeze(-1),
                'target_function_jpg_bytes': target_function_jpg_bytes,
            })
        else:
            return Response({
                'message': 'The dataset has not yet been generated.',
            })


class TrainSNNTorchRegressor(APIView):
    def post(self, request, *args, **kwargs):
        global SNNTORCH_DATASET
        serializer = TrainSNNTorchSerializer(data=request.data)

        if serializer.is_valid():
            seed = serializer.validated_data['seed']
            torch.manual_seed(seed)
            random.seed(seed)
            np.random.seed(seed)

            timesteps = serializer.validated_data['timesteps']
            dataset = RegressionDataset(timesteps=timesteps, num_samples=1)
            dataloader = torch.utils.data.DataLoader(dataset=dataset, batch_size=1, drop_last=True)
            SNNTORCH_DATASET = dataset

            hidden_layer = serializer.validated_data['hidden_layer']
            model = SNNTorchRegressorNet(hidden=hidden_layer).to(DEVICE)
            
            train_batch = iter(dataloader)
            with torch.no_grad():
                for feature, label in train_batch:
                    feature = torch.swapaxes(input=feature, axis0=0, axis1=1)
                    label = torch.swapaxes(input=label, axis0=0, axis1=1)
                    feature = feature.to(DEVICE)
                    label = label.to(DEVICE)
                    mem = model(feature)
            fig = plt.figure(figsize=(16, 8))
            plt.plot(mem[:, 0, 0].cpu(), label="Предсказание")
            plt.plot(label[:, 0, 0].cpu(), '--', label="Истина")
            plt.title("Необученная модель")
            plt.xlabel("Временной шаг")
            plt.ylabel("Мембранный потенциал")
            plt.legend(loc='best')
            plt.grid()
            untrained_model_jpg_bytes = io.BytesIO()
            plt.savefig(untrained_model_jpg_bytes, format='jpg')
            untrained_model_jpg_bytes.seek(0)
            untrained_model_jpg_bytes = base64.b64encode(untrained_model_jpg_bytes.read()).decode()
            
            max_iteraions = serializer.validated_data['max_iteraions']
            learning_rate = serializer.validated_data['learning_rate']
            optimizer = torch.optim.Adam(params=model.parameters(), lr=learning_rate)
            loss_function = torch.nn.MSELoss()
            model.train()
            for _ in range(max_iteraions):
                train_batch = iter(dataloader)
                minibatch_counter = 0
                loss_epoch = []
                
                for feature, label in train_batch:
                    feature = torch.swapaxes(input=feature, axis0=0, axis1=1)
                    label = torch.swapaxes(input=label, axis0=0, axis1=1)
                    feature = feature.to(DEVICE)
                    label = label.to(DEVICE)

                    mem = model(feature)
                    loss_val = loss_function(mem, label)
                    optimizer.zero_grad()
                    loss_val.backward()
                    optimizer.step()

            model.eval()
            label = label.cpu().detach().numpy()
            mem = mem.cpu().detach().numpy()
            fig = plt.figure(figsize=(16, 8))
            plt.plot(mem[:, 0, :], label="Предсказание")
            plt.plot(label[:, 0, :], label="Истина")
            plt.title("Обученная модель")
            plt.xlabel("Временной шаг")
            plt.ylabel("Мембранный потенциал")
            plt.legend(loc='best')
            plt.grid()
            trained_model_jpg_bytes = io.BytesIO()
            plt.savefig(trained_model_jpg_bytes, format='jpg')
            trained_model_jpg_bytes.seek(0)
            trained_model_jpg_bytes = base64.b64encode(trained_model_jpg_bytes.read()).decode()

            torch.save(model, SNNTORCH_MODEL_PATH)

            return Response({
                'model': 'SNNTorchRegressor',
                'task': 'Regression',
                'seed': seed,
                'timesteps': timesteps,
                'hidden_layer': hidden_layer,
                'max_iteraions': max_iteraions,
                'learning_rate': learning_rate,
                'save': SNNTORCH_MODEL_NAME,
                'untrained_model_jpg_bytes': untrained_model_jpg_bytes,
                'trained_model_jpg_bytes': trained_model_jpg_bytes,
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictSNNTorchRegressor(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PredictSNNTorchSerializer(data=request.data)
        
        if serializer.is_valid() and os.path.exists(MODEL_PATH):
            feature = serializer.validated_data['features']
            feature = torch.tensor(feature).unsqueeze(-1).unsqueeze(-1)
            
            model = torch.load(SNNTORCH_MODEL_PATH).to(DEVICE)
            model.eval()
            prediction = model(feature)
            prediction = prediction.squeeze(-1).squeeze(-1).cpu().detach().numpy()
            fig = plt.figure(figsize=(16, 8))
            plt.plot(prediction, label="Предсказание")
            plt.title("Предсказание модели")
            plt.xlabel("Временной шаг")
            plt.ylabel("Мембранный потенциал")
            plt.legend(loc='best')
            plt.grid()
            model_prediction_jpg_bytes = io.BytesIO()
            plt.savefig(model_prediction_jpg_bytes, format='jpg')
            model_prediction_jpg_bytes.seek(0)
            model_prediction_jpg_bytes = base64.b64encode(model_prediction_jpg_bytes.read()).decode()

            return Response({
                'prediction': prediction,
                'model_prediction_jpg_bytes': model_prediction_jpg_bytes,
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
