from django.apps import AppConfig, apps
from django.db.models.signals import post_migrate


class MLConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ml'
