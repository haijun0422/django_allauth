# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午2:11
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from .views import profile, profile_update

app_name = 'users'
urlpatterns = [
    url(r'^profile/', profile, name='profile'),
    url(r'^profile_update/', profile_update, name='profile_update')
]
