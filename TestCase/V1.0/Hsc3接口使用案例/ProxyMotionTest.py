#!/usr/bin/python
# -*- coding: utf-8 -*-
# fileName ProxyMotionTest.Py
import sys
sys.path.append("HSC3Api")
import time
from HSC3Api import CommApi
from HSC3Api import ProxyMotion
from HSC3Api import Hsc3ApiPy


# 测试机型：JR605
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
proMot = ProxyMotion.ProxyMotion(cmm)

if connectIPC(cmApi=cmm, strIP="10.10.56.214", uPort=23234):
    # 设置坐标系
    print(proMot.getManualStat())
    print(proMot.getWorkFrame(0))
    proMot.setWorkFrame(0, Hsc3ApiPy.FrameType.FRAME_WORLD)
    print(proMot.getWorkFrame(0))
    # 设置操作模式
    print(proMot.getOpMode())
    proMot.setOpMode(opMode=Hsc3ApiPy.OpMode.OP_T2)
    print(proMot.getOpMode())
    # 设置手动倍率
    print(proMot.getJogVord())
    proMot.setJogVord(10)
    print(proMot.getJogVord())
    # 设置手动运行模式
    print(proMot.getManualMode())
    proMot.setManualMode(Hsc3ApiPy.ManualMode.MANUAL_CONTINUE)
    print(proMot.getManualMode())
    # 设置寸动距离
    print(proMot.getInchLen())
    proMot.setInchLen(5)
    print(proMot.getInchLen())
    # 设置零点
    print(proMot.getHomePosition(0))
    proMot.setHomePosition(0, [0, -90, 180, 0, 90, 0, 0, 0, 0], 63)
    print(proMot.getHomePosition(0))
    # 设置限位
    ret = proMot.getJointLimit(0)
    print(ret)
    print(ret[1][0])
    proMot.setJointLimit(0, [200, 0, 240, 180, 115, 360, 0, 0, 0], [-200, -180, 80, -180, -115, -360, 0, 0, 0], 63) # 00111111
    print(proMot.getJointLimit(0))
    # 获取内部轴数
    print(proMot.getRobAxisCount(0))
    print(proMot.getAuxAxisCount(0))
    print(proMot.getAuxAxisBegin(0))
    # 使能
    proMot.setGpEn(0, 1)
    ret, gpEn = proMot.getGpEn(0)
    print(gpEn)
    print("错误码:%d,使能状态:gpEn:%d" % (ret, gpEn))
    if gpEn:
        print("已使能")
        # 运动到点
        pos = Hsc3ApiPy.GeneralPos()
        pos.isJoint = True
        pos.ufNum = -1
        pos.utNum = -1
        pos.config = 0x100000
        pos.vecPos = [0, -90, 180, 0, 90, 0, 0, 0, 0]
        proMot.moveTo(0, pos, False)
        time.sleep(5)
        # 获取位置数据
        print(proMot.getJntData(0))
        print(proMot.getAuxData(0))
        print(proMot.getLocData(0))
        print(proMot.getConfig(0))
        # 设置工具坐标数据，工件坐标数据
        print(proMot.getTool(0, 1))
        proMot.setTool(0, 1, [0, -90, 180, 0, 90, 0])
        print(proMot.getTool(0, 1))
        print(proMot.getWorkpiece(0, 1))
        proMot.setWorkpiece(0, 1, [0, -90, 180, 0, 90, 0])
        print(proMot.getWorkpiece(0, 1))
        # 设置工具号，工件号
        print(proMot.getToolNum(0))
        proMot.setToolNum(0, 1)
        print(proMot.getToolNum(0))
        print(proMot.getWorkpieceNum(0))
        proMot.setWorkpieceNum(0, 1)
        print(proMot.getWorkpieceNum(0))
        # 获取轴组数据
        ret, gpData = proMot.getGroupData(0)
        print(ret)
        print(gpData.en)
        print(gpData.mode)
        print(gpData.frame)
        print(gpData.vordJog)
        print(gpData.vordAut)
        print(gpData.inchLen)
        print(gpData.ufNum)
        print(gpData.utNum)
        print(gpData.config)
        print(gpData.dataJnt)
        print(gpData.dataAux)
        print(gpData.dataLoc)
        # 获取可用机型的名字
        print(proMot.getRobTypeNameList())
        # 获取轴组配置
        ret, gpCfg = proMot.getGroupConfig(0)
        print(ret)
        print(gpCfg.typeRob)
        print(gpCfg.strTypeName)
        print(gpCfg.cntRob)
        print(gpCfg.cntAux)
        print(gpCfg.beginAux)
        # 设置机型
        # proMot.setRobType(0, "JR605")
    while (1):
        print("请输入命令：")
        cmd = input()
        if cmd == "q":
            print("退出")
            break
        else:
            ret = cmm.execCmd(cmd, 3)
            print(ret)

# 断开链接
cmm.disconnect()

