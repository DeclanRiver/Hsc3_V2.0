#!/usr/bin/python
# -*- coding: utf-8 -*-
# fileName ProxySysTest.Py
import time
from HSC3Api import CommApi
from HSC3Api import ProxySys


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
proSys = ProxySys.ProxySys(cmm)


if connectIPC(cmApi=cmm, strIP="10.10.56.214", uPort=23234):
    # 查询系统是否就绪
    ret = proSys.isReady()
    print(ret)
    if ret[1]:
        # 获取版本信息
        print(proSys.getVersion("Release"))
        print(proSys.getVersion("CL"))
        print(proSys.getVersion("ML"))
        print(proSys.getVersion("Api"))
        # 重启系统
        proSys.reboot()
        time.sleep(10)
        if connectIPC(cmApi=cmm, strIP="10.10.56.214", uPort=23234):
            # 等待系统就绪
            while (True):
                ret = proSys.isReady()
                print(ret)
                if ret[1]:
                    break
                else:
                    time.sleep(1)
            ret = proSys.getMessage(1000)
            print(ret)
            if ret[0] == 0:
                print(proSys.queryError(ret[2]))
        else:
            print("重启10s后, 未能连接到系统")
    else:
        print("系统未就绪")
else:
    print("连接失败")
# 断开链接
cmm.disconnect()
print("退出")







