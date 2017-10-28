# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-08 20:20
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryGood',
            fields=[
                ('ts_document', models.TextField(blank=True, help_text='The content that will be searched over', null=True)),
                ('ts_document_vector', django.contrib.postgres.search.SearchVectorField(blank=True, help_text='The ts_vector for the document field', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_delivery_goods', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ('-updated', '-created'),
            },
        ),
    ]
