from django.urls import path
from . import views

app_name = 'mondai1_2'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),

]

