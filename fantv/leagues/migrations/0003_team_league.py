# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='league',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='leagues.League'),
            preserve_default=False,
        ),
    ]