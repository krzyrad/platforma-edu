# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-18 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_topic_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'notatki'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name_plural': 'wiadomosci'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name_plural': 'aktualnosci'},
        ),
        migrations.AlterModelOptions(
            name='resources',
            options={'verbose_name_plural': 'pliki'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'studenci'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name_plural': 'tematy'},
        ),
    ]
