#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : ProxyVarTest.py
import time
from HSC3Api import CommApi
from HSC3Api import ProxyVar
from HSC3Api import Hsc3ApiPy

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
proVar = ProxyVar.ProxyVar(comm)

if connectIPC(comm, "10.10.56.214", 23234):
    # 设置 R 寄存器
    print(proVar.setR(3, 100))
    # 获取 R 寄存器
    print(proVar.getR(0))
    print(proVar.getR(0, 10))
    # 设置 JR 寄存器
    jPos = Hsc3ApiPy.JntPos()
    jPos.vecPos = [0, -90, 180, 0, 90, 0, 0, 0, 0]
    print(proVar.setJR(0, 2, jPos))
    # 获取 JR 寄存器
    ret = proVar.getJR(0, 0)
    print(ret[1].vecPos)
    ret = proVar.getJR(0, 0, 3)
    print(ret[1])
    for jr in ret[1]:
        print(jr.vecPos)
    # 设置 LR 寄存器
    lPos = Hsc3ApiPy.LocPos()
    lPos.ufNum = -1
    lPos.utNum = -1
    lPos.config = 0x100000
    lPos.vecPos = [0, -90, 180, 0, 90, 0, 0, 0, 0]
    print(proVar.setLR(0, 1, lPos))
    # 获取 LR 寄存器
    ret = proVar.getLR(0, 0)
    print(ret[1].vecPos)
    ret = proVar.getLR(0, 0, 3)
    print(ret[1])
    for jr in ret[1]:
        print(jr.vecPos)
    # 配置区域
    areaCfg = Hsc3ApiPy.AreaConfigData()
    areaCfg.ufnum = -1
    areaCfg.origin = [100, 100, 100]
    areaCfg.shapeType = Hsc3ApiPy.AreaShapeType.AREA_SHAPE_TYPE_BOX
    areaCfg.shapeSize = [100, 200, 100]
    areaCfg.offset = 10
    areaCfg.type = Hsc3ApiPy.AreaType.WORK_AREA
    areaCfg.outReverse = True
    areaCfg.mode = Hsc3ApiPy.ShareAreaMode.SHARE_AREA_MODE_WRN_STOP
    proVar.configArea(0, 1, areaCfg)
    # 获取区域类型
    print(proVar.getAreaType(0, 0))  # 区域 0
    print(proVar.getAreaType(0))    # 所有区域
    # 获取共享区使能
    print(proVar.getShareAreaEn(0, 0))  # 区域0
    print(proVar.getShareAreaEn(0))
    # 获取区域输出
    print(proVar.getAreaOut(0, 0))
    print(proVar.getAreaOut(0))
    # 获取区域配置
    ret = proVar.getAreaConfig(0, 1)
    print(ret[1].ufnum)
    print(ret[1].origin)
    print(ret[1].shapeType)
    print(ret[1].shapeSize)
    print(ret[1].offset)
    print(ret[1].type)
    print(ret[1].outReverse)
    print(ret[1].mode)

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

