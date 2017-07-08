# -*- coding: utf-8 -*-

from users.models import UserInfo
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('url', 'id', 'user', 'user_name', 'user_gender', 'user_email', 'user_nickname', 'user_phone', 'user_address', 'user_gravatar')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        userinfo = UserInfoSerializer
        fields = ('url', 'userinfo', 'id', 'username', 'email')


