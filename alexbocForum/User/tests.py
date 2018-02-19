# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileModelTests(TestCase):

    def test_can_create_user_success(self):
        username = 'ale_test1'
        password = 'alexandrali123'
        user1 = User.objects.create_user(username = username, password=password)
        user2 = authenticate(username = username, password = password)
        self.assertEqual(user1, user2)

