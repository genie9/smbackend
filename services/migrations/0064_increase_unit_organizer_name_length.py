# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-20 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0063_make_unit_connection_name_longer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='organizer_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]