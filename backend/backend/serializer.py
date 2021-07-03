# -*- coding: utf-8 -*-
# @Author: wanghaoran
# @Time  : 2021/7/3 18:12
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        return token

    def validate(self, attrs):
        """
        登录返回token和refresh
        :param attrs:
        :return:
        """
        data = super().validate(attrs)
        # 将access改为token
        data["token"] = data.pop("access")
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
