# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_realdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='地点名称')),
                ('ip', models.CharField(max_length=32, null=True, verbose_name='IP地址')),
            ],
        ),
    ]
