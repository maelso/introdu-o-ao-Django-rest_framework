# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('description', models.CharField(max_length=150, verbose_name='Descrição')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('group', models.CharField(max_length=50, verbose_name='Grupo da Tarefa')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
