# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20170203_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Group'),
        ),
    ]
