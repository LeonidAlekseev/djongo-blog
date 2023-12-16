from django.views import generic
from django.db import models
from .models import Post


class PostList(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        search_post = self.request.GET.get('search')

        if search_post:
            queryset = Post.objects.filter(
                models.Q(title__icontains=search_post) | \
                models.Q(category__icontains=search_post) | \
                models.Q(content__icontains=search_post),
                status=1
            ).order_by('-created_at')
        else:
            queryset = Post.objects.filter(status=1).order_by('-created_at')

        return queryset

models.Q
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post.html'
    paginate_by = 6
