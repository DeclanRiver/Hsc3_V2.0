#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : ProxyMotion.py
# Detail   : 华数III型二次开发接口 - 业务接口 - IO操作代理
#            提供了III型控制器系统功能相关业务接口。

from HSC3Api import Hsc3ApiPy
from HSC3Api import CommApi


class ProxyIO:
    __p = 0

    def __init__(self,pCommApi):
        self.__p = Hsc3ApiPy.ProxyIOPy(pCommApi.getId())

    # / **
    # * @ brief 获取数字输入端口数量
    # * @ return tuple(ret, num)
    # ret 错误码
    # num 数量
    # * /
    def getMaxDinNum(self):
        return self.__p.getMaxDinNum()

    # / **
    # * @ brief 获取数字输出端口数量
    # * @ return tuple(ret, num)
    # ret 错误码
    # num 数量
    # * /
    def getMaxDoutNum(self):
        return self.__p.getMaxDoutNum()

    # / **
    # * @ brief 获取数字输入分组数量
    # * @ details 32 个输入为一组（组0包括输入0~.31、组1包括输入32~63、...）。
    # * @ return tuple(ret, num)
    # ret 错误码
    # num 数量
    # * /
    def getMaxDinGrp(self):
        return self.__p.getMaxDinGrp()

    # / **
    # * @ brief 获取数字输出分组数量
    # * @ details  32 个输出为一组（组0包括输出0~31、组1包括输出32~63、...）。
    # * *@ return tuple(ret, num)
    # ret 错误码
    # num 数量
    # * /
    def getMaxDoutGrp(self):
        return self.__p.getMaxDoutGrp()

    # / **
    # * @ brief 获取数字输入分组值
    # * @ param grpIndex 分组号（0..n - 1）
    # * @ return tuple(ret, num)
    # ret 接口返回错误码
    # num 分组值（32 位无符号整数，最低位代表分组中数字输入0的值，最高位代表数字输入31的值）
    # * /
    def getDinGrp(self, grpIndex):
        return self.__p.getDinGrp(grpIndex)

    # / **
    # * @ brief 获取数字输出分组值
    # * @ param grpIndex 分组号（0..n - 1）
    # * @ return tuple(ret, num)
    # ret 接口返回错误码
    # num 分组值（32 位无符号整数，最低位代表分组中数字输出0的值，最高位代表数字输出31的值）
    # * /
    def getDoutGrp(self, grpIndex):
        return self.__p.getDoutGrp(grpIndex)

    # / **
    # * @ brief 获取数字输入分组状态
    # * @ param grpIndex 分组号（0..n - 1）
    # * @ return tuple(ret, num)
    # ret 接口返回错误码
    # num 分组状态（32 位无符号整数，最低位代表分组中数字输入0的状态，最高位代表数字输入31的状态）
    #              状态：true - 虚拟；false - 真实
    # * @ see setDinMaskBit
    # * /
    def getDinMaskGrp(self, grpIndex):
        return self.__p.getDinMaskGrp(grpIndex)

    # / **
    # * @ brief 获取数字输出分组状态
    # * @ param grpIndex 分组号（0..n - 1）
    # * @ return tuple(ret, num)
    # ret 接口返回错误码
    # num 分组状态（32 位无符号整数，最低位代表分组中数字输出0的状态，最高位代表数字输出31的状态）
    #               状态： true - 虚拟；false - 真实
    # * @ see setDoutMaskBit
    # * /
    def getDoutMaskGrp(self, grpIndex):
        return self.__p.getDoutMaskGrp(grpIndex)

    # / **
    # * @ brief
    # 设置数字输入端口值
    # * @ param portIndex 端口号（0..n - 1）
    # * @ param value 值(bool) True - ON；False - OFF
    # * @ return ret：错误码
    # * @ see getDinGrp
    # * /
    def setDin(self, portIndex, value):
        return self.__p.setDin(portIndex, value)

    # / **
    # * @ brief 设置数字输出端口值
    # * @ param portIndex 端口号（0..n - 1）
    # * @ param value 值(bool) True - ON；False - OFF
    # * @ return ret：错误码
    # * @ see  getDoutGrp
    # * /
    def setDout(self, portIndex, value):
        return self.__p.setDout(portIndex, value)

    # / **
    # * @ brief 设置数字输入状态值
    # * @ details 数字输入状态为“虚拟”时，可通过setDin设置值。 数字输入状态为“真实”时，值从IO模块中读取，通过setDin设置值是无效的。
    # * @ param portIndex 端口号（0..n - 1）
    # * @ param stat 状态(bool)：true - 虚拟； false - 真实
    # * @ return ret：错误码
    # * @ see
    # getDinMaskGrp
    # setDin
    # * /
    def setDinMaskBit(self, portIndex, stat):
        return self.__p.setDinMaskBit(portIndex, stat)

    # / **
    # * @ brief 设置数字输出状态值
    # * @ details  数字输入状态为“虚拟”时，可通过setDout设置值，但不能触发IO模块输出。 数字输入状态为“真实”时，可通过setDout设置值，并可触发IO模块输出。
    # * @ param portIndex 端口号（0..n - 1）
    # * @ param stat 状态：true - 虚拟； false - 真实
    # * @ return ret：错误码
    # * @ see
    # getDoutMaskGrp
    # setDout
    # * /
    def setDoutMaskBit(self, portIndex, stat):
        return self.__p.setDoutMaskBit(portIndex, stat)

    # / **
    # * @ brief 钩模块功能文字式交互
    # * @ details 注：该接口基于复杂的协议，不建议直接使用。
    # * @ param strIntent 交互意图
    # * @ param strMsg 发送信息
    # * @ return tuple(ret, strResponse)
    # ret 接口返回错误码
    # strResponse 控制器回复
    # * /
    def contactOnHook(self, strIntent, strMsg):
        return self.__p.contactOnHook(strIntent, strMsg)
