from django.urls import path
from . import views

# アプリ名を登録
#   URLconfのURLパターンを逆引きできるように名前を登録する
app_name = 'seisaku'

# アプリのURLパターンを登録
#   urlpatternsのリストに記述する
urlpatterns = [
    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールのIndexViewを実行
    # URLパターン名は 'index'
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'), 
    path('contact/', views.ContactView.as_view(), name='contact'),
]
