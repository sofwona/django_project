# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-04 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0011_auto_20170404_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='transaction_id',
            field=models.CharField(default=3, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default=3, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
