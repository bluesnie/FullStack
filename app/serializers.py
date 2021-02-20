# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2021/2/20 13:25'
__doc__ = ''

from rest_framework import serializers

from app import models


class Table2Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Table2
        fields = '__all__'
