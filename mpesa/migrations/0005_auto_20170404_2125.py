# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-04 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0004_auto_20170404_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='firstname',
        ),
    ]
