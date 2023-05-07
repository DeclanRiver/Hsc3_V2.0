#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : ProxyMotion.py
# Detail   : 华数III型二次开发接口 - 业务接口 - 采集功能代理
#            提供了III型控制器采集功能相关业务接口。
from HSC3Api import Hsc3ApiPy
from HSC3Api import CommApi


class ProxyCollect:
    __p = 0

    def __init__(self, pCommApi):
        self.__p = Hsc3ApiPy.ProxyCollectPy(pCommApi.getId())

    # /**
    # * @brief   添加采集任务
    # * @details 一个采集任务包含若干采集变量（参考华数III型控制器可采集变量列表），采样周期为k*T，其中k为倍数，T为基础周期4ms。
    # 注：不能重复添加同一ID的采集任务。
    # * @param   tid         采集任务ID
    # * @param   iSampleKT   采样周期倍数K（≥1）
    # * @param   strVarList  采集变量名列表（格式：半角逗号分隔的名字列表，例“var.axis[0].pfb,var.axis[1].pfb,”）
    # * @see     delTask
    # */s
    def addTask(self, tid, iSampleKT, strVarList):
        return self.__p.addTask(tid, iSampleKT, strVarList)

    # /**
    # * @brief   删除采集任务
    # * @param   tid         采集任务ID
    # * @see     addTask
    # */
    def delTask(self, tid):
        return self.__p.delTask(tid)

    # / **
    # * @ brief 启动采集任务
    # * @ details 采集数据通过UDP返回（参考采集数据封装协议）。
    # * @param tid 采集任务ID,tid == None时, 开始所有采集任务,
    #                         tid != None时, tid 应该是32位 Number，开始对应id的采集任务
    # * @ see
    #   CommApi::getUdpMsg
    #   stop
    # * /
    def start(self, tid=None):
        if tid == None:
            return self.__p.start()
        else:
            return self.__p.start(tid)

    # /**
    # * @brief   停止采集任务
    # * @param tid   采集任务ID, tid == None时,停止所有采集任务
    #                            tid != None时, 则停止对应id的采集任务
    #
    # * @see     start
    # */
    def stop(self, tid=None):
        if tid == None:
            return self.__p.stop()
        else:
            return self.__p.stop(tid)

    # /**
    # * @brief   获取存在的采集任务列表
    # * @return tuple(ret, listTask)
    # ret  错误码
    # listTask 采集任务ID列表
    # */
    def getExistTasks(self):
        return self.__p.getExistTasks()

    # / **
    # * @ brief 获取正在运行的采集任务列表
    # * @ return tuple(ret, listTask)
    # ret 错误码
    # listTask 采集任务ID列表
    # * /
    def getRunningTasks(self):
        return self.__p.getRunningTasks()

    # /**
    # * @brief   获取控制系统当前时间戳
    # * @details 建议启动采集任务前先获取控制系统的当前时间戳，通过采集数据中的时间戳与之相减的差值，可换算出距离采集启动的时间。
    # * @return tuple(ret, timestamp)
    # ret 错误码
    # timestamp       时间戳
    # */
    def getCurTimestamp(self):
        return self.__p.getCurTimestamp()
