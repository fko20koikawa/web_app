from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

# クラスベースビュー
class IndexView(TemplateView):
    template_name = 'blogapp/index.html'
