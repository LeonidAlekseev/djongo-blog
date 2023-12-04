from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=32, default='Без категории')
    created_at = models.DateTimeField(default=datetime.now)
    body = models.TextField()

    @property
    def created_at_formatted(self):
        return self.created_at.strftime('%H:%M | %d.%m.%Y')

    def __str__(self):
        return self.title
