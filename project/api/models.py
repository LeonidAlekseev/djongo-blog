import pandas as pd
from django.conf import settings
from django.db import models
from django.dispatch import receiver


DATA_PATH = settings.BASE_DIR / 'api' / 'storage' / 'medical_costs_dataset.csv'


class MedicalCostsDataset(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    bmi = models.FloatField()
    children = models.IntegerField()
    smoker = models.CharField(max_length=5)
    region = models.CharField(max_length=20)
    charges = models.FloatField()


data = pd.read_csv(DATA_PATH).values
medical_costs_data = [
    MedicalCostsDataset(
        age=row[0], 
        sex=row[1], 
        bmi=row[2], 
        children=row[3], 
        smoker=row[4], 
        region=row[5], 
        charges=row[6], 
    ) for row in data
]
MedicalCostsDataset.objects.bulk_create(medical_costs_data)
