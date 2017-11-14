__auth__ = 'Christ'
__date__ = '2017/11/13 17:50'
__version__ = '1.0'

# 过滤配置 引入模块
import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    # 设置要过滤字段的类型以及行为
    # name为字段， lookup_expr为要执行的操作
    # 等于 Goods.objects.filter(shop_price__gt=min_price)
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    # 模糊查询相当于sql 的 like 和 ilike
    # 按商品名模糊查询有另一个模块在view中实现，所以此配置废弃
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    # 配置自定义的顶部类过滤
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))

    class Meta:
        # 设置需要过滤的字段
        model = Goods
        fields = ['price_min', 'price_max']
