# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=150, verbose_name='Descrição'),
        ),
    ]