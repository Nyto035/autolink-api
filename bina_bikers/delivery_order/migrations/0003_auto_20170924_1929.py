# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_order', '0002_auto_20170910_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryorder',
            name='status',
            field=models.CharField(choices=[('ACCEPTED', 'accepted'), ('PENDING', 'pending'), ('CANCELLED', 'cancelled'), ('PAID', 'paid')], default='PENDING', max_length=50),
        ),
    ]
