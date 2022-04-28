#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Author:Mikigo
@Date  :2022/4/20 0:33
@Desc  :
"""
from django import forms


class LoginForm(forms.Form):
    """用户名密码快捷校验"""
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)
