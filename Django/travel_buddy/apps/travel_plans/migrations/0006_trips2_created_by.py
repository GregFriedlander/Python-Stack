# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel_plans', '0005_auto_20171020_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips2',
            name='created_by',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to='travel_plans.Users'),
            preserve_default=False,
        ),
    ]
