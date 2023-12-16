import uuid
from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


CHOICES = {
    'category': {
        0: 'Обзоры',
        1: 'Обсуждения',
        2: 'Выступления',
        3: 'Разработки',
    },
    'status': {
        0: 'Черновик',
        1: 'Опубликован',
    },
}


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    category = models.IntegerField(choices=CHOICES['category'].items(), default=0)
    content = models.TextField(max_length=100000)
    status = models.IntegerField(choices=CHOICES['status'].items(), default=0)

    class Meta:
        ordering = ['-created_at']

    @property
    def created_at_formatted(self):
        return self.created_at.strftime('%H:%M | %d.%m.%Y')

    @property
    def updated_at_formatted(self):
        return self.updated_at.strftime('%H:%M | %d.%m.%Y')

    @property
    def category_name(self):
        return CHOICES['category'][int(self.category)]

    @property
    def status_name(self):
        return CHOICES['status'][int(self.status)]

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug or Post.objects.filter(slug=self.slug).exists():
            self.slug = slugify(self.title)[:200]

            num = 0
            while Post.objects.filter(slug=self.slug).exists():
                num += 1
                self.slug = f"{self.slug[:(199 - len(str(num)))]}-{num}"

        super(Post, self).save(*args, **kwargs)
