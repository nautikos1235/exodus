# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_query', '0007_auto_20170924_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisrequest',
            name='apk',
            field=models.FileField(upload_to='apks/ffc0c815-33bd-4f79-9e81-02420db71ad0'),
        ),
        migrations.AlterField(
            model_name='analysisrequest',
            name='storage_path',
            field=models.TextField(default='apks/ffc0c815-33bd-4f79-9e81-02420db71ad0'),
        ),
    ]