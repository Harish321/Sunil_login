# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-28 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_delete_check_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='check_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
            ],
        ),
    ]
