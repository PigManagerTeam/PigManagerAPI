# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from users.models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    ordering = ('user',)
    actions_on_top = True;
    actions_on_bottom = True;
    # list_filter = ('user', 'user_name', 'user_gender', 'user_email', 'user_nickname', 'user_phone', 'user_address', 'user_gravatar')
    list_display = ('user', 'user_name', 'user_gender', 'user_email', 'user_nickname', 'user_phone', 'user_address', 'user_gravatar')
    search_fields = ('user', 'user_name', 'user_gender', 'user_email', 'user_nickname', 'user_phone', 'user_address', 'user_gravatar')

admin.site.register(UserInfo, UserInfoAdmin)
