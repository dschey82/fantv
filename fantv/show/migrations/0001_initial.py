# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=256)),
                ('name_last', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=256)),
                ('name_last', models.CharField(blank=True, max_length=256)),
                ('actors', models.ManyToManyField(to='show.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256)),
                ('season', models.IntegerField(default=1)),
                ('serial', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.Show'),
        ),
        migrations.AddField(
            model_name='character',
            name='episodes',
            field=models.ManyToManyField(to='show.Episode'),
        ),
        migrations.AddField(
            model_name='actor',
            name='characters',
            field=models.ManyToManyField(to='show.Character'),
        ),
    ]
