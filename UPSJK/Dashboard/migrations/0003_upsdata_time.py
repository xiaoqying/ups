# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_upsdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='upsdata',
            name='time',
            field=models.CharField(max_length=64, null=True, verbose_name='时间'),
        ),
    ]
