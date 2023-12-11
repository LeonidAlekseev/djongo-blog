from django.views.generic import ListView, TemplateView
from django.db import models
from .models import Post


class BlogListView(ListView):
    template_name = 'blog.html'
    paginate_by = 6
    model = Post
