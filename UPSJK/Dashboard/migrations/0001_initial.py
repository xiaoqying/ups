# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 03:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UpsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='地点名称')),
                ('ipaddress', models.CharField(max_length=32, null=True, verbose_name='IP地址')),
                ('in_voltage', models.CharField(max_length=32, null=True, verbose_name='输入电压')),
                ('in_fault_voltage', models.CharField(max_length=32, null=True, verbose_name='输入故障电压')),
                ('out_voltage', models.CharField(max_length=32, null=True, verbose_name='输出电压')),
                ('out_current', models.CharField(max_length=32, null=True, verbose_name='输出电流')),
                ('in_frequency', models.CharField(max_length=32, null=True, verbose_name='输入频率')),
                ('battery_voltage', models.CharField(max_length=32, null=True, verbose_name='电池电压')),
                ('temperature', models.CharField(max_length=32, null=True, verbose_name='温度')),
            ],
            options={
                'verbose_name_plural': 'UPS信息表',
            },
        ),
        migrations.CreateModel(
            name='UpsMd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='类型名称')),
            ],
            options={
                'verbose_name_plural': '类型名称',
            },
        ),
        migrations.AddField(
            model_name='upsinfo',
            name='upsmd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.UpsMd', verbose_name='UPS类型'),
        ),
    ]
