# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import View

class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'User/Login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('Forum:index'))
        else:
            return render(request, 'User/login.html')
