# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from users.models import UserInfo
from django.contrib.auth.models import User, Group
from users.serializers import UserSerializer, UserInfoSerializer

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
