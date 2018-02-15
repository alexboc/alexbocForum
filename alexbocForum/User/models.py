# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import hashlib

def encry(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()

@python_2_unicode_compatible
class User(models.Model):
    user_name = models.CharField('User Name', max_length=200, default='')
    password = models.CharField('Password', max_length=200, default=encry('123456'), blank=True)

    def __str__(self):
        return self.user_name
