from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(primary_key=True, max_length=64)
    category = models.CharField(max_length=32, default='Без категории')
    created_at = models.DateTimeField(default=datetime.now)
    body = models.TextField()

    def __str__(self):
        return self.title
