#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    for x in range(1,5):
    	time.sleep(2)
    	print(x, "...")
    print(data)
    print(addr)
    print('Received from %s:%s.' % addr)

    for x in range(1,5):
    	time.sleep(2)
    	print(x, "...")
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)
