# -*- coding:utf-8 _*_
"""
@Time : 2023/03/14
@author 系统部郭松江
@Content est_demo.py 公共前后置配置五年级
"""
import pytest
from time import *
from Lib.FTP import MyFtp
import sys
from HSC3Api import CommApi,ProxyCollect,ProxyVm,Hsc3ApiPy,ProxyMotion,ProxyVar,ProxySys,ProxyIO

# comm = CommApi.CommApi("")
# proMot = ProxyMotion.ProxyMotion(comm)  # 构造ProxyMotion对象
# pVm = ProxyVm.ProxyVm(comm)  # 构造ProxyVm对象
# proVar = ProxyVar.ProxyVar(comm)  # 构造ProVar对象
# proIO = ProxyIO.ProxyIO(comm)  # 构造ProIO对象
# comm.connect("10.10.56.214", 23234)
# sleep(1)

#包级别前后置方法，总的测试数据上传（自动执行）
@pytest.fixture(scope="package",autouse=True)
def ftp文件传输fixture():
    print("\033[1;31m [包级别前置]：连接，测试数据文件上传\033[0m")
    # IP = '10.10.56.214'
    # user = 'root'
    # password = '111111'
    # ftp_path = '/usr/codesys/hsc3_app/script'
    # local_path = 'D:/SVN/File/测试/III型自动化测试/AutoProject/2023/Hsc3_AutoTest2023/SysData/OrderSet'
    # if pVm.mainProgNames()[1]:
    #     print('当前已有程序加载', pVm.mainProgNames()[1])
    #     sys.exit(0)
    # f = MyFtp(IP)
    # f.login(user, password)
    # f.udl_dir(ftp_path, local_path, 0)
    # sleep(5)
    print("\033[1;31m [包级别后置]：断开Ftp连接\033[0m")
    yield
    # f.close()

#模块级别前后置方法-检测系统状态是否异常，进行异常恢复(自动执行)
@pytest.fixture(scope="module",autouse=True)
def 系统状态监测fixture():
    print("\033[1;32m 模块级前置方法\033[0m")
    # #系统就绪状态监测
    # if (comm.execCmd("sys.isReady()",1)[1])!= "true":
    #     comm.execCmd("lib.reboot()", 1)
    #     sleep(40)
    #     comm.connect("10.10.56.214", 23234)
    #     sleep(1)
    #     print("\033[1;33m 系统异常了！！！，无法就绪，启动重启机制,重启完成~\033[0m")
    # yield
    print("\033[1;32m 模块级后置方法\033[0m")

# @pytest.fixture(scope="class",autouse=False)
# def 系统状态判断fixture():
#     print("\033[1;33m 类级前置方法\033[0m")
#     yield
#     print("\033[1;33m 类级前置方法\033[0m")

# @pytest.fixture(scope="function",autouse=True)
# def myfixture():
#     print("\033[1;31m 测试\033[0m")
#     if comm.execCmd("sys.hasError()",1)==1
#     sys.hasError()
#     #程序语法错误 / 程序运动过程中掉使能 / 关节目标点不可达为1,正常为0
#
#     yield
#     print("\033[1;31m 测试\033[0m")

#——————————————————————————————————————————————————————分割线——————————————————————————————————————————————————————————————————————————————————————————————————————————---
#自定义前后置方法-IO复位置OFF（需使用，调用即可）
# @pytest.fixture(scope="function",name="IO复位",ids="gsj")
# def Io():
#     comm.connect("10.10.56.214", 23234)
#     sleep(1)
#     print("前置：IO初始化")
#     for num in range(512):
#         proIO.setDin(num, False)
#         proIO.setDout(num, False)
#     sleep(0.5)
#     for num in range(16):
#         assert proIO.getDinGrp(num) == (0, 0),"复位输入DI信号为OFF失败"
#         assert proIO.getDoutGrp(num) == (0, 0),"复位输入DO信号为OFF失败"
#     yield
#     print("后置：IO复位")
#     for num in range(512):
#         proIO.setDin(num, False)
#         proIO.setDout(num, False)
#     sleep(0.5)
#     for num in range(16):
#         assert proIO.getDinGrp(num) == (0, 0),"复位输入DI信号为OFF失败"
#         assert proIO.getDoutGrp(num) == (0, 0),"复位输入DO信号为OFF失败"

#自定义前后置方法-寄存器复位（需使用，调用即可）
# @pytest.fixture(scope="function",name="寄存器复位[R,JR,LR]",ids="gsj")
# def 寄存器():
#     print("前置：寄存器初始化")
#     # 设置 R、JR、LR 寄存器
#     for num in range(1000):
#         proVar.setR(num, 0)
#         jPos = Hsc3ApiPy.JntPos()
#         jPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#         proVar.setJR(0, num, jPos)
#         lPos = Hsc3ApiPy.LocPos()
#         lPos.ufNum = 0
#         lPos.utNum = 0
#         lPos.config = 0
#         lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#         proVar.setLR(0, num, lPos)
#     sleep(0.5)
#     for num in range(1000):
#         assert proVar.getR(num)[1] == [0], "R寄存器初始化失败"
#         assert proVar.getJR(0, num)[1].vecPos == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "JR寄存器初始化失败"
#         assert proVar.getLR(0, num)[1].vecPos == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "LR寄存器初始化失败"
#     yield
#     print("后置：寄存器初始化")
#     # 设置 R、JR、LR 寄存器
#     for num in range(1000):
#         proVar.setR(num, 0)
#         jPos = Hsc3ApiPy.JntPos()
#         jPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#         proVar.setJR(0, num, jPos)
#         lPos = Hsc3ApiPy.LocPos()
#         lPos.ufNum = 0
#         lPos.utNum = 0
#         lPos.config = 0
#         lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#         proVar.setLR(0, num, lPos)
#     sleep(0.5)
#     for num in range(1000):
#         assert proVar.getR(num)[1] == [0], "R寄存器初始化失败"
#         assert proVar.getJR(0, num)[1].vecPos == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "JR寄存器初始化失败"
#         assert proVar.getLR(0, num)[1].vecPos == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "LR寄存器初始化失败"
