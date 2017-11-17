from django.shortcuts import render
from django.db.models import Q
# 引入django内置的登录模块
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login

from .models import UserProfile


# 重写django的登录函数
class CustomBackend(ModelBackend):
    #  重写内置的登录方法
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(mobile=username))
        # 内置方法判断密码是否正确
            if user.check_password(password):
                return user
        except Exception as e:
            return None




