# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-01 10:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('MobileNo', models.IntegerField()),
                ('LastModifiedDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]