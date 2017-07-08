# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class UserInfo(models.Model):
    GENDER_CHOICES = (
        (u'man', u'男'),
        (u'feman', u'女')
    )
    user = models.OneToOneField(User)
    user_name = models.CharField(max_length=32, blank=True, default=None, verbose_name=_(u'用户姓名'))
    user_gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name=_(u'用户性别'))
    user_email = models.EmailField(max_length=50, blank=True, default=None, verbose_name=_(u'用户邮箱'))
    user_nickname = models.CharField(max_length=50, blank=True, default=None, verbose_name=_(u'用户昵称'))
    user_phone = models.CharField(max_length=20, blank=True, default=None, verbose_name=_(u'联系方式'))
    user_address = models.CharField(max_length=150, blank=True, default=None, verbose_name=_(u'家庭住址'))
    user_gravatar = models.CharField(max_length=200, blank=True, default=None, verbose_name=_(u'用户头像'))

    class Meta:
        app_label = 'users'
        db_table = 'pm_userinfo'
        verbose_name = u'用户信息'
        verbose_name_plural = u'用户信息'


