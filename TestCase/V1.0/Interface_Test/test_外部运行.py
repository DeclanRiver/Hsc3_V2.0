
"""
@Time : 2023/03/09
@author 系统部李汉鼎
@Content test_外部运行.py
"""

import sys
import time
sys.path.append("HSC3Api")
from HSC3Api import ProxyMotion
from HSC3Api import ProxyVar
from HSC3Api import CommApi
from HSC3Api import ProxyVm
from HSC3Api import ProxyIO
from HSC3Api import ProxySys
from HSC3Api import Hsc3ApiPy
import pytest
from Lib import 工具库_hd
from Lib import FTP

lib = 工具库_hd
comm = CommApi.CommApi("..\\log\\test")
proMot = ProxyMotion.ProxyMotion(comm)  # 构造ProxyMotion对象
pVm = ProxyVm.ProxyVm(comm)  # 构造ProxyVm对象
proVar = ProxyVar.ProxyVar(comm)  # 构造ProVar对象
proSys = ProxySys.ProxySys(comm)  # 构造ProSys对象
proIO = ProxyIO.ProxyIO(comm)  # 构造ProIO对象

# 连接系统
# lib.连接系统("10.10.56.214")
i = 0
while not comm.isConnected():
    comm.connect("10.10.56.214", 23234)
    # comm.connect("10.10.57.213", 23234)
    time.sleep(1)
    if comm.isConnected():
        print("连接成功！！！")
    elif not comm.isConnected():
        print("第", i + 1, "次连接失败，重连中...")
        i += 1


# 模式切换自动化测试
# 模式切换成功正确性
# 模式切换成功后输出IO的正确性
# 自动、外部模式下外部运行配置的输入信号控制程序正确性、输出信号正确性

