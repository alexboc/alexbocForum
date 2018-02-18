# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from alexbocForum import settings as mysettings
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
import hashlib
import os

def upload_avatar(instance, filename):
    fn, ext = os.path.splitext(filename)
    fn = instance.user_name
    filename = fn + ext
    pre_file_dir = os.path.join(mysettings.MEDIA_ROOT, ('avatars/%s' % (filename))).replace('\\', '/')

    if os.path.exists(pre_file_dir):
        os.remove(pre_file_dir)
    return os.path.join('avatars', filename)

@python_2_unicode_compatible
class User(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='user',
        verbose_name=_('User'), blank=True, null=True, default='')
    nickname = models.CharField(_('Nickname'), max_length=255, blank=False, default='')
    sign = models.CharField(_('Personal Signature'), max_length=255, default='')
    avatar = models.ImageField(upload_to=upload_avatar, default='avatars/default.jpg')

    def __str__(self):
        return self.nickname or self.user.username
