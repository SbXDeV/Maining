from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class Indexing(TemplateView):
    template_name = 'index/index.html'
