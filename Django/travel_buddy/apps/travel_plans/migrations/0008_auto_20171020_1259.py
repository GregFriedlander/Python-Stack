# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_plans', '0007_auto_20171020_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trips2',
            name='createdby',
        ),
        migrations.AddField(
            model_name='trips2',
            name='user_created',
            field=models.ForeignKey(default='test', on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to='travel_plans.Users'),
            preserve_default=False,
        ),
    ]
