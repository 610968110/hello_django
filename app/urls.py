from django.conf.urls import url
from django.urls import path
from app import views

urlpatterns = [
    path('index', views.index),
    path('index0', views.index0),
    url(r'^view/?$', views.index1),
    url(r'^view\d*$', views.index2),
    url(r'^book/?$', views.show_book),
    url(r'^book/(\d+)$', views.show_hero),  # 会利用正则的分组自动传递参数
]
