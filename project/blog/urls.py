from django.urls import path

from .views import BlogListView, RNNPageView, SNNPageView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('rnn/', RNNPageView.as_view(), name='rnn'),
    path('snn/', SNNPageView.as_view(), name='snn')
]
