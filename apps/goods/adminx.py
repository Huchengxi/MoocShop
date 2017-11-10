__auth__ = 'Christ'
__date__ = '2017/11/10 22:01'
__version__ = '1.0'

"""
xadmin 的配置
"""
import xadmin
from .models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner, HotSearchWords
from .models import IndexAd


class GoodsAdmin:
    list_display = ['name', 'click_num', 'sold_num', 'fav_num', 'goods_num', 'ma']