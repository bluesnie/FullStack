# _*_ encoding: utf-8 _*_
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app import views

__author__ = 'nzb'
__date__ = '2021/2/20 12:59'
__doc__ = ''

router = DefaultRouter()

router.register('dynamic_chart', views.DynamicView, 'dynamic_chart')     # 动态图表

urlpatterns = [
    path('', include(router.urls)),
]