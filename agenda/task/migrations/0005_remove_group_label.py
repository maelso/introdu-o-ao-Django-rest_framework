# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20170203_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='label',
        ),
    ]
