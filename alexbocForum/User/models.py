# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from alexbocForum import settings as mysettings
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import hashlib
import os

def upload_avatar(instance, filename):
    fn, ext = os.path.splitext(filename)
    fn = instance.username
    filename = fn + ext
    pre_file_dir = os.path.join(mysettings.MEDIA_ROOT, ('avatars/%s' % (filename))).replace('\\', '/')

    if os.path.exists(pre_file_dir):
        os.remove(pre_file_dir)
    return os.path.join('avatars', filename)


class CustomUserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set.')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


@python_2_unicode_compatible
class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=63, unique=True)

    nickname = models.CharField(_('Nickname'), max_length=255, blank=True, default='')
    sign = models.CharField(_('Personal Signature'), max_length=255, blank=True, default='')
    avatar = models.ImageField(upload_to=upload_avatar, default='avatars/default-avatar.png')

    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELD=['']

    objects=CustomUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
          return self.username

    def get_short_name(self):
          return self.username
