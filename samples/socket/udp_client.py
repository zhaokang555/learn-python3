#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'AAA', b'BBB', b'CCC']:

    # 发送数据:
    for x in range(1,5):
    	time.sleep(2)
    	print(x, "...")
    
    s.sendto(data, ('127.0.0.1', 9999))

    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()
