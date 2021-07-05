# -*- coding: utf-8 -*-
# @Author: wanghaoran
# @Time  : 2021/7/5 16:23
from django_filters import rest_framework as filters
from api import models


class UserFilter(filters.FilterSet):
    min_id = filters.NumberFilter(field_name="id", lookup_expr='gte')
    max_id = filters.NumberFilter(field_name="id", lookup_expr='lte')

    class Meta:
        model = models.User
        fields = ['id', 'username', 'min_id', 'max_id']


class PostFilter(filters.FilterSet):

    class Meta:
        models = models.Post
        fields = ["id", "author", "title"]
