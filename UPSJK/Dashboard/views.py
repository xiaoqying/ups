# coding: utf-8
from django.shortcuts import render
from django.views import View
import time,socket
import pymysql
from Dashboard import models
#from dwebsocket.decorators import accept_websocket,require_websocket
# Create your views here.
class GetInfo(View):
    def get(self,request):
        conn = pymysql.connect(host='192.168.101.24', user='ups', passwd='ups', db='ups')
        cursor = conn.cursor()
        # sql = """INSERT INTO Dashboard_realdata(ip, data)
        #                                 SELECT ip, data
        #                                     from	Dashboard_upsdata
        #                                     where id in(
        #                                         select MAX(t.id)
        #                                         from Dashboard_upsdata t
        #                                         group by t.ip)"""
        #
        # sql1 = """DELETE from Dashboard_realdata"""
        sql2 = """DELETE from Dashboard_upsinfo"""
        # cursor.execute(sql1)
        cursor.execute(sql2)
        conn.commit()
        sql4="""SELECT ip, data from	Dashboard_upsdata_temp"""
        cursor.execute(sql4)
        data=cursor.fetchall()
        # print('---------',data)
        # cursor.execute(sql)
        # obj1=models.RealData.objects.all()
        dic={}
        '''data里面的数据是ip+data的元组 （（192.168.1.1,220,222,222,000,33,55....），（））'''
        for i in data:
            addr=i[0]
            data=i[1].split()
            # print('+++++++++++', data)
            infos = [data[0], data[1], data[2], data[3] + '%', data[4], data[5].replace('.',''), data[6]]
            # print(type(data[1]))
            obj3 = models.Region.objects.filter(ip=addr).first()
            # print('111111111')
            # print("----->",obj3.ip,obj3.name)
            dic = {
                'name':obj3.name,
                "upsmd_id": 1,
                'ipaddress': obj3.ip,
                'in_voltage': infos[0],
                'in_fault_voltage': infos[1],
                'out_voltage': infos[2],
                'out_current': infos[3],
                'in_frequency': infos[4],
                'battery_voltage': infos[5],
                'temperature': infos[6],
            }
            # print(dic)
            models.UpsInfo.objects.create(**dic)
        err_msg='UPS状态异常...'
        obj2 = models.UpsInfo.objects.all()
        return render(request, 'index.html', locals())
    def post(self,request):
        obj2 = models.UpsInfo.objects.all()
        return render(request, 'index.html', locals())
