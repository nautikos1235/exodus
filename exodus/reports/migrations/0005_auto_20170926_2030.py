# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20170924_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='httpspayload',
            name='destination_uri',
            field=models.CharField(max_length=2000),
        ),
    ]
