from django.urls import path

from .views import BlogListView, MLPageView, RNNPageView, SNNPageView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('ml/', MLPageView.as_view(), name='ml'),
    path('rnn/', RNNPageView.as_view(), name='rnn'),
    path('snn/', SNNPageView.as_view(), name='snn')
]
