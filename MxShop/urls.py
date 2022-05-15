"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
# from apps.goods.views import GoodsListView
from apps.goods.views import GoodsListViewSet, GoodsCategoryListViewSet

import xadmin
# router 和 viewsets 配套使用
router = DefaultRouter()
router.register(r'goods', GoodsListViewSet, basename="goods")
router.register(r'categorys', GoodsCategoryListViewSet, basename="categorys")

good_list = GoodsListViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # url(r'goods/$', GoodsListView.as_view(), name="good-list"),
    # url(r'goods/$', good_list, name="good-list"),
    path('', include(router.urls)),
    url(r'docs/', include_docs_urls(title="慕雪生鲜")),
]
