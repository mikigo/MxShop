from rest_framework import serializers
from apps.goods.models import Goods, GoodsCategory


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         """Create and return a new Goods"""
#         return Goods.objects.create(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # 外键的所有信息展示出来

    class Meta:
        model = Goods
        fields = "__all__"  # 取出所有的字段
        # fields = (
        #     'category',
        #     'goods_sn',
        #     'name',
        #     'click_num',
        #     'sold_num',
        #     'fav_num',
        #     'goods_num',
        #     'market_price',
        #     'shop_price',
        #     'goods_brief',
        #     'goods_desc',
        #     'ship_free',
        #     'goods_front_image',
        #     'is_new',
        #     'is_hot',
        #     'add_time',
        # )
