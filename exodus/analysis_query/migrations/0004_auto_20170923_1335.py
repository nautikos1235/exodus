# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_query', '0003_auto_20170922_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisrequest',
            name='apk',
            field=models.FileField(upload_to='apks/c9ac441b-680c-4579-b584-682e93bfe4a9'),
        ),
    ]