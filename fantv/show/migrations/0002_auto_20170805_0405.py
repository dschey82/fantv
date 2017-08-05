# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='imdb_link',
            field=models.URLField(default='http://www.imdb.com'),
        ),
        migrations.AddField(
            model_name='character',
            name='imdb_link',
            field=models.URLField(default='http://www.imdb.com'),
        ),
        migrations.AddField(
            model_name='episode',
            name='imdb_link',
            field=models.URLField(default='http://www.imdb.com'),
        ),
        migrations.AddField(
            model_name='show',
            name='imdb_link',
            field=models.URLField(default='http://www.imdb.com'),
        ),
    ]