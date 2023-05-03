#!/usr/bin/python
# -*- coding: utf-8 -*-
# fileName ProxyIOTest.Py
import time
from HSC3Api import CommApi
from HSC3Api import ProxyIO


# 连接
# cmApi CommApi对象
# strIP (str)连接IP
# uport (usinged int)端口
# return 1-连接成功，0-连接失败
def connectIPC(cmApi, strIP, uPort):
    cmApi.setAutoConn(1)
    cmApi.connect(strIP, uPort)
    time.sleep(1)
    if cmApi.isConnected():
        return 1
    else:
        return 0


cmm = CommApi.CommApi("..\\log\\test")
proIO = ProxyIO.ProxyIO(cmm)

if connectIPC(cmApi=cmm, strIP="10.10.56.214", uPort=23234):
    print(proIO.getMaxDinNum())
    print(proIO.getMaxDoutNum())
    print(proIO.getMaxDinGrp())
    print(proIO.getMaxDoutGrp())
    # 获取IO 值和状态
    for num in range(0, 16):
        print(proIO.getDinGrp(num))
    for num in range(0, 16):
        print(proIO.getDoutGrp(num))
    for num in range(0, 16):
        print(proIO.getDinMaskGrp(num))
    for num in range(0, 16):
        print(proIO.getDoutMaskGrp(num))
    # 设置IO 值和状态
    for num in range(0, 32):
        proIO.setDinMaskBit(num, True)
    for num in range(0, 32):
        proIO.setDoutMaskBit(num, True)
    for num in range(0, 32):
        proIO.setDin(num, True)
    for num in range(0, 32):
        proIO.setDout(num, True)
    # 再次获取 IO 值和状态
    for num in range(0, 2):
        print(proIO.getDinGrp(num))
    for num in range(0, 2):
        print(proIO.getDoutGrp(num))
    for num in range(0, 2):
        print(proIO.getDinMaskGrp(num))
    for num in range(0, 2):
        print(proIO.getDoutMaskGrp(num))

# 断开链接
cmm.disconnect()
print("退出")

