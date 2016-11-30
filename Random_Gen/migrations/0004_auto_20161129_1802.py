# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Random_Gen', '0003_auto_20161108_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gems',
            old_name='gems_percent_lower',
            new_name='percent_lower',
        ),
        migrations.RenameField(
            model_name='gems',
            old_name='gems_percent_upper',
            new_name='percent_upper',
        ),
        migrations.RenameField(
            model_name='gems',
            old_name='gem_value_dice_number',
            new_name='value_dice_number',
        ),
        migrations.RenameField(
            model_name='gems',
            old_name='gem_value_dice_size',
            new_name='value_dice_size',
        ),
        migrations.AlterField(
            model_name='gems',
            name='gem_name',
            field=models.CharField(max_length=6000),
        ),
    ]