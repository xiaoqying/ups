# coding:utf-8
from django.db import models

# Create your models here.
class Region(models.Model):
    name=models.CharField(max_length=32,null=True,verbose_name='地点名称')
    ip=models.CharField(max_length=32,null=True,verbose_name='IP地址')
class UpsInfo(models.Model):
    name=models.CharField(max_length=32,null=True,verbose_name='地点名称')
    upsmd=models.ForeignKey(to='UpsMd',null=True,verbose_name='UPS类型')
    ipaddress=models.CharField(max_length=32,null=True,verbose_name='IP地址')
    in_voltage=models.CharField(max_length=32,null=True,verbose_name='输入电压')
    in_fault_voltage=models.CharField(max_length=32,null=True,verbose_name='输入故障电压')
    out_voltage=models.CharField(max_length=32,null=True,verbose_name='输出电压')
    out_current=models.CharField(max_length=32,null=True,verbose_name='输出电流')
    in_frequency=models.CharField(max_length=32,null=True,verbose_name='输入频率')
    battery_voltage=models.CharField(max_length=32,null=True,verbose_name='电池电压')
    temperature=models.CharField(max_length=32,null=True,verbose_name='温度')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'UPS信息表'

class UpsMd(models.Model):
    name=models.CharField(max_length=32,null=True,verbose_name='类型名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '类型名称'

class UpsData(models.Model):
    ip=models.CharField(max_length=32,null=True,verbose_name='ip地址')
    data=models.CharField(max_length=64,null=True,verbose_name='数据')
    time=models.CharField(max_length=64,null=True,verbose_name='时间')

class RealData(models.Model):
    ip=models.CharField(max_length=32,null=True,verbose_name='ip地址')
    data = models.CharField(max_length=64, null=True, verbose_name='实时数据')
