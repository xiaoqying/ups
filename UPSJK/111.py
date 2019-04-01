#/usr/bin/python
#coding:utf8
import socket,time
IP = '0.0.0.0'
PORT = 4002
server = socket.socket()
server.bind((IP, PORT))
server.listen(100)

cli, addr = server.accept()
print('Connected by', addr)
n = 0
info = ''
while n < 5:
    print("waiting ..........")
    data = 'Q1\r'

    cli.sendall(data.encode())
    info = cli.recv(10240)
    # print(info.decode())
    contex = ''
    if len(info) > 1:
        a = info.decode().replace('(', '').split()
        contex = ''' 
输入电压：%s V
输入故障电压：%s V
输出电压：%s V
输出电流：%s
输入频率：%s HZ
电池电压：%s V
温度:%s ℃
''' % (a[0], a[1], a[2], a[3] + '%', a[4], a[5], a[6])
    # print(info)
    n += 1
    time.sleep(2)
server.close()
print(contex)