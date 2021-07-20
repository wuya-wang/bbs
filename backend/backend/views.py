# -*- coding: utf-8 -*-
# @Author: wanghaoran
# @Time  : 2021/7/20 12:52
from rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.response import Response
from .serializer import MyTokenObtainPairSerializer


# 注册并返回token
class Register(RegisterView, MyTokenObtainPairSerializer):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        refresh = self.get_token(user)
        data = dict()
        data['refresh'] = str(refresh)
        data['token'] = str(refresh.access_token)
        return Response(status=status.HTTP_201_CREATED, data=data)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        return user
