from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
# 引入rest_framework的状态码
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
# 引入搜索模块
from rest_framework import filters
# 引入分页模块
from rest_framework.pagination import PageNumberPagination
# 引入过滤模块 还是django 的filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

# 引入过滤类
from .filters import GoodsFilter
from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer


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
    # 序列化
    serializer_class = GoodsSerializer
    # 定制的分页配置
    pagination_class = GoodsPagination

    # 防止公开页面也要认证token造成麻烦，在接口中验证
    # authentication_classes = (TokenAuthentication,)

    # 对查询集进行过滤操作，
    """
    方法一： 最基本的数据过滤
    
    # 获取django rest_framework 的 查询集 详见此模块的request和response对象
    # 内置函数
    def get_queryset(self):
        # 只储存了sql脚本，不会把数据全部取出
        queryset = Goods.objects.all()
        price_min = self.request.query_params.get('price_min', 0)
        if price_min:
            queryset = queryset.filter(shop_price__gt=int(price_min))
        return queryset
    """
    """
    方法二，使用django_filter
    """
    # 配置django_filter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置要过滤的字段 ,注意加s！！！！！！！
    # 因为有了过滤类 支持模糊以及区间过滤所以废弃
    # filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
    # 配置商品的查询功能
    # 在字段前可以加参数，^开头 =精确搜索 @全文搜索 $
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 设置排序的字段
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewset(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer




