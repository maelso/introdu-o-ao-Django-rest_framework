# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20170204_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id_group',
        ),
        migrations.AddField(
            model_name='task',
            name='group',
            field=models.IntegerField(choices=[(1, 'PRIMARIO'), (2, 'SECUNDARIO')], default=1),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
