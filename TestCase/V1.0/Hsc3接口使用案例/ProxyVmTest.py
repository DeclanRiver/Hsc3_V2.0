#!/usr/bin/python
# -*- coding: utf-8 -*-
# fileName CommApiTest.Py
import time
from HSC3Api import CommApi
from HSC3Api import ProxyMotion
from HSC3Api import ProxyVm


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


comm = CommApi.CommApi("..\\log\\test")  # 构造CommApi对象
pMot = ProxyMotion.ProxyMotion(comm) #构造ProxyMotion对象
pVm = ProxyVm.ProxyVm(comm)         #构造ProxyVm对象

#连接
if connectIPC(comm, "10.10.56.214", 23234):
    pMot.setGpEn(0, 1)
    time.sleep(1)
    # 加载程序
    ret = pVm.load("./script/", "J1.PRG")
    print(ret)
    time.sleep(5)
    # 获取加载程序名列表
    print(pVm.mainProgNames())
    # 获取程序状态
    ret = pVm.progState("J1.PRG")
    print(ret)
    ret = pVm.start("J1.PRG")
    time.sleep(20)
    ret = pVm.pause("J1.PRG")
    ret = pVm.stop("J1.PRG")
    ret = pVm.unload("J1.PRG")
    # 执行命令
    while (1):
        cmd = input('请输入：')
        if cmd == "q":
            break
        ret = comm.execCmd(cmd, 3)
        print(ret)
# 断开链接
comm.disconnect()
print("退出")
