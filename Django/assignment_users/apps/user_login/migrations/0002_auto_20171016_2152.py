# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-16 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
