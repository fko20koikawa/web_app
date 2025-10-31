from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class TopView(TemplateView):
    template_name = "mondai1/top.html"
    