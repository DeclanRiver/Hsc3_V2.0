#!/usr/bin/python
# -*- coding: utf-8 -*-
# import sys
# sys.path.append(r"D:\workplace\Hsc3Api\build\win_python\Debug")
# fileName CommApiTest.Py
import uiautomator2 as u2
import time
from HSC3Api import CommApi


#连接
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
# 连接
#
# def connectIPC(cmApi,strIP,uPurt):
#     cmApi.setAutoCom(1)
#     cmApi.connect(strIP,uPurt)
#     time.sleep(1)
#     if cmApi.isConnected():
#         return 1
#     else:
#         return 0
# comm = CommApi.CommApi("..\\log\\test")

if connectIPC(comm, "10.10.56.214", 23234):
    # 获取控制器中的PRG程序文件
    ret, listFileInfo = comm.getFileListInfo("/usr/codesys/hsc3_app/script/")
    for listNum in listFileInfo:
        print(listNum.strName)
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

# if connectIPC(comm,"10.10.56.214",23234):
#     ret  listFileInfo = comm.getFileListInfo("/usr/codesys/hsc3_app/script/")
#     for listNum in listFileInfo:
#         print(listNum.strName)
#     while(1):
#         cmd = input("请输入：")
#         if cmd ==  'q':
#             break
#         ret = comm.execCmd(cmd,3)
#         print(ret)
#
# comm.disconnect();
# print('退出')