# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-02-10 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_type', models.CharField(max_length=5)),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=10)),
                ('lat', models.CharField(max_length=20)),
                ('lng', models.CharField(max_length=20)),
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
                ('rate', models.CharField(max_length=10)),
                ('comments', models.TextField()),
                ('author', models.IntegerField()),
            ],
            options={
                'db_table': 'equipment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_type', models.CharField(max_length=5)),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=10)),
                ('lat', models.CharField(max_length=20)),
                ('lng', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=40)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rate', models.CharField(max_length=10)),
                ('date_available', models.DateField()),
                ('expiration_date', models.DateField()),
                ('load_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('haul_distance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('haul_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('media_dir', models.TextField()),
                ('notifications', models.CharField(max_length=3)),
                ('comments', models.TextField()),
                ('author', models.IntegerField()),
            ],
            options={
                'db_table': 'material',
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
                ('lat', models.CharField(max_length=20)),
                ('lng', models.CharField(max_length=20)),
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
                ('rate', models.CharField(max_length=10)),
                ('comments', models.TextField()),
                ('author', models.IntegerField()),
            ],
            options={
                'db_table': 'site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=2)),
                ('phone', models.CharField(max_length=10)),
                ('business', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_profile',
                'managed': False,
            },
        ),
    ]
