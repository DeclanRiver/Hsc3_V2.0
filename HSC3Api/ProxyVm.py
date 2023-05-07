#!/usr/bin/python
# -*- coding: utf-8 -*-
# fileName :ProxyVm.h
# details  :程序运行代理
#           提供了III型控制器程序运行相关业务接口。

from HSC3Api import Hsc3ApiPy
from HSC3Api import CommApi


class ProxyVm:
    __p = 0

    def __init__(self, pCommApi):
        self.__p = Hsc3ApiPy.ProxyVmPy(pCommApi.getId())

    # / **
    # * @ brief    加载程序
    # * @ param    path  路径（不包含文件名）
    # * @ param    fileName  主程序文件名
    # * /
    def load(self, Path, fileName):
        return self.__p.load(Path, fileName)

    # / **
    # * @ brief 启动运行
    # * @ param fileName 主程序文件名
    # * /
    def start(self, fileName):
        return self.__p.start(fileName)

    # / **
    # * @ brief 暂停运行
    # * @ param fileName 主程序文件名
    # * /
    def pause(self,fileNames):
        return self.__p.pause(fileNames)

    # / **
    # * @ brief 停止运行
    # * @ param fileName 主程序文件名
    # * /
    def stop(self,fileName):
        return self.__p.stop(fileName)

    # / **
    # * @ brief 单步运行
    # * @ param fileName 主程序文件名
    # * /
    def step(self,fileName):
        return self.__p.step(fileName)

    # / **
    # * @ brief 卸载程序
    # * @ param fileName 主程序文件名
    # * /
    def unload(self,fileNmae):
        return self.__p.unload(fileNmae)

    # / **
    # * @ brief 获取自动运行状态
    # * @ param fileName 主程序文件名
    # * @ param[out] state 状态
    # * /
    def progState(self, fileName):
        return self.__p.progState(fileName)

    # / **
    # * @ brief 设置单步模式
    # * @ param fileName 主程序文件名
    # * @ param en 是否单步
    # * /
    def setStepMode(self, fileName, en):
        return self.__p.setStepMode(fileName, en)

    # / **
    # * @ brief 获取运行行号
    # * @ param fileName 主程序文件名
    # * @ return tuple(错误码,行号)
    # * /
    def getCurLineNo(self, fileName):
        return self.__p.getCurLineNo(fileName)

    # / **
    # * @ brief 获取当前运行程序名
    # * @ param fileName 主程序文件名
    # * @ return tuple(错误码, 程序名)
    # * /
    def getCurProgName(self, fileName, progName):
        return self.__p.getCurProgName(fileName, progName)

    # / **
    # * @ brief 获取已加载的主程序名列表
    # * @ return tuple(错误码，主程序名列表)
    # 主程序名列表（格式：中括号扩起、半角逗号分隔的字符串队列，例“[abc.prg, def .prg ]”）
    # * /
    def mainProgNames(self):
        return self.__p.mainProgNames()

    # / **
    # * @ brief  获取运行程序信息
    # * @ param fileName 主程序文件名
    # * @ return tuple(错误码, 运行程序信息)
    # * @ 错误码
    # * @ 运行程序信息
    # * /
    def getProgInfo(self, fileName):
        return self.__p.getProgInfo(fileName)







