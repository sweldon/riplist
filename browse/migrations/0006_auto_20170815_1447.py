# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-15 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0005_auto_20170815_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='images',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='images',
            field=models.TextField(blank=True, null=True),
        ),
    ]
