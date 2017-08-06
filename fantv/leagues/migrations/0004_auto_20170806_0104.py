# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0003_team_league'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='name_first',
        ),
        migrations.AddField(
            model_name='player',
            name='name_last',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='player',
            name='username',
            field=models.CharField(default=models.CharField(max_length=256), max_length=256),
        ),
    ]