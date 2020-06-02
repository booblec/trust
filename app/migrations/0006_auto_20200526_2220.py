# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-26 19:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200526_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 26, 22, 20, 46, 537179), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 26, 22, 20, 46, 538178), verbose_name='Дата'),
        ),
    ]