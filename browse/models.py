# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipment(models.Model):
    listing_type = models.CharField(max_length=5)
    address = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    type = models.CharField(max_length=40)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    attachments = models.TextField()
    hauling_options = models.TextField()
    trailer = models.CharField(max_length=3)
    operator = models.CharField(max_length=3)
    fuel = models.TextField()
    date_available = models.DateField()
    expiration_date = models.DateField()
    date_needed = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    comments = models.TextField()

    class Meta:
        managed = False
        db_table = 'equipment'


class Material(models.Model):
    listing_type = models.CharField(max_length=5)
    address = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    type = models.CharField(max_length=40)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_available = models.DateField()
    expiration_date = models.DateField()
    load_price = models.DecimalField(max_digits=6, decimal_places=2)
    haul_distance = models.DecimalField(max_digits=6, decimal_places=2)
    haul_price = models.DecimalField(max_digits=6, decimal_places=2)
    media_dir = models.TextField()
    notifications = models.CharField(max_length=3)
    comments = models.TextField()

    class Meta:
        managed = False
        db_table = 'material'


class Site(models.Model):
    listing_type = models.CharField(max_length=5)
    address = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    surface = models.CharField(max_length=20)
    fenced = models.CharField(max_length=7)
    gated = models.CharField(max_length=3)
    num_entrances = models.IntegerField()
    width_entrances = models.CharField(max_length=20)
    utilities = models.TextField()
    ammenities = models.TextField()
    date_available = models.DateField()
    expiration_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    comments = models.TextField()

    class Meta:
        managed = False
        db_table = 'site'
