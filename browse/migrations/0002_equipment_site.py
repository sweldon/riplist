# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-02-02 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_type', models.CharField(max_length=5)),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=40)),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=4)),
                ('attachments', models.TextField()),
                ('hauling_options', models.TextField()),
                ('trailer', models.CharField(max_length=3)),
                ('operator', models.CharField(max_length=3)),
                ('fuel', models.TextField()),
                ('date_available', models.DateField()),
                ('expiration_date', models.DateField()),
                ('date_needed', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('comments', models.TextField()),
            ],
            options={
                'db_table': 'equipment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_type', models.CharField(max_length=5)),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=10)),
                ('surface', models.CharField(max_length=20)),
                ('fenced', models.CharField(max_length=7)),
                ('gated', models.CharField(max_length=3)),
                ('num_entrances', models.IntegerField()),
                ('width_entrances', models.CharField(max_length=20)),
                ('utilities', models.TextField()),
                ('ammenities', models.TextField()),
                ('date_available', models.DateField()),
                ('expiration_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('comments', models.TextField()),
            ],
            options={
                'db_table': 'site',
                'managed': False,
            },
        ),
    ]