"""MoocShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from extra_app import xadmin
# 设置media的访问路径
from MoocShop.settings import MEDIA_ROOT
from django.views.static import serve

# from goods.views_base import GoodsListView
# 引入framework的文档功能
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewset
# 引入认证view
from rest_framework.authtoken import views
# 引入jwt认证模块
from rest_framework_jwt.views import obtain_jwt_token
# 引入神奇router
from rest_framework.routers import DefaultRouter

"""
第一种重写url配置的方法
goods_list = GoodsListViewSet.as_view({
    # 将两种请求与此view绑定，前面就不用重写
    get和post方法
    'get': 'list',
    # post请求，给前端提供上传商品的接口
    'post': 'create',
})
"""
# 第二种使用router配置url 的方法
# 创建一个router对象
router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")
# 配置GoodsCategory的url
router.register(r'categorys', CategoryViewset, base_name="categorys")

# router.register(r'users', UserViewset, base_name="users")


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 配置rest_framework的登陆url，和访问media资源的api
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # drf自带的token用户认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口,可以自己命名
    url(r'^login/', obtain_jwt_token),
    # 商品的列表页
    # 基础的列表实现
    # url(r'goods/$', GoodsListView.as_view()),

    # 使用router所以废弃
    # url(r'goods/$', GoodsListViewSet.as_view(), name='good-list'),

    # 使用router的url配置
    url(r'^', include(router.urls)),
    # 配置文档功能
    url(r'docs/', include_docs_urls(title='慕学生鲜'))

    # rest_framework
]
