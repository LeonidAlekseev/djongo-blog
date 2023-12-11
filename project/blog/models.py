# import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


CHOICES = dict(
    category = (
        (0, 'Обзоры'),
        (1, 'Обсуждения'),
        (2, 'Выступления'),
        (3, 'Разработки'),
    ),
    status = (
        (0, 'Черновик'),
        (1, 'Опубликован'),
    )
)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.IntegerField(choices=CHOICES['category'], default=0)
    content = models.TextField()
    status = models.IntegerField(choices=CHOICES['status'], default=0)

    class Meta:
        ordering = ['-created_at']

    @property
    def created_at_formatted(self):
        return self.created_at.strftime('%H:%M | %d.%m.%Y')

    @property
    def updated_at_formatted(self):
        return self.updated_at.strftime('%H:%M | %d.%m.%Y')

    def __str__(self):
        return self.title
