# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午2:30
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import UserProfile


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='名', max_length=50, required=False)
    last_name = forms.CharField(label='姓', max_length=50, required=False)
    org = forms.CharField(label='机构', max_length=50, required=False)
    telephone = forms.CharField(label='电话', max_length=50, required=False)


class SignupForm(forms.Form):
    def signup(self, request, user):
        user_profile = UserProfile()
        user_profile.user = user
        user.save()
        user_profile.save()
