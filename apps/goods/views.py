from django.shortcuts import render

# Create your views here.
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# 引入rest_framework的状态码
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from goods.models import Goods


# 定制分页
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    # 指定查询的端口
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    方法一，继承APIView
    返回商品；列表的视图

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        # many 表示序列化的对象为列表对象
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)
    """

    """
    # 这个request是drf的request
    def post(self, request):
        
        # 先验证前端传来的json对象是否合法
        # 然后再进行保存操作
        # 类似于上一个项目的我要学习的form表单
        
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 表示数据保存成功
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 表示数据保存失败(请求失败)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    """
    方法二，继承mixins.ListModelMixin 和 generics.GenericAPIView
    (非常重要的view 是对APIview的封装)
    提供了分页等功能
    
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    """
    """
    方法三继承generics的ListAPIView
    
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # 设置定制分页
    pagination_class = GoodsPagination
    """
    """
    方法四，继承viewsets
    继承mixins.ListModeMixin, viewsets.GenericViewSet
    本项目将使用的方式，配合Router使用
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # 定制的分页配置 啊
    pagination_class = GoodsPagination