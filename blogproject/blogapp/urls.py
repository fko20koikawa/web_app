from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('' , views.IndexView.as_view(), name='index'),
    path('blog-detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
        # scienceカテゴリの一覧ページのURLパターン
    path(
        # scienceカテゴリの一覧ページのURLは「science-list/」
        'science-list/',
        # viewsモジュールのBlogDetailを実行
        views.ScienceView.as_view(),
        # URLパターンの名前を'science_list'にする
        name='science_list'
        ),
    # dailylifeカテゴリの一覧ページのURLパターン
    path(
        # dailylifeカテゴリの一覧ページのURLは「dailylife-list/」
        'dailylife-list/',
        # viewsモジュールのDailylifeViewを実行
        views.DailylifeView.as_view(),
        # URLパターンの名前を'dailylife_list'にする
        name='dailylife_list'
        ),
    # musicカテゴリの一覧ページのURLパターン
    path(
        # scienceカテゴリの一覧ページのURLは「music-list/」
        'music-list/',
        # viewsモジュールのMusicViewを実行
        views.MusicView.as_view(),
        # URLパターンの名前を'music_list'にする
        name='music_list'
        ),
        
    # 問い合わせページのURLパターン
    path(
        # 問い合わせページのURLは「contact/」
        'contact/',
        # viewsモジュールのContactViewを実行,
        views.ContactView.as_view(),
        # URLパターンの名前を'contact'にする
        name='contact'
    ),
]