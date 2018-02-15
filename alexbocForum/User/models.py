# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from alexbocForum import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import hashlib
import os

def encry(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()

def upload_avatar(instance, filename):
    fn, ext = os.path.splitext(filename)
    fn = instance.user_name
    filename = fn + ext
    pre_file_dir = os.path.join(settings.MEDIA_ROOT, ('avatars/%s' % (filename))).replace('\\', '/')

    if os.path.exists(pre_file_dir):
        os.remove(pre_file_dir)
    return os.path.join('avatars', filename)

@python_2_unicode_compatible
class User(models.Model):
    user_name = models.CharField('User Name', max_length=200, default='')
    password = models.CharField('Password', max_length=200, default=encry('123456'), blank=True)
    sign = models.CharField('Personal Signature', max_length=200, default='')
    avatar = models.ImageField(upload_to=upload_avatar, default='avatars/default.jpg')

    def __str__(self):
        return self.user_name

    def __unicode__(self):
        return self.user_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
