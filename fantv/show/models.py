# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=256)
    imdb_link = models.URLField(default='http://www.imdb.com')

    def __str__(self):
        return self.name    

class Episode(models.Model):
    title = models.CharField(max_length=256, blank=True)
    imdb_link = models.URLField(default='http://www.imdb.com')
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    season = models.IntegerField(default=1)
    serial = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Character(models.Model):
    name_first = models.CharField(max_length=256)
    name_last = models.CharField(max_length=256,blank=True)
    imdb_link = models.URLField(default='http://www.imdb.com')
    episodes = models.ManyToManyField('Episode')
    actors = models.ManyToManyField('Actor')

    def __str__(self):
        if (name_last != ""):
            return self.name_first + " " + self.name_last
        else:
            return self.name_first

class Actor(models.Model):
    name_first = models.CharField(max_length=256)
    name_last = models.CharField(max_length=256)
    imdb_link = models.URLField(default='http://www.imdb.com')
    characters = models.ManyToManyField('Character')

    def __str__(self):
        if (name_last != ""):
            return self.name_first + " " + self.name_last
        else:
            return self.name_first