from django.urls import path

from . import views

app_name = 'apple'  # 标识app的唯一标识
urlpatterns = [
    # name用来反查URL, 如果一个URL很长且复杂, 这个name用于后端渲染页面, 如果是前后端分离开发, 可以不要
    path('apple_django/', views.apple_django, name='apple_django'),  # # 基于Django的函数请求
    path('apple_drf/', views.apple_drf, name='apple_drf'),  # # 基于drf的函数请求
    path('apple_class/', views.AppleViews.as_view(), name='apple_class'),  # # 基于drf的class请求
]
