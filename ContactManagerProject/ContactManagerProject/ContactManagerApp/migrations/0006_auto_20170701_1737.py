# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-01 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactManagerApp', '0005_auto_20170701_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='LastName',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]