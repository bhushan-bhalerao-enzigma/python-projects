# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-01 10:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContactManagerApp', '0002_auto_20170701_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='LastModifiedDate',
        ),
    ]