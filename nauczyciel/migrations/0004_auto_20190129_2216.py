# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-29 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nauczyciel', '0003_auto_20181218_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
