__author__ = 'Christ'
__date__ = '2017/11/12 0012 上午 3:42'

from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    """
    继承serializers.Serializer
    方法一，直接定义每一个字段，和model的form功能类似
    form是直接处理html对象的
    而serializer则是处理json数据的
    可以通过他增删改查，保存操作
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    """

    """
    给前端提供保存的方法，相当于重写object
    def create(self, validated_data):
        
        给前端提供一个添加商品的接口，
        类似于models.form的表单可以直接保存数据
        (上一个项目的我要学习)
        :param validated_data:
        :return:
        
        return Goods.objects.create(**validated_data)
    """
    """
    方法二，直接继承ModelSerializer
    相当于上一个项目直接继承modelform
    可以自动识别字段不用自己再添加
    (直接通过model映射)
    """
    # 自定义字段覆盖原有的字段
    # 展示外键的信息，而不是id
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"



