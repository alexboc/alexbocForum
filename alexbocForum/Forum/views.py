# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    user = request.user
    if user.is_authenticated:
        print('I am ' + user.username)
        return render(request, 'Forum/index.html')
    else:
        return HttpResponseRedirect(reverse('User:login'))
