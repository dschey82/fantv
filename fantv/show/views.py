# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Show

# Create your views here.
def show_index(request):
    return render(request, 'show/index.html', {'shows': Show.objects.all()})