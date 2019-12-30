# from django.conf.urls import url, static
from django.urls import path
from .view import views

# URLマッピング
urlpatterns = [
    path('search/', views.search_info),  # 検索結果取得
    path('recommend/', views.reccomend_info),  # おすすめ結果取得
    path('login/', views.user_info),  # ユーザー情報操作
]
