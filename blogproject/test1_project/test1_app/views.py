from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from .forms import Test1AppForm

class Test1AppView(FormView):
    template_name = "test1.html"
    form_class = Test1AppForm
