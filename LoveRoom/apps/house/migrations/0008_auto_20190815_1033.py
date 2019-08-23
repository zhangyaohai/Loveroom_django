# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-15 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_auto_20190815_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseinfo',
            name='location',
            field=models.TextField(default='--', verbose_name='位置详情'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='tag',
            field=models.TextField(default='--', verbose_name='标签'),
            preserve_default=False,
        ),
    ]