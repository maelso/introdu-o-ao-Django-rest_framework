# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20170203_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
    ]