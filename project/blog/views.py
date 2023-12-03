from django.views.generic import ListView, TemplateView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class RNNPageView(TemplateView):
    template_name = 'rnn.html'


class SNNPageView(TemplateView):
    template_name = 'snn.html'
