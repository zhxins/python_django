# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-04 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]