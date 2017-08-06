# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(League)
admin.site.register(Scorecard)
admin.site.register(Statistic)
admin.site.register(Team)
admin.site.register(Player)