#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : ProxyMotion.py
# Detail   : 华数III型二次开发接口 - 业务接口 - 运动功能代理
#            提供了III型控制器运动功能相关业务接口。

from HSC3Api import Hsc3ApiPy
from HSC3Api import CommApi


class ProxyMotion:
    """运动功能代理"""
    __p = 0

    def __init__(self, pCommApi):
        self.__p = Hsc3ApiPy.ProxyMotionPy(pCommApi.getId())

    # / **
    # * @ brief 设置操作模式
    # * @ param  opMode  模式
    # * /
    def setOpMode(self, opMode):
        '''
        OP_T1   T1示教模式
        OP_T2   T2示教模式
        OP_AUT  自动操作模式
        OP_EXT  外部操作模式
        OP_DRAG 拖动示教模式
        :return:manMode 模式
        '''
        return self.__p.setOpMode(opMode)

    # / **
    # * @ brief 获取操作模式
    # * @ return tuple(错误码, 操作模式)
    # * /
    def getOpMode(self):
        '''
        OP_T1   T1示教模式
        OP_T2   T2示教模式
        OP_AUT  自动操作模式
        OP_EXT  外部操作模式
        OP_DRAG 拖动示教模式
        :return:manMode 模式
        '''
        return self.__p.getOpMode()

    # / **
    # * @ brief 设置手动运行模式
    # * @ param manMode 模式
    # * /
    def setManualMode(self, manMode):
        return self.__p.setManualMode(manMode)

    # / **
    # * @ brief 获取手动运行模式
    # * @ return tuple(错误码, 手动运行模式）
    # * /
    def getManualMode(self):
        return self.__p.getManualMode()

    # / **
    # * @ brief 设置手动运行增量距离
    # * @ param length 距离大小（单位根据坐标系确定，关节：°；笛卡尔：mm )
    # * /
    def setInchLen(self, length):
        return self.__p.setInchLen(length)

    # / **
    # * @ brief 获取手动运行增量距离
    # * @ return tuple(错误码, 增量距离)
    # 增量距离（单位根据坐标系确定，关节：°；笛卡尔：mm）
    # * /
    def getInchLen(self):
        return self.__p.getInchLen()

    # / **
    # * @ brief 获取手动运行状态
    # * @ return tuple(错误码,状态)
    # * /
    def getManualStat(self):
        return self.__p.getManualStat()

    # / **
    # * @ brief 设置自动运行模式
    # * @ param mode 模式
    # * /
    def setAutoMode(self, mode):
        return self.__p.setAutoMode(mode)

    # / **
    # * @ brief 获取自动运行模式
    # * @ return tuple(错误码, 自动模式)
    # * /
    def getAutoMode(self):
        return self.__p.getAutoMode()

    # / **
    # * @ brief 设置自动运行倍率
    # * @ param vord 倍率（1 ~100，单位：\ % ）
    # * /
    def setVord(self, autoVord):
        return self.__p.setVord(autoVord)

    # / **
    # * @ brief 获取自动运行倍率
    # * @ return tuple(错误码, 倍率)
    # 倍率（1 ~100，单位：\ % ）
    # * /
    def getVord(self):
        return self.__p.getVord()

    # / **
    # * @ brief 设置手动运行倍率
    # * @ param vord 倍率（1 ~100，单位：\ % ）
    # * /
    def setJogVord(self, jogVord):
        return self.__p.setJogVord(jogVord)

    # / **
    # * @ brief 获取手动运行倍率
    # * @ return tuple(错误码, 倍率)
    # 倍率（1 ~100，单位：\ % ）
    # * /
    def getJogVord(self):
        return self.__p.getJogVord()

    # / **
    # * @ brief 操作急停
    # * @ param estop 是否急停
    # * /
    def setEstop(self, estop):
        return self.__p.setEstop(estop)

    # / **
    # * @ brief 获取是否处于急停状态
    # * @ return tuple(错误码, 急停状态)
    # * @ 急停状态:(bool)是否处于急停状态
    # * /
    def getEstop(self):
        return self.__p.getEstop()

    # / **
    # * @ brief    组使能
    # * @ param    gpId    组号（0..n - 1）
    # * @ param    en      是否使能
    # * @ return   错误码
    # * /
    def setGpEn(self, gpId, en):
        return self.__p.setGpEn(gpId, en)

    # / **
    # * @ brief 获取是否处于使能状态
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 使能状态)
    # * @ 使能状态:(bool)
    # * /
    def getGpEn(self, gpId):
        return self.__p.getGpEn(gpId)

    # / **
    # * @ brief 组复位
    # * @ param gpId 组号（0..n - 1）
    # * /
    def gpReset(self):
        return self.__p.gpReset()

    # / **
    # * @ brief 零点校准
    # * @ param gpId 组号（0..n - 1）
    # * @ param pos 零点设定值,list类型，要求9个点位数据，例：[0,-90,180,0,90,0,0,0,0]
    # * @ param mask 掩码，低9位有效，最低位代表组中第1个轴，第9位代表组中第9个轴。
    # * @ return 错误码
    # * /
    def setHomePosition(self, gpId,  pos, mask):
        return self.__p.setHomePosition(gpId,  pos, mask)

    # / **
    # * @ brief 获取零点
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 零点设定值)
    # * /
    def getHomePosition(self, gpId):
        return self.__p.getHomePosition(gpId)

    # / **
    # * @ brief 设置软限位
    # * @ param gpId 组号（0..n - 1）
    # * @ param pos 正向软限位设定值
    # * @ param neg 负向软限位设定值
    # * @ param mask 使能掩码，低9位有效，最低位代表组中第1个轴，第9位代表组中第9个轴。
    # * /
    def setJointLimit(self, gpId, pos, neg, mask):
        return self.__p.setJointLimit(gpId, pos, neg, mask)

    # / **
    # * @ brief 获取软限位
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 正向软限位设定值, 负向软限位设定值, 使能掩码)
    # 使能掩码，低9位有效，最低位代表组中第1个轴，第9位代表组中第9个轴。
    # * /
    def getJointLimit(self, gpId):
        return self.__p.getJointLimit(gpId)

    # / **
    # * @ brief 单轴手动运动
    # * @ param gpId 组号（0..n - 1）
    # * @ param axId 轴号（0~5 为内部轴，6~8 为附加轴）
    # * @ param direc 方向，DirectType枚举类型
    # * @ return 错误码
    # * /
    def startJog(self, gpId, axId, direc):
        return self.__p.startJog(gpId, axId, direc)

    # / **
    # * @ brief 停止手动运动
    # * @ details 注：可停止单轴手动运动、运动定位运动。
    # * @ param gpId 组号（0..n - 1）
    # * @ return 错误码
    # * @ see
    #       startJog
    #       moveTo
    # * /
    def stopJog(self, gpId):
        return self.__p.stopJog(gpId)

    # / **
    # * @ brief 运动定位
    # * @ param gpId 组号（0..n - 1）
    # * @ param point 目标点
    # * @ param isLinear:true - 直线运动, false - 关节运动
    # * @ return 错误码
    # * /
    def moveTo(self, gpId, point, isLinear):
        return self.__p.moveTo(gpId, point, isLinear)

    # / **
    # * @ brief 设置工作坐标系
    # * @ param gpId 组号（0..n - 1）
    # * @ param frame 坐标系
    # * @ return 错误码
    # * /
    def setWorkFrame(self, gpId, frame):
        return self.__p.setWorkFrame(gpId, frame)

    # / **
    # * @ brief 获取工作坐标系
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 坐标系)
    # * 坐标系 :FrameType枚举类型
    # * /
    def getWorkFrame(self, gpId):
        return self.__p.getWorkFrame(gpId)

    # / **
    # * @ brief 获取内部轴数
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 轴数)
    # * /
    def getRobAxisCount(self, gpId):
        return self.__p.getRobAxisCount(gpId)

    # / **
    # * @ brief 获取附加轴数
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 轴数)
    # * /
    def getAuxAxisCount(self, gpId):
        return self.__p.getAuxAxisBegin(gpId)

    # / **
    # * @ brief 获取附加轴起始轴号
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 起始轴号)
    # * /
    def getAuxAxisBegin(self, gpId):
        return self.__p.getAuxAxisBegin(gpId)

    # / **
    # * @ brief 获取关节坐标点数据
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 点数据)
    # 点数据（注：最多6轴数据）
    # * /
    def getJntData(self, gpId):
        return self.__p.getJntData(gpId)

    # / **
    # * @ brief 获取附加轴坐标点数据
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 点数据)
    # * /
    def getAuxData(self, gpId):
        return self.__p.getAuxData(gpId)

    # / **
    # * @ brief 获取笛卡尔坐标点数据
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 点数据)
    # 点数据（注：XYZABC）
    # * /
    def getLocData(self, gpId):
        return self.__p.getLocData(gpId)

    # / **
    # * @ brief 获取形态
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 形态)
    # * /
    def getConfig(self, gpId):
        return self.__p.getConfig(gpId)

    # / **
    # * @ brief 设置工具坐标数据
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 工具坐标索引（0~15）
    # * @ param pos 点数据
    # * /
    def setTool(self, gpId, index, pos):
        return self.__p.setTool(gpId, index, pos)

    # / **
    # * @ brief 获取工具坐标数据
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 工具坐标索引（0~15）
    # * @ return tuple(错误码, 点数据)
    # * /
    def getTool(self, gpId, index):
        return self.__p.getTool(gpId, index)

    # / **
    # * @ brief 设置工件坐标数据
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 工件坐标索引（0~15）
    # * @ param pos 点数据
    # * /
    def setWorkpiece(self, gpId, index, pos):
        return self.__p.setWorkpiece(gpId, index, pos)

    # / **
    # * @ brief 获取工件坐标数据
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 工件坐标索引（0~5）
    # * @ return tuple(错误码, 点数据)
    # * /
    def getWorkpiece(self, gpId, index):
        return self.__p.getWorkpiece(gpId, index)

    # / **
    # * @ brief 设置工具号
    # * @ param gpId 组号（0..n - 1）
    # * @ param num 工具坐标索引（0~15）
    # * /
    def setToolNum(self, gpId, num):
        return self.__p.setToolNum(gpId, num)

    # / **
    # * @ brief 获取工具号
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 工具坐标索引)
    # 工具坐标索引（0~15）
    # * /
    def getToolNum(self, gpId):
        return self.__p.getToolNum(gpId)

    # / **
    # * @ brief 设置工件号
    # * @ param gpId 组号（0..n - 1）
    # * @ param num 工件坐标索引（0~15）
    # * /
    def setWorkpieceNum(self, gpId, num):
        return self.__p.setWorkpieceNum(gpId, num)

    # / **
    # * @ brief 获取工件号
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 工件坐标索引)
    # 工件坐标索引（0~15）
    # * /
    def getWorkpieceNum(self, gpId):
        return self.__p.getWorkpieceNum(gpId)

    # / **
    # * @ brief 获取轴组数据
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 轴组数据)
    # 轴组数据:GroupData结构体类型
    # * /
    def getGroupData(self, gpId):
        return self.__p.getGroupData(gpId)

    # / **
    # * @ brief 设置机型（需重启）
    # * @ param gpId 组号（0..n - 1）
    # * @ param strTypeName 机型名字
    # * /
    def setRobType(self, gpId, strTypeName):
        return self.__p.setRobType(gpId, strTypeName)

    # / **
    # * @ brief 获取可用机型名字
    # * @ return tuple(错误码, 机型名字列表)
    # * /
    def getRobTypeNameList(self):
        return self.__p.getRobTypeNameList()

    # / **
    # * @ brief 获取轴组配置
    # * @ param gpId 组号（0..n - 1）
    # * @ return tuple(错误码, 轴组配置)
    # 轴组配置:GroupConfig结构体类型
    # * /
    def getGroupConfig(self, gpId):
        return self.__p.getGroupConfig(gpId)

    # / **
    # * @ brief 标定
    # * @ param what 标定对象（ < em > "TOOL" < / em > - 工具， < em > "BASE" < / em > - 工件）
    # * @ param gpId 组号（0..n - 1）
    # * @ param num 工具号 / 工件号
    # * @ param type 标定方法编号 （注：参考运动层定义）
    # * @ param strData 标定数据（格式：半角分号分隔的点数据队列，例“{1, 2, }; {3, 4, }; {5, 6, }”）
    # * @ return tuple(错误码, 标定结果)
    # 标定结果:（格式：例“ret = 0x0, data = {7, 8, }”，其中“ret”是标定返回值，“data”是标定结果）
    # * /
    def gpCalibrate(self, what, gpId, num, type, strData):
        return self.__p.gpCalibrate(self, what, gpId, num, type, strData)
