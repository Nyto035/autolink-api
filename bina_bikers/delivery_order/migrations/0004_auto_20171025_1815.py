# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_order', '0003_auto_20170924_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryorder',
            name='distance',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deliveryorder',
            name='total_cost',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
