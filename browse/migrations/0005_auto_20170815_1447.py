# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-15 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0004_auto_20170528_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'managed': True},
        ),
    ]
