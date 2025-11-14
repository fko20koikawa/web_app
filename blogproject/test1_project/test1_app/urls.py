from django.urls import path
from . import views

app_name = 'test1_app'

urlpatterns = [
    path('', views.Test1AppView.as_view(), name="test1_app"),
]