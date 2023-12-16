# Generated by Django 4.0.1 on 2023-12-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalCostsDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('bmi', models.FloatField()),
                ('children', models.IntegerField()),
                ('smoker', models.CharField(max_length=5)),
                ('region', models.CharField(max_length=20)),
                ('charges', models.FloatField()),
            ],
        ),
    ]
