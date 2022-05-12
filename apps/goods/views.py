from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from .models import Goods


class StandardResultsSetPagination(PageNumberPagination):
    # 定制分页
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100

# GenericViewSet是最高的一层，它继承了GenericAPIView，GenericAPIView又继承了APIView，APIView继承了View
# mixin
# CreateModelMixin  创建
# ListModelMixin 获取一个列表
# RetrieveModelMixin 获取某一个
# UpdateModelMixin 更新
# DestroyModelMixin 删除
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """商品列表页"""
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'shop_price'] # 过滤器

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         queryset =  queryset.filter(shop_price__gt=int(price_min))
    #     return queryset

# generics.ListAPIView 继承了 mixins.ListModelMixin, generics.GenericAPIView
# class GoodsListView(generics.ListAPIView):
#     """商品列表页"""
#
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = StandardResultsSetPagination
#     # 分页在 settings 里面配置


# GenericAPIView 继承了 APIView ，更加上层
# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """商品列表页"""
#
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# 需要继承 mixins.CreateModelMixin
# def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)

# class GoodsListView(APIView):
#     """商品列表页"""
#
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         serializer = GoodsSerializer(goods, many=True)
#         return Response(serializer.data)

# def post(self, request, format=None):
#     serializer = GoodsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()  # 调用 create 方法
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
