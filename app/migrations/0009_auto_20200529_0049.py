# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-28 21:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200529_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(default='temp.png', upload_to='', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 29, 0, 49, 19, 31201), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 29, 0, 49, 19, 32202), verbose_name='Дата'),
        ),
    ]
