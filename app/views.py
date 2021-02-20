import random
from collections import OrderedDict

from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from app import serializers, models
# Create your views here.


class PagePagination(LimitOffsetPagination):
    """分页"""
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 200
    default_limit = 100

    def get_paginated_response(self, data):
        ret = dict([
            ('code', 10000),
            ('errMsg', ''),
            ('count', self.count),
            ('previous', self.get_previous_link()),
            ('next', self.get_next_link()),
        ])
        if isinstance(data, dict):
            ret.update(**data)
        else:
            ret.update({
                'results': data
            })
        return Response(OrderedDict(ret))


class DynamicView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """动态图表"""
    queryset = models.Table2.objects.filter().order_by('-id')
    serializer_class = serializers.Table2Serializer
    pagination_class = PagePagination
    # permission_classes = []

    @action(methods=['GET'], detail=False)
    def dynamic_chart_template1(self, request, *args, **kwargs):
        """实时动态图表网页 1"""
        return render(request, 'dynamic_chart1.html', {})

    @action(methods=['GET'], detail=False)
    def dynamic_chart_template2(self, request, *args, **kwargs):
        """100 条图表数据网页 2"""
        return render(request, 'dynamic_chart2.html', {})

    @action(methods=['GET'], detail=False)
    def dynamic_chart_data(self, request, *args, **kwargs):
        """动态数据"""
        data = [random.randint(1, 20) for _ in range(3)]
        # 批量保存数据库
        save_objs = [models.Table1(content=i) for i in data]
        models.Table1.objects.bulk_create(save_objs)

        res = {'code': 10000, 'results': data, 'errMsg': ''}
        return Response(res)

    def create(self, request, *args, **kwargs):
        """保存当前数据到表2"""
        data = request.data.get("data", None)
        res = {'code': 10000, 'errMsg': ''}

        if data:
            save_objs = [models.Table1(content=i) for i in data]
            models.Table2.objects.bulk_create(save_objs)
        else:
            res['code'] = 40000
            res['errMsg'] = '无数据可保存'

        return Response(res)