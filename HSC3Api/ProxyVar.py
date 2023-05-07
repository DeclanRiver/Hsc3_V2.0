#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : ProxyVar.py
# Detail   : 华数III型二次开发接口 - 业务接口 - 变量操作代理
#            提供了III型控制器系统功能相关业务接口。
from HSC3Api import Hsc3ApiPy
from HSC3Api import CommApi


class ProxyVar:

    __p = 0

    def __init__(self, pCommApi):
        self.__p = Hsc3ApiPy.ProxyVarPy(pCommApi.getId())

    # / **
    # * @ brief 保存轴数据
    # * @ param axId 轴号（0..n - 1）
    # * @ param file 数据文件名，选项：
    #                             "para" - 参数
    #                             "home" - 原点相关参数
    #                             "limit" - 软限位相关参数
    # * @ return ret
    # ret 错误码
    # * /
    def saveAx(self, axId, file):
        return self.__p.saveAx(axId, file)

    # / **
    # * @ brief 保存组数据
    # * @ param gpId 组号（0..n - 1）
    # * @ param file 数据文件名，选项：
    #                           "para" - 参数；
    #                           "JR" - JR（关节坐标）寄存器值；
    #                           "LR" - LR（笛卡尔坐标）寄存器值；
    #                           "UT" - UT寄存器值；
    #                           "UF" - UF寄存器值；
    #                           "area" - 区域相关参数
    #                           "track" - 跟踪相关参数
    # * @ return ret
    # ret 错误码
    # * /
    def saveGp(self, gpId, file):
        return self.__p.saveGp(gpId, file)

    # / **
    # * @ brief 保存公共数据
    # * @ param file 数据文件名，选项：
    #                           "R" - R（实数）寄存器值
    # * @ return ret
    # ret 错误码
    # * /
    def saveCommon(self, file):
        return self.__p.saveCommon(file)

    # / **
    # * @ brief 设置R（实数）寄存器值
    # * @ param index 索引
    # * @ param value 值
    # * @ return ret
    # ret 错误码
    # * /
    def setR(self, index, value):
        return self.__p.setR(index, value)

    # / **
    # * @ brief 获取R（实数）寄存器值
    # * @ param index 索引
    # * @ param num 获取寄存器的数量
    # * @ return tuple(ret, value)
    # ret 错误码
    # value 值，num == 1 时, value 是 numbers
    #           num != 1 时, value 是 存放从 index 开始,连续的 num 个R寄存器的值 的 list
    # * /
    def getR(self, index, num=1):
        if len == 1:
            return self.__p.getR(index)
        else:
            return self.__p.getR(index, num)

    # / **
    # * @ brief 设置JR（关节坐标）寄存器值
    # * @ param gpId 组号（0..n - 1）
    # * @ param index  索引
    # * @ param data 值 （JntPos类型的对象）
    # * @ return ret
    # ret 错误码
    # * /
    def setJR(self, gpId, index, data):
        return self.__p.setJR(gpId, index, data)

    # / **
    # * @ brief 获取JR（关节坐标）寄存器值
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 索引
    # * @ param num 数量
    # * @ return tuple(ret, Data)
    # ret 错误码
    # Data 值, num == 1 时, Data 是 JntPos 对象
    #          num != 1 时, Data 是 存放从 index 开始,连续的 num 个JR寄存器的 JntPos 数据对象的 list
    # * /
    def getJR(self, gpId, index, num=1):
        if num == 1:
            return self.__p.getJR(gpId, index)
        else:
            return self.__p.getJR(gpId, index, num)

    # / **
    # * @ brief 设置LR（笛卡尔坐标）寄存器值
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 索引
    # * @ param data 值 (LocPos对象)
    # * @ return ret
    # ret 错误码
    # * /
    def setLR(self, gpId, index, data):
        return self.__p.setLR(gpId, index, data)

    # / **
    # * @ brief 获取LR（笛卡尔坐标）寄存器值
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 索引
    # * @ param num 数量
    # * @ return tuple(ret, Data)
    # ret 错误码
    # Data 值，num == 1 时, Data 是 LocPos 对象
    #          num != 1 时, Data 是 存放从 index 开始,连续的 num 个LR寄存器的 LocPos 数据对象的 list
    # * /
    def getLR(self, gpId, index, num=1):
        if num == 1:
            return self.__p.getLR(gpId, index)
        else:
            return self.__p.getLR(gpId, index, num)

    # / **
    # * @ brief 配置区域
    # * @ param gpId 组号（0..n - 1）
    # * @ param  index 索引
    # * @ param data 值 （AreaConfigData 对象）
    # * @ return ret
    # ret 错误码
    # * /
    def configArea(self, gpId, index, data):
        return self.__p.configArea(gpId, index, data)

    # / **
    # * @ brief 获取区域类型
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 索引
    # * @ return tuple（ret, type)
    # type 区域类型，index == -1 时, type 是 存放所有区域类型值（AreaType 枚举值） 的 lists。
    #                index != -1 时, type 是 index 指定的区域的类型值（AreaType 枚举值）
    # * /
    def getAreaType(self, gpId, index=-1):
        if index == -1:
            return self.__p.getAreaType(gpId)
        else:
            return self.__p.getAreaType(gpId, index)

    # / **
    # * @ brief 使能共享区
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 索引
    # * @ param en 是否使能
    # * @ return ret
    # ret 错误码
    # * /
    def setShareAreaEn(self, gpId, index, en):
        return self.__p.setShareAreaEn(gpId, index, en)

    # / **
    # * @ brief 获取共享区使能
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 索引
    # * @ return tuple(ret, en)
    # ret 错误码
    # en 是否使能，index == -1 时，en 是 存放所有区域的共享区使能状态（bool值）的 list。
    #              index != -1 时，en 是 index 指定区域的共享区使能状态（bool 值）
    # * /
    def getShareAreaEn(self, gpId, index=-1):
        if index == -1:
            return self.__p.getShareAreaEn(gpId)
        else:
            return self.__p.getShareAreaEn(gpId, index)

    # / **
    # * @ brief 获取区域输出
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 索引
    # * @ return tuple(ret, en)
    # ret 错误码
    # en 是否输出，index == -1 时，en 是 存放所有区域的输出状态（bool值）的 list。
    #              index != -1 时，en 是 index 指定区域的输出状态（bool 值）
    def getAreaOut(self, gpId, index=-1):
        if index == -1:
            return self.__p.getAreaOut(gpId)
        else:
            return self.__p.getAreaOut(gpId, index)

    # / **
    # * @ brief 获取区域配置
    # * @ param gpId 组号（0..n - 1）
    # * @ param index 索引
    # * @ return tuple(ret, data)
    # ret 错误码
    # data 值,AreaConfigData 结构体对象
    # * /
    def getAreaConfig(self, gpId, index):
        return self.__p.getAreaConfig(gpId, index)

