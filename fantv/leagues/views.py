# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import League, Team, Player, Scorecard, Statistic

# Create your views here.
def index(request):
    return render(request, "leagues/index.html")

def league_detail(request, id):
    teams = Team.objects.filter(league=id)
    league = League.objects.filter(id=id)
    context = {"league": league, "teams": teams}
    return render(request, "leagues/detail.html", context)