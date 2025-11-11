"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # , include追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(('blogapp.urls', 'blogapp'), namespace='blogapp')),
    path('mondai1/', include('mondai1.urls')),
    path('mondai1_2/', include('mondai1_2.urls')),
    path('mondai1_3/', include('mondai1_3.urls')),
    path('mondai2/', include('mondai2.urls')),
    path('seisaku/', include(('seisaku.urls', 'seisaku'), namespace='seisaku')),  # 制作課題 
]
