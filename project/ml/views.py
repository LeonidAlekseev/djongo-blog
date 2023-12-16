from django.views import generic
from django.shortcuts import render


class CatBoost(generic.View):
    template_name = 'catboost.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
