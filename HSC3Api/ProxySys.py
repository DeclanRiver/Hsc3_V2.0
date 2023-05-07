#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : ProxyMotion.py
# Detail   : 华数III型二次开发接口 - 业务接口 - 系统功能代理
#            提供了III型控制器系统功能相关业务接口。
from HSC3Api import Hsc3ApiPy
from HSC3Api import CommApi


class ProxySys:
    __p = 0

    def __init__(self, pCommApi):
        self.__p = Hsc3ApiPy.ProxySysPy(pCommApi.getId())

    # / **
    # * @ brief 系统复位
    # * /
    def reset(self):
        return self.__p.reset()

    # / **
    # * @ brief 查询报警详情
    # * @ param errCode 错误码
    # * @ return tuple(接口返回错误码, 错误原因, 排除措施)
    # * /
    def queryError(self, errCode):
        return self.__p.queryError(errCode)

    # / **
    # * @ brief 系统是否就绪
    # * @ return tuple(错误码, ok)
    # ok 已 / 未就绪
    # * /
    def isReady(self):
        return self.__p.isReady()

    # / **
    # * @ brief 获取系统报警
    # * @ details 使用该接口会阻塞调用线程，直至获取到信息 / 等待超时。
    # * @ param ulWaitTime 等待时间（单位：ms）
    # * @ return tuple(ret, level, code, strMsg)
    # * @ ret 接口返回错误码 : 0x0 - 获取到合法信息（但不排除strMsg为空）；
    #              KM_ERR_INVALID_MESSAGE- 获取到信息但信息无效；
    #              KM_ERR_NO_MESSAGE - 未收到信息（等待超时）
    # * @ level 报警级别
    # * @ code 报警错误码
    # * @ strMsg 信息内容
    # * /
    def getMessage(self, ulWaitTime):
        return self.__p.getMessage(ulWaitTime)

    # / **
    # * @ brief  获取版本信息
    # * @ param key 键
    #            "Release" - 控制器发布版本；
    #            "CL"  - 控制器业务层；
    #            "ML" - 控制器运动层；
    #            "Api" - 二次开发接口
    # * @ return tuple(ret, value)
    # ret 接口返回错误码
    # value 版本信息
    # * /
    def getVersion(self, key):
        return self.__p.getVersion(key)

    # / **
    # * @ brief 系统关机
    # * /
    def shutdown(self):
        return self.__p.shutdown()

    # / **
    # * @ brief 系统重启
    # * /
    def reboot(self):
        return self.__p.reboot()

    # / **
    # * @ brief 设置语言
    # * @ param strLang 语言名
    # * /
    def setLang(self, strLang):
        return self.__p.setLang(strLang)

