from django.urls import path
from django.views.generic import TemplateView

app_name = 'mondai2'

urlpatterns = [
    path('', TemplateView.as_view(template_name="mondai2/index.html"), name="index"),
    path('about/', TemplateView.as_view(template_name="mondai2/about.html"), name="about"),
    path('category/', TemplateView.as_view(template_name="mondai2/category.html"), name="category"),
    path('contact/', TemplateView.as_view(template_name="mondai2/contact.html"), name="contact"),
    path('post/', TemplateView.as_view(template_name="mondai2/post.html"), name="post"), 
    path('single-post/', TemplateView.as_view(template_name="mondai2/single-post.html"), name="single-post"), 
    path('starter-page/', TemplateView.as_view(template_name="mondai2/starter-page.html"), name="starter-page"),
    path('blog-details/', TemplateView.as_view(template_name="mondai2/blog-details.html"), name="blog-details"),
]
