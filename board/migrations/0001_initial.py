# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detection_at', models.DateTimeField()),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('spread_ip', models.GenericIPAddressField()),
                ('waypoint_ip', models.GenericIPAddressField()),
                ('spread_route', models.TextField()),
                ('spread_feature_text', models.TextField()),
                ('spread_feature_image', models.ImageField(blank=True, upload_to='')),
                ('detection_pattern', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]