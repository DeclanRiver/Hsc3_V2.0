#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : CommApi.py
# Detail   : 通信客户端  提供接口包含：通信连接配置、连接控制、数据操作等。

from HSC3Api import Hsc3ApiPy


class CommApi:
    __p = 0

    def __init__(self, logPath):
        self.__p = Hsc3ApiPy.CommApiPy(logPath)

    def getId(self):
        return self.__p.getId()

    # / **
    # * @ brief    获取版本信息
    # * @ return   版本信息字符串
    # * /
    def getVersionStr(self):
        return self.__p.getVersionStr()

    # / **
    # * @ brief 配置自动重连功能
    # * @ details 自动重连模式：使用NetConnect接口触发自动重连，客户端在通信断开后可再次连接，直到使用NetExit接口停止自动重连。
    # *           非自动重连模式：使用NetConnect接口进行连接，客户端在通信断开后不会重连，除非再次调用NetConnect接口。
    # *注：CommApi构造时默认为自动重连模式。建议在调用NetConnect接口前进行配置。
    # * @ param en 是否启用
    # * /
    def setAutoConn(self, en):
        return self.__p.setAutoConn(en)

    # / **
    # * @ brief 配置UDP功能
    # * @ details 若启用UDP功能，在TCP通信已连接后，将尝试UDP通信连接。
    # *注：CommApi构造时默认不启用UDP功能。建议在调用NetConnect接口前进行配置。
    # * @ param en 是否启用,1-启用，0-不启用
    # * /
    def setUseUdp(self, en):
        return self.__p.setUseUdp(en)


    # / **
    # * @ brief    查询是否已连接
    # * @ details  注：返回值仅表示TCP通信连接的状态，与UDP / FTP无关。
    # * @ return   返回 true  - 已连接
    # *                 false - 未连接
    # * /
    def isConnected(self):
        return self.__p.isConnected()

    # / **
    # * @ brief 连接
    # * @ details 自动重连模式：使用该接口返回0x0表示成功触发自动重连功能（不能多次触发），不代表通信已连接。
    # *           非自动重连模式：使用该接口会阻塞调用线程，直至连接成功 / 超时（约3s）失败 / 其它原因导致的失败。
    # * @ param strIp IP
    # * @ param uPort 端口
    # * @ return 错误码（0x0 命令发送成功），
    # * @ see setAutoConn
    # * /
    def connect(self, ip, port):
        return self.__p.connect(ip, port)

    # / **
    # * @ brief 断开连接
    # * @ details 注：自动重连模式下使用该接口，还会停止自动重连功能。
    # * @ return 错误码（0x0 成功）
    # * @ see setAutoConn
    # * /
    def disconnect(self):
        return self.__p.disconnect()

    # / **
    # * @ brief 执行命令
    # * @ details 注：使用该接口会阻塞调用线程，直至成功 / 超时（约8s）失败 / 其它原因导致的失败。
    # * @ param strCmd 命令内容（参考华数III型控制器业务层接口协议文档填写命令）
    # * @ param priority 优先级（值越小，优先级越高；建议使用CmdPriority枚举类型）
    # * @ return param[out] strRet 返回信息
    # * @ return 错误码（0x0 成功）
    # * /
    def execCmd(self, cmd, priority):
        return self.__p.execCmd(cmd, priority)

    # / **
    # * @ brief 获取异步信息
    # * @ details 异步信息是控制器主动发送到客户端的信息。注：获取到信息后，客户端内部不会再保留该信息。
    # * @ return tuple(错误码,返回信息)
    # *错误码（0x0成功，总是返回0x0)
    # *(返回信息（无信息时返回空串）
    # * /
    def getAsyncMsg(self):
        return self.__p.getAsyncMsg()

    # / **
    # * @ brief 清空异步信息
    # * @ details 清空客户端内部所有的异步信息。
    # * 注：获取到信息后，客户端内部不会再保留该信息。
    # * @ return 错误码（0x0 成功，总是返回0x0）
    # * /
    def clearAsyncMsg(self):
        return self.__p.clearAsyncMsg()

    # / **
    # * @ brief 获取UDP信息
    # * @ details UDP信息是控制器通过UDP通信主动发送到客户端的信息。注：获取到信息后，客户端内部不会再保留该信息。
    # * @ return tuple(错误码,返回信息)
    # 错误码（0x0 # 成功，总是返回0x0）
    # strMsg 返回信息（无信息时返回空串）
    # * @ see
    # setUseUdp
    # * /
    def getUdpMsg(self):
        return self.__p.getUdpMsg()

    # / **
    # * @ brief 获取UDP对话ID
    # * @ details
    # 注：配置启动UDP功能，TCP通信连接约3s后，待UDP通信已连接，方可获取到正常ID。
    # * @ return tuple(错误码, 对话ID)
    # * 错误码（0x0 成功）
    # * 对话ID（正常为大于0的整数，-1 表示不存在UDP通信）
    # * @ see
    # setUseUdp
    # * /
    def getUdpSessionId(self):
        return self.__p.getUdpSessionId()

    # / **
    # * @ brief 清空缓存的UDP信息
    # * @ details 清空客户端内部所有的UDP信息。
    # * @ return 错误码（0x0 成功，总是返回0x0）
    # * @ see
    # setUseUdp
    # * /
    def clearUdpMsg(self):
        return self.__p.clearUdpMsg()

    # / **
    # * @ brief 下载文件
    # * @ param strLocalName 本地文件路径名字
    # * @ param strSrcName 源（服务器）文件路径名字
    # * @ return 错误码（0x0 成功）
    # * /
    def getFile(self, strLocalName, strSrcName):
        return self.__p.getFile(strLocalName, strSrcName)

    # / **
    # * @ brief 上传文件
    # * @ param  strDstName 目标（服务器）文件路径名字
    # * @ param strLocalName 本地文件路径名字
    # * @ return 错误码（0x0  成功）
    # * /
    def putFile(self, strDstName, strLocalName):
        return self.__p.getFile(strDstName, strLocalName)

    # / **
    # * @ brief 删除文件
    # * @ param strPath（服务器）文件路径名字
    # * @ return 错误码（0x0  成功）
    # * /
    def delFile(self, strPath):
        return self.__p.delFile(strPath)

    # / **
    # * @ brief 删除目录
    # * @ details
    # 注：若目录非空，删除操作将失败，可使用fileListInfo接口检查目录列表信息。
    # * @ param strPath（服务器）目录名字
    # * @ return 错误码（0x0 成功）
    # * @ see
    # fileListInfo
    # * /
    def delDir(self, strPath):
        return self.__p.delDir(strPath)

    # / **
    # * @ brief 创建目录
    # * @ param strPath（服务器）目录名字
    # * @ return 错误码（0x0  成功）
    # * /
    def mkDir(self, strPath):
        return self.__p.mkDir(strPath)

    # / **
    # * @ brief  获取目录列表信息
    # * @ param strDirPath  （服务器）目录名字
    # * @ return tuple(错误码,目录列表信息)
    # * @  错误码（0x0 成功）
    # * @  目录列表信息
    # * /
    def getFileListInfo(self,strDirPath):
        return self.__p.getFileListInfo(strDirPath)
