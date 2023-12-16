from rest_framework import serializers
from .models import MedicalCostsDataset


class MedicalCostsDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCostsDataset
        fields = '__all__'


class TrainSerializer(serializers.Serializer):
    seed = serializers.IntegerField()


class PredictSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    sex = serializers.CharField(max_length=10)
    bmi = serializers.FloatField()
    children = serializers.IntegerField()
    smoker = serializers.CharField(max_length=5)
    region = serializers.CharField(max_length=20)
