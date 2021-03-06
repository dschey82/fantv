# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from show.models import Show, Episode

# Create your models here.
class League(models.Model):
    show = models.ForeignKey('show.Show', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Scorecard(models.Model):
    name = models.CharField(max_length=256)
    episode = models.ForeignKey('show.Episode', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Statistic(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

class Player(models.Model):
    name_first = models.CharField(max_length=256)
    name_last = models.CharField(max_length=256, blank=True)
    username = models.CharField(max_length=256, default=name_first)

    def __str__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey('Player', on_delete=models.CASCADE)
    league = models.ForeignKey('League', on_delete=models.CASCADE)

    def __str__(self):
        return self.name