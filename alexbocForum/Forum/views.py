# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    user = request.user
    return render(request, 'Forum/index.html', {'user': user})
