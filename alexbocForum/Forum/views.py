# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as auth_logout
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic.base import View

User = get_user_model()

class IndexView(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            print('I am ' + user.username)
            return render(request, 'Forum/index.html')
        else:
            return HttpResponseRedirect(reverse('User:login'))


class LogoutRedirectView(RedirectView):
    pattern_name = 'User:login'

    def get_redirect_url(self, *args, **kwargs):
        auth_logout(self.request)
        print('I log out successfully!')
        return super(LogoutRedirectView, self).get_redirect_url(*args, **kwargs)
