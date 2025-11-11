from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class TopView(TemplateView):
    template_name = "mondai1_2/top.html"
