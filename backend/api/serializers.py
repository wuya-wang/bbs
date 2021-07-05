# -*- coding: utf-8 -*-
# @Author: wanghaoran
# @Time  : 2021/7/5 16:02
from rest_framework import serializers
from api import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', "last_login", 'avatar']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer

    class Meta:
        model = models.Post
        fields = ['id', 'title', "text", 'author']
