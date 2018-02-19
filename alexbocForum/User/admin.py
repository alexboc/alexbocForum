# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User information', {'fields': ['username', 'password', 'nickname', 'sign',
    'avatar']}),
        ('Admin information', {'fields': ['is_staff', 'groups', 'user_permissions']}),
    ]

    list_display = ('username', 'avatar', 'is_staff')


admin.site.register(UserProfile, UserProfileAdmin)
