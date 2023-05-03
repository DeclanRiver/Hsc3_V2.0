#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : ProxyMotion.py
# Detail   : 华数III型二次开发接口测试 - 业务接口 - 采集功能代理
#            提供了III型控制器系统功能相关业务接口测试及使用方法示例。
from HSC3Api import ProxyCollect
from HSC3Api import CommApi
from HSC3Api import Hsc3ApiPy
import time


# 连接
# cmApi CommApi对象
# strIP (str)连接IP
# uport (usinged int)端口
# return 1-连接成功，0-连接失败
def connectIPC(cmApi, strIP, uPort):
    cmApi.setUseUdp(True)
    cmApi.setAutoConn(1)
    cmApi.connect(strIP, uPort)
    time.sleep(1)
    if cmApi.isConnected():
        return 1
    else:
        return 0
    # def connectIPC(cmApi,strIP,uPort):
    #     cmApi.setUseUdp(True)
    #     cmApi.setAutoConn(1)
    #     cmApi.connect(strIP,uPort)
    #     time.sleep(1)
    #     if cmApi.isConnected():
    #         return 1
    #     else:
    #         return 0


cmm = CommApi.CommApi("..\\log\\test")
proCol = ProxyCollect.ProxyCollect(cmm)

# com = CommApi.CommApi("..\\log\\test")
# proColl = ProxyCollect.ProxyCollect(com)
# 连接
if connectIPC(cmApi=cmm, strIP="10.10.56.214", uPort=23234):
    time.sleep(4)
    # 添加采集任务
    proCol.addTask(1, 2, "var.axis[0].vfb")
    # proCol.addTask(3, 2, "var.axis[0].afb")
    # 获取已存在的采集任务列表
    print(proCol.getExistTasks())
    # 开始采集任务
    proCol.start(1)
    # 获取正在运行的采集任务
    print(proCol.getRunningTasks())
    cmd = ""
    while cmd != "q":
        # 获取采集数据
        print(cmm.getUdpMsg())
        cmd = input()# 停止采集任务
    proCol.stop(1)
    print(proCol.getExistTasks())
    print(proCol.getRunningTasks())
    # 删除采集任务
    print(proCol.delTask(1))
    time.sleep(2)
    print(proCol.getExistTasks())
    # 获取系统的时间戳
    print(proCol.getCurTimestamp())
# 断开链接
cmm.disconnect()
# def connectIP(cmAPI = cmm,strIP = '10.10.56.214',rport = 23234):
#     time.sleep(4)
#     proCol.addTask(1, 2, "var.axis[0].vfb")
#     print(proCol.getExistTasks())
#     cmd = ""
#     while cmd != "q":
#         print(cmm.getUdpMsg())
#         cmd = input()
#     proCol.stop(1)
#     print(proCol.getExistTasks())
#     print(proCol.getRunningTasks())
#     print(proCol.delTask())
#     print(proCol.getCurTimestamp())
#
#
# cmm.disconnect()