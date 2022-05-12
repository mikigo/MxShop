#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Author:Mikigo
@Date  :2022/5/12 23:33
@Desc  :
"""

# https://django-filter.readthedocs.io/en/main/guide/rest_framework.html
from django_filters import rest_framework as filters
from .models import Goods


class GoodsFilter(filters.FilterSet):
    """对商品进行过滤"""
    price_min = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="shop_price", lookup_expr='lt')
    # name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