@pytest.mark.repeat(120)
def test_模式切换():
    """

    :return:
    """
    time.sleep(0.1)
    opm = [Hsc3ApiPy.OpMode.OP_EXT, Hsc3ApiPy.OpMode.OP_AUT, Hsc3ApiPy.OpMode.OP_T2, Hsc3ApiPy.OpMode.OP_T1]

    j = 3
    # 切换配置文件
    # 上传文件
    f = FTP.MyFtp("10.10.56.214")
    r = f.login('root', '111111')
    r.upload_file(remove_path='/usr/codesys/data', local_path='..\\SysData\\系统配置文件', prg='hsc3_hook.config')
    r.upload_file(remove_path='/usr/codesys/data', local_path='..\\SysData\\系统配置文件', prg='_system.data')
    r.upload_file(remove_path='/usr/codesys/hsc3_app/script', local_path='..\\SysData\\系统配置文件', prg='TEST_RUN.PRG')
    r.upload_file(remove_path='/usr/codesys/hsc3_app/script', local_path='..\\SysData\\系统配置文件', prg='TEST_FALSE.PRG')
    r.upload_file(remove_path='/usr/codesys/hsc3_app/script', local_path='..\\SysData\\系统配置文件', prg='hsc3_c_ext.config')
    print("上传配置文件成功")
    f.close()
    time.sleep(1)
    # 重启系统、等待就绪、文件生效
    lib.等待就绪()
    lib.IO虚拟()

    # 以当前位置为校准数据
    proMot.setHomePosition(0, proMot.getJntData(0)[1], 63)
    time.sleep(1)
    # 切换模式\判断IO
    while j + 1:
        proMot.setOpMode(opMode=opm[j])
        time.sleep(1)
        lib.自定义断言(proMot.getOpMode()[1], opm[j], 1)
        # 模式切换成功，通过二次开发接口和外部信号控制程序状态，并检测是否正常
        # 空闲+零点位置
        lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[3], True)

        lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[12], True)
        # 手动模式  T1    T2
        if proMot.getOpMode()[1] == opm[2] or proMot.getOpMode()[1] == opm[3]:
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[9], True)
            proMot.setGpEn(0, True)
            time.sleep(1)
            # 使能信号
            lib.自定义断言(proMot.getGpEn(0)[1], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[2], True)
            # 加载程序
            pVm.load('/usr/codesys/hsc3_app/script/', 'TEST_RUN.PRG')
            time.sleep(2)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[0], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[2], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[4], True)
            # 运行状态
            pVm.start('TEST_RUN.PRG')
            time.sleep(0.2)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[5], True)
            pVm.pause('TEST_RUN.PRG')
            time.sleep(0.2)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[7], True)
            pVm.stop('TEST_RUN.PRG')
            time.sleep(0.2)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[0], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[2], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[4], True)
            pVm.unload('TEST_RUN.PRG')
            time.sleep(0.2)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[3], True)
            # 加载语法错误程序
            pVm.load('/usr/codesys/hsc3_app/script/', 'TEST_FALSE.PRG')
            time.sleep(3)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[1], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[3], True)
            proSys.reset()
            time.sleep(0.1)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[1], False)
        elif proMot.getOpMode()[1] == opm[1] or proMot.getOpMode()[1] == opm[0]:
            proVar.setR(100, 1)
            if proMot.getOpMode()[1] == opm[1]:
                lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[10], True)
                # 加载程序→准备状态
                pVm.load('/usr/codesys/hsc3_app/script/', 'TEST_RUN.PRG')
                time.sleep(2)
                lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[0], True)
                lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[2], True)
                lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[4], True)
            elif proMot.getOpMode()[1] == opm[0]:
                # 加载程序→准备状态
                lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[11], True)
                proIO.setDin(3, True)
                time.sleep(0.1)
                proIO.setDin(3, False)
                time.sleep(1)
                lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[4], True)

            # 使能
            proIO.setDin(5, False)
            time.sleep(0.1)
            proIO.setDin(5, True)
            time.sleep(1)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[0], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[2], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[4], True)
            # 运行状态
            proIO.setDin(0, False)
            time.sleep(0.1)
            proIO.setDin(0, True)
            time.sleep(0.1)
            proIO.setDin(0, False)
            time.sleep(1)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[5], True)
            # 安全速度
            a = proMot.getJogVord()
            proIO.setDin(8, True)
            time.sleep(0.1)
            proIO.setDin(8, False)
            time.sleep(0.5)
            lib.自定义断言(proMot.getVord()[1], 10)
            proIO.setDin(8, True)
            time.sleep(0.5)
            lib.自定义断言(proMot.getVord()[1], a[1])
            proIO.setDin(1, False)
            time.sleep(0.1)
            proIO.setDin(1, True)
            time.sleep(0.1)
            proIO.setDin(1, False)
            time.sleep(0.3)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[7], True)
            proIO.setDin(2, False)
            time.sleep(0.1)
            proIO.setDin(2, True)
            time.sleep(0.1)
            proIO.setDin(2, False)
            time.sleep(0.3)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[0], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[2], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[4], True)
            # 停止
            proIO.setDin(2, False)
            time.sleep(0.1)
            proIO.setDin(2, True)
            time.sleep(0.1)
            proIO.setDin(2, False)
            time.sleep(0.2)
            # 卸载
            proIO.setDin(4, False)
            time.sleep(0.1)
            proIO.setDin(4, True)
            time.sleep(0.1)
            proIO.setDin(4, False)
            time.sleep(0.5)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[3], True)
            # 加载语法错误程序
            proVar.setR(100, 0)
            time.sleep(0.1)
            if proMot.getOpMode()[1] == opm[0]:
                proIO.setDin(3, False)
                time.sleep(0.2)
                proIO.setDin(3, True)
                time.sleep(0.2)
                proIO.setDin(3, False)
                time.sleep(2)
            elif proMot.getOpMode()[1] == opm[1]:
                pVm.load('/usr/codesys/hsc3_app/script/', 'TEST_FALSE.PRG')
                time.sleep(2)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[1], True)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[3], True)
            proIO.setDin(6, False)
            time.sleep(0.2)
            proIO.setDin(6, True)
            time.sleep(0.5)
            proIO.setDin(6, False)
            time.sleep(1)
            lib.自定义断言(lib.decToBin(proIO.getDoutGrp(0)[1])[1], False)
        j -= 1


if __name__ == '__main__':
    pytest.main(["-v", "-s", __file__])
