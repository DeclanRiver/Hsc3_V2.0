# !usr/bin/env python3
# encoding=utf-8
"""
@author:少华
"""
import time
from HSC3Api import CommApi
from HSC3Api import ProxyVm
from HSC3Api import ProxyMotion
from HSC3Api import ProxyIO
from HSC3Api import Hsc3ApiPy
from HSC3Api import ProxyVar
comm = CommApi.CommApi('')
pvm = ProxyVm.ProxyVm(comm)
pMot = ProxyMotion.ProxyMotion(comm)
pio = ProxyIO.ProxyIO(comm)
pvr = ProxyVar.ProxyVar(comm)
comm.connect('10.10.56.214', 23234)
time.sleep(1)
assert comm.isConnected()


class Test_for:
    def test_冒烟01(self, prg='OrderSet/循环指令/FOR1.PRG'):
        """
        FOR循环一个比较大的值（一亿），0到正整数
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(10, 0)
        time.sleep(0.5)
        assert pvr.getR(10, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(10, 1)[1][0] == 100000001  # 验证循环次数

    def test_冒烟02(self, prg='OrderSet/循环指令/FOR2.PRG'):
        """
        FOR循环:正整数到正整数
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(11, 0)
        time.sleep(0.5)
        assert pvr.getR(11, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(11, 1)[1][0] == 10  # 验证循环次数

    def test_冒烟03(self, prg='OrderSet/循环指令/FOR3.PRG'):
        """
        FOR循环:负整数到0
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(12, 0)
        time.sleep(0.5)
        assert pvr.getR(12, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(12, 1)[1][0] == 20  # 验证循环次数

    def test_冒烟04(self, prg='OrderSet/循环指令/FOR4.PRG'):
        """
        FOR循环:负整数到负数，且BY R寄存器
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(20, 0)
        pvr.setR(112, 4)
        time.sleep(0.5)
        assert pvr.getR(20, 1)[1][0] == 0
        assert pvr.getR(112, 1)[1][0] == 4

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(20, 1)[1][0] == 4  # 验证循环次数

    def test_冒烟05(self, prg='OrderSet/循环指令/FOR5.PRG'):
        """
        FOR循环:负整数到正数，BY 数值
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(21, 0)
        time.sleep(0.5)
        assert pvr.getR(21, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(21, 1)[1][0] == 12  # 验证循环次数

    def test_冒烟06(self, prg='OrderSet/循环指令/FOR6.PRG'):
        """
        FOR循环:内置R寄存器和整数，BY R寄存器
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(26, 0)
        pvr.setR(3, -2)
        pvr.setR(111, 5)
        time.sleep(0.5)
        assert pvr.getR(26, 1)[1][0] == 0
        assert pvr.getR(3, 1)[1][0] == -2
        assert pvr.getR(111, 1)[1][0] == 5

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(26, 1)[1][0] == 4  # 验证循环次数

    def test_冒烟07(self, prg='OrderSet/循环指令/FOR7.PRG'):
        """
        FOR循环:内置均为R寄存器，BY 数值
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(27, 0)
        pvr.setR(5, -2)
        pvr.setR(6, 0)
        time.sleep(0.5)
        assert pvr.getR(27, 1)[1][0] == 0
        assert pvr.getR(5, 1)[1][0] == -2
        assert pvr.getR(6, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(27, 1)[1][0] == 2  # 验证循环次数

    def test_冒烟08(self, prg='OrderSet/循环指令/FOR8.PRG'):
        """
        FOR循环:内置7层FOR指令嵌套
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(30, 0)
        time.sleep(0.5)
        assert pvr.getR(30, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(30, 1)[1][0] == 7560  # 验证循环次数
