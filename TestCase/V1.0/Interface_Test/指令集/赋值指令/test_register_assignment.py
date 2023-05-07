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


class Test_r:
    def test_冒烟01(self, prg='OrderSet/寄存器赋值指令/R1.PRG'):
        """
        所有R寄存器赋值成功
        :param prg: 主程序
        :return: NONE
        """
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
        for i in range(1000):  # 验证R寄存器赋值
            assert pvr.getR(i, 1)[1][0] == 1

    def test_冒烟02(self, prg='OrderSet/寄存器赋值指令/R2.PRG'):
        """
        R[]=0、正负小数、正负整数、长精度小数或比较大的整数
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        pvr.setR(1, 1)
        time.sleep(0.5)
        for i in range(2, 10):
            pvr.setR(i, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 10)[1] == [0,1,0,0,0,0,0,0,0]

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
        assert pvr.getR(0, 10)[1] == [-0.000001, 0, 0.000001, 999.999999, -999.999999, 97, 999, -99, 100000000,
                                      -100000000]  # 验证R寄存器赋值

    def test_冒烟03(self, prg='OrderSet/寄存器赋值指令/R3.PRG'):
        """
        R[]=R[]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(11, 80)
        time.sleep(0.5)
        assert pvr.getR(11, 1)[1][0] == 80
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
        assert pvr.getR(12, 1)[1][0] == 80  # 验证R寄存器赋值

    def test_冒烟04(self, prg='OrderSet/寄存器赋值指令/R4.PRG'):
        """
        R[R[]]=R[R[]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 13)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 13
        pvr.setR(1, 14)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 14
        pvr.setR(13, 13)
        time.sleep(0.5)
        assert pvr.getR(13, 1)[1][0] == 13
        pvr.setR(14, 0)
        time.sleep(0.5)
        assert pvr.getR(14, 1)[1][0] == 0

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
        assert pvr.getR(14, 1)[1][0] == 13  # 验证R寄存器赋值

    def test_冒烟05(self, prg='OrderSet/寄存器赋值指令/R5.PRG'):
        """
        R[]=JR[][]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        for i in range(15, 24):
            pvr.setR(i, 0)
        time.sleep(0.5)
        assert pvr.getR(15, 9)[1] == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        jpos = Hsc3ApiPy.JntPos
        jpos.vecPos = [2, 2.56, 20, 20.44, 200, 200.77, 43, 44, 45]
        pvr.setJR(0, 0, jpos)
        time.sleep(0.5)
        assert pvr.getJR(0, 0, 1)[1].vecPos == [2, 2.56, 20, 20.44, 200, 200.77, 43, 44, 45]

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
        assert pvr.getR(15, 9)[1] == [2, 2.56, 20, 20.44, 200, 200.77, 43, 44, 45]  # 验证R寄存器赋值

    def test_冒烟06(self, prg='OrderSet/寄存器赋值指令/R6.PRG'):
        """
        R[R[]]=JR[R[]][R[]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
        pvr.setR(1, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        pvr.setR(2, 26)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 26
        pvr.setR(26, 0)
        time.sleep(0.5)
        assert pvr.getR(26, 1)[1] == 0
        jpos = Hsc3ApiPy.JntPos
        jpos.vecPos = [20, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 1, jpos)
        time.sleep(0.5)
        assert pvr.getJR(0, 1, 1)[1].vecPos[0] == 20

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
        assert pvr.getR(26, 1)[1][0] == 20  # 验证R寄存器赋值

    def test_冒烟07(self, prg='OrderSet/寄存器赋值指令/R7.PRG'):
        """
        R[]=LR[][]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        for i in range(27, 36):
            pvr.setR(i, 0)
        time.sleep(0.5)
        assert pvr.getR(27, 9)[1] == [0, 1, 0, 0, 0, 0, 0, 0, 0]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [10.512, 0, -90.215, 195, 90, 1, 10, 111, 124]
        pvr.setLR(0, 0, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 0, 1)[1].vecPos == [10.512, 0, -90.215, 195, 90, 1, 10, 111, 124]

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
        assert pvr.getR(27, 9)[1] == [10.512, 0, -90.215, 195, 90, 1, 10, 111, 124]  # 验证R寄存器赋值

    def test_冒烟08(self, prg='OrderSet/寄存器赋值指令/R8.PRG'):
        """
        R[R[]]=LR[R[]][R[]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
        pvr.setR(1, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1
        pvr.setR(2, 36)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 36
        pvr.setR(36, 0)
        time.sleep(0.5)
        assert pvr.getR(36, 1)[1][0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [10.512, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 1, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 1, 1)[1].vecPos[0] == 10.512

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
        assert pvr.getR(36, 1)[1][0] == 10.512  # 验证R寄存器赋值

    def test_冒烟09(self, prg='OrderSet/寄存器赋值指令/R9.PRG'):
        """
        R[]=DI[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(37, 0)
        time.sleep(0.5)
        assert pvr.getR(37, 1)[1][0] == 0
        pio.setDin(500, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(500)', 5)[1] == '"true"'

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
        assert pvr.getR(37, 1)[1][0] == 1  # 验证R寄存器赋值

    def test_冒烟10(self, prg='OrderSet/寄存器赋值指令/R10.PRG'):
        """
        R[R[]]=DI[R[]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 500)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 500
        pvr.setR(1, 38)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 38
        pvr.setR(38, 0)
        time.sleep(0.5)
        assert pvr.getR(38, 1)[1][0] == 0
        pio.setDin(500, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(500)', 5)[1] == '"true"'

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
        assert pvr.getR(38, 1)[1][0] == 1  # 验证R寄存器赋值

    def test_冒烟11(self, prg='OrderSet/寄存器赋值指令/R11.PRG'):
        """
        R[]=DO[]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(39, 0)
        time.sleep(0.5)
        assert pvr.getR(39, 1)[1][0] == 0
        pio.setDout(500, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(500)', 5)[1] == '"true"'

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
        assert pvr.getR(39, 1)[1][0] == 1  # 验证R寄存器赋值

    def test_冒烟12(self, prg='OrderSet/寄存器赋值指令/R12.PRG'):
        """
        R[R[]]=DO[R[]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 500)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 500
        pvr.setR(1, 40)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 40
        pvr.setR(40, 0)
        time.sleep(0.5)
        assert pvr.getR(40, 1)[1][0] == 0
        pio.setDout(500, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(500)', 5)[1] == '"true"'

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
        assert pvr.getR(40, 1)[1][0] == 1  # 验证R寄存器赋值


class Test_jr:
    def test_冒烟01(self, prg='OrderSet/寄存器赋值指令/JR1.PRG'):
        """
        所有JR赋值，JR[]=JPOS
        :param prg: 主程序
        :return: NONE
        """
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
        p = pMot.getJntData(0)[1]  # 获取当前位置
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        # 验证JR赋值
        for q in range(1000):
            for i in range(9):
                assert float('%.3f' % pvr.getJR(0, q, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟02(self, prg='OrderSet/寄存器赋值指令/JR2.PRG'):
        """
        JR[R[X]]=JPOS
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 0, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0

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
        p = pMot.getJntData(0)[1]  # 获取当前位置
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        # 验证JR赋值
        for i in range(9):
            assert float('%.3f' % pvr.getJR(0, 0, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟03(self, prg='OrderSet/寄存器赋值指令/JR3.PRG'):
        """
        JR[X]=JR[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 2, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 2, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [101, 222, 333, 444, 555, 666, 777, 888, 999]
        pvr.setJR(0, 1, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 1, 1)[1].vecPos == [101, 222, 333, 444, 555, 666, 777, 888, 999]
        p = pvr.getJR(0, 1, 1)[1].vecPos

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
        # 验证JR赋值
        for i in range(9):
            assert float('%.3f' % pvr.getJR(0, 2, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟04(self, prg='OrderSet/寄存器赋值指令/JR4.PRG'):
        """
        JR[R[X]]=JR[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 4, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 4, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [101, 222, 333, 444, 555, 666, 777, 888, 999]
        pvr.setJR(0, 3, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 3, 1)[1].vecPos == [101, 222, 333, 444, 555, 666, 777, 888, 999]
        p = pvr.getJR(0, 3, 1)[1].vecPos
        pvr.setR(0, 3)
        time.sleep(0.5)
        pvr.setR(1, 4)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 3
        assert pvr.getR(1, 1)[1][0] == 4

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
        # 验证JR赋值
        for i in range(9):
            assert float('%.3f' % pvr.getJR(0, 4, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟05(self, prg='OrderSet/寄存器赋值指令/JR5.PRG'):
        """
        JR[]=P[]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 5, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 5, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        # 验证JR赋值
        p = [10.0, -80.0, 180.0, 0.0, 90.0, 0.0, 0.0, 0.0, 0.0]
        for i in range(9):
            assert float('%.3f' % pvr.getJR(0, 5, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟06(self, prg='OrderSet/寄存器赋值指令/JR6.PRG'):
        """
        JR[R[X]]=P[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 6, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 6, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setR(1, 0)
        time.sleep(0.5)
        pvr.setR(2, 6)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        assert pvr.getR(2, 1)[1][0] == 6

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
        # 验证JR赋值
        p = [10.0, -80.0, 180.0, 0.0, 90.0, 0.0, 0.0, 0.0, 0.0]
        for i in range(9):
            assert float('%.3f' % pvr.getJR(0, 6, 1)[1].vecPos[i]) == float('%.3f' % p[i])


class Test_lr:
    def test_冒烟01(self, prg='OrderSet/寄存器赋值指令/LR1.PRG'):
        """
        LR寄存器全部赋值，LR[X]=LPOS
        :param prg: 主程序
        :return: NONE
        """
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
        p = pMot.getLocData(0)[1]  # 获取当前位置
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        for q in range(1000):
            for i in range(9):
                assert float('%.3f' % pvr.getLR(0, q, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟02(self, prg='OrderSet/寄存器赋值指令/LR2.PRG'):
        """
        LR[R[X]]=LPOS
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 0, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0

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
        p = pMot.getLocData(0)[1]  # 获取当前位置
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        for i in range(9):
            assert float('%.3f' % pvr.getLR(0, 0, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟03(self, prg='OrderSet/寄存器赋值指令/LR3.PRG'):
        """
        LR[X]=LR[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 1, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 1, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [101, 222, 333, 444, 555, 666, 777, 888, 999]
        pvr.setLR(0, 0, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 0, 1)[1].vecPos == [101, 222, 333, 444, 555, 666, 777, 888, 999]
        p = pvr.getLR(0, 0, 1)[1].vecPos

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
        for i in range(9):
            assert float('%.3f' % pvr.getLR(0, 1, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟04(self, prg='OrderSet/寄存器赋值指令/LR4.PRG'):
        """
        LR[R[X]]=LR[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 3, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 3, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [101, 222, 333, 444, 555, 666, 777, 888, 999]
        pvr.setLR(0, 2, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 2, 1)[1].vecPos == [101, 222, 333, 444, 555, 666, 777, 888, 999]
        pvr.setR(1, 2)
        time.sleep(0.5)
        pvr.setR(2, 3)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 2
        assert pvr.getR(2, 1)[1][0] == 3

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
        p = [101, 222, 333, 444, 555, 666, 777, 888, 999]
        for i in range(9):
            assert float('%.3f' % pvr.getLR(0, 3, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟05(self, prg='OrderSet/寄存器赋值指令/LR5.PRG'):
        """
        LR[]=P[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 4, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 4, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        p = [10.0, -80.0, 180.0, 0.0, 90.0, 0.0, 0, 0, 0]
        for i in range(9):
            assert float('%.3f' % pvr.getLR(0, 4, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟06(self, prg='OrderSet/寄存器赋值指令/LR6.PRG'):
        """
        LR[R[X]]=P[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 5, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 5, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setR(1, 0)
        time.sleep(0.5)
        pvr.setR(2, 5)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        assert pvr.getR(2, 1)[1][0] == 5

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
        p = [10.0, -80.0, 180.0, 0.0, 90.0, 0.0, 0, 0, 0]
        for i in range(9):
            assert float('%.3f' % pvr.getLR(0, 5, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟07(self, prg='OrderSet/寄存器赋值指令/LR7.PRG'):
        """
        LR[X]=UF[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 6, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 6, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pMot.setWorkpiece(0, 0, [1, 23, 123, 1234, 555, 666])
        time.sleep(0.5)
        assert pMot.getWorkpiece(0, 0)[1] == [1, 23, 123, 1234, 555, 666]
        p = pMot.getWorkpiece(0, 0)[1]

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
        for i in range(9):
            assert float('%.3f' % pvr.getLR(0, 6, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟08(self, prg='OrderSet/寄存器赋值指令/LR8.PRG'):
        """
        LR[R[X]]=UF[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 7, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 7, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pMot.setWorkpiece(0, 0, [1, 23, 123, 1234, 555, 666])
        time.sleep(0.5)
        assert pMot.getWorkpiece(0, 0)[1] == [1, 23, 123, 1234, 555, 666]
        p = pMot.getWorkpiece(0, 0)[1]
        pvr.setR(1, 0)
        time.sleep(0.5)
        pvr.setR(2, 7)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        assert pvr.getR(2, 1)[1][0] == 7

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
        for i in range(9):
            assert float('%.3f' % pvr.getLR(0, 7, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟09(self, prg='OrderSet/寄存器赋值指令/LR9.PRG'):
        """
        LR[X]=UT[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 8, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 8, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pMot.setTool(0, 0, [1, 23, 123, 1234, 555, 666])
        time.sleep(0.5)
        assert pMot.setTool(0, 0)[1] == [1, 23, 123, 1234, 555, 666]
        p = pMot.getTool(0, 0)[1]

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
        for i in range(9):
            assert float('%.3f' % pvr.getLR(0, 8, 1)[1].vecPos[i]) == float('%.3f' % p[i])

    def test_冒烟10(self, prg='OrderSet/寄存器赋值指令/LR10.PRG'):
        """
        LR[R[X]]=UT[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 9, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 9, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pMot.setTool(0, 0, [1, 23, 123, 1234, 555, 666])
        time.sleep(0.5)
        assert pMot.setTool(0, 0)[1] == [1, 23, 123, 1234, 555, 666]
        p = pMot.getTool(0, 0)[1]
        pvr.setR(1, 0)
        time.sleep(0.5)
        pvr.setR(2, 9)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        assert pvr.getR(2, 1)[1][0] == 9

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
        for i in range(9):
            assert float('%.3f' % pvr.getLR(0, 9, 1)[1].vecPos[i]) == float('%.3f' % p[i])


class Test_jrxx:
    def test_冒烟01(self, prg='OrderSet/寄存器赋值指令/JRXX1.PRG'):
        """
        JR[][]内部轴及外部轴可以赋值成功
        :param prg: 主程序
        :return: NONE
        """
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
        # 验证JRXX赋值
        assert pvr.getJR(0, 0, 1)[1].vecPos[:9] == [0, 99, -99, 199.9999, -199.9999, 85.456, 85, 45, 455]

    def test_冒烟02(self, prg='OrderSet/寄存器赋值指令/JRXX2.PRG'):
        """
        JR[X][X]=R[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 100)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 100
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0,0,0,0,0,0,0,0,0]
        pvr.setJR(0, 1, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 1, 1)[1].vecPos[0] == 0

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
        # 验证LRXX赋值
        assert pvr.getJR(0, 1, 1)[1].vecPos[0] == 100

    def test_冒烟03(self, prg='OrderSet/寄存器赋值指令/JRXX3.PRG'):
        """
        JR[R[X]][R[X]]=R[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(1, 1)
        time.sleep(0.5)
        pvr.setR(2, 2)
        time.sleep(0.5)
        assert pvr.getR(1, 2)[1] == [1, 2]
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0,0,0,0,0,0,0,0,0]
        pvr.setJR(0, 1, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 1, 1)[1].vecPos[1] == 0

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 1, 1)[1].vecPos[1] == 2

    def test_冒烟04(self, prg='OrderSet/寄存器赋值指令/JRXX4.PRG'):
        """
        JR[X][X]=JR[X][X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0,0,0,0,0,0,0,0,0]
        pvr.setJR(0, 10, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 10, 1)[1].vecPos[5] == 0
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [10,10,10,10,10,10,10,10,10]
        pvr.setJR(0, 1, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 1, 1)[1].vecPos[2] == 10

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
        # 验证LRXX赋值
        assert pvr.getJR(0, 10, 1)[1].vecPos[5] == 10

    def test_冒烟05(self, prg='OrderSet/寄存器赋值指令/JRXX5.PRG'):
        """
        JR[R[X]][R[X]]=JR[R[X]][R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(1, 10)
        time.sleep(0.5)
        pvr.setR(2, 3)
        time.sleep(0.5)
        pvr.setR(3, 4)
        time.sleep(0.5)
        assert pvr.getR(1, 3)[1] == [10, 3, 4]
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        pvr.setJR(0, 10, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 10, 1)[1].vecPos == [10, 20, 30, 40, 50, 60, 70, 80, 90]

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
        # 验证LRXX赋值
        assert pvr.getJR(0, 10, 1)[1].vecPos[3] == 50

    def test_冒烟06(self, prg='OrderSet/寄存器赋值指令/JRXX6.PRG'):
        """
        JR[X][X]=LR[X][X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 10, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 10, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [111, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)

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
        # 验证LRXX赋值
        assert pvr.getJR(0, 10, 1)[1].vecPos[5] == 111

    def test_冒烟07(self, prg='OrderSet/寄存器赋值指令/JRXX7.PRG'):
        """
        JR[R[X]][R[X]]=LR[R[X]][R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(1, 11)
        time.sleep(0.5)
        pvr.setR(2, 3)
        time.sleep(0.5)
        pvr.setR(3, 4)
        time.sleep(0.5)
        assert pvr.getR(1, 3)[1] == [11, 3, 4]
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 11, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 11, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 122, 0, 0, 0, 0]
        pvr.setLR(0, 11, lPos)

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
        # 验证LRXX赋值
        assert pvr.getJR(0, 11, 1)[1].vecPos[3] == 122

    def test_冒烟08(self, prg='OrderSet/寄存器赋值指令/JRXX8.PRG'):
        """
        JR[X][X]=P[X][X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 13, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 13, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        p1 = [10.0, -80.0, 180.0, 0.0, 90.0, 0.0, 0.0, 0.0, 0.0]
        p2 = [910.445, -474.121, 1357.19, 89.9838, -4.87313, 83.9814, 0, 0, 0]

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
        # 验证LRXX赋值
        assert pvr.getJR(0, 13, 1)[1].vecPos[:2] == [p1[1], p2[1]]

    def test_冒烟09(self, prg='OrderSet/寄存器赋值指令/JRXX9.PRG'):
        """
        JR[R[X]][R[X]]=P[R[X]][R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(1, 13)
        time.sleep(0.5)
        pvr.setR(2, 0)
        time.sleep(0.5)
        pvr.setR(3, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 3)[1] == [13, 0, 1]
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 13, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 13, 1)[1].vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        p1 = [10.0, -80.0, 180.0, 0.0, 90.0, 0.0, 0.0, 0.0, 0.0]
        p2 = [910.445, -474.121, 1357.19, 89.9838, -4.87313, 83.9814, 0, 0, 0]

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
        # 验证LRXX赋值
        assert pvr.getJR(0, 13, 1)[1].vecPos[:2] == [p1[0], p2[0]]

    def test_冒烟10(self, prg='OrderSet/寄存器赋值指令/JRXX10.PRG'):
        """
        JR[R[X]][R[X]]=X
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(1, 14)
        time.sleep(0.5)
        pvr.setR(2, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 2)[1] == [14, 0]
        jpos = Hsc3ApiPy.JntPos()
        jpos.vecPos = [10, 10, 10, 10, 10, 10, 10, 10, 10]
        pvr.setJR(0, 14, jpos)
        time.sleep(1)
        assert pvr.getJR(0, 14, 1)[1].vecPos == [10, 10, 10, 10, 10, 10, 10, 10, 10]

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
        # 验证LRXX赋值
        assert pvr.getJR(0, 14, 1)[1].vecPos[0] == 0


class Test_lrxx:
    def test_冒烟01(self, prg='OrderSet/寄存器赋值指令/LRXX1.PRG'):
        """
        LR[X][X]=X
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 0, 1).vecPos == [0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 0, 1)[1].vecPos[:9] == [0, 99, -99, 199.9999, -199.9999, 85.456, 85, 45, 455]

    def test_冒烟02(self, prg='OrderSet/寄存器赋值指令/LRXX2.PRG'):
        """
        LR[R[X]][R[X]]=X
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(10, 50)
        time.sleep(0.5)
        pvr.setR(11, 0)
        time.sleep(0.5)
        assert pvr.getR(10, 2)[1] == [50, 0]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 50, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 50, 1).vecPos[0] == 0

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 50, 1)[1].vecPos[0] == 9.9

    def test_冒烟03(self, prg='OrderSet/寄存器赋值指令/LRXX3.PRG'):
        """
        LR[X][X]=R[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(10, 456)
        time.sleep(0.5)
        assert pvr.getR(10, 1)[1][0] == 456
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 50, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 50, 1).vecPos[2] == 0

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 50, 1)[1].vecPos[2] == 456

    def test_冒烟04(self, prg='OrderSet/寄存器赋值指令/LRXX4.PRG'):
        """
        LR[R[X]][R[X]]=R[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(1, 50)
        time.sleep(0.5)
        pvr.setR(2, 2)
        time.sleep(0.5)
        pvr.setR(3, 4)
        time.sleep(0.5)
        assert pvr.getR(1, 3)[1] == [50, 2, 4]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 50, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 50, 1).vecPos[4] == 0

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 50, 1)[1].vecPos[4] == 2

    def test_冒烟05(self, prg='OrderSet/寄存器赋值指令/LRXX5.PRG'):
        """
        LR[X][X]=LR[X][X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 51, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 51, 1).vecPos[5] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 50, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 0, 1).vecPos[1] == 50

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 51, 1)[1].vecPos[5] == 50

    def test_冒烟06(self, prg='OrderSet/寄存器赋值指令/LRXX6.PRG'):
        """
        LR[R[X]][R[X]]=LR[R[X]][R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(1, 51)
        time.sleep(0.5)
        pvr.setR(2, 7)
        time.sleep(0.5)
        pvr.setR(3, 51)
        time.sleep(0.5)
        pvr.setR(4, 6)
        time.sleep(0.5)
        assert pvr.getR(1, 4)[1] == [51, 7, 51, 6]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 90, 0, 0]
        pvr.setLR(0, 51, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 51, 1).vecPos[6:8] == [0, 90]

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 51, 1)[1].vecPos[6] == 90

    def test_冒烟07(self, prg='OrderSet/寄存器赋值指令/LRXX7.PRG'):
        """
        LR[X][X]=JR[X][X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 51, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 51, 1).vecPos[8] == 0
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [22, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1).vecPos[0] == 22

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 51, 1)[1].vecPos[8] == 22

    def test_冒烟08(self, prg='OrderSet/寄存器赋值指令/LRXX8.PRG'):
        """
        LR[R[X]][R[X]]=JR[R[X]][R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 52)
        time.sleep(0.5)
        pvr.setR(1, 10)
        time.sleep(0.5)
        pvr.setR(2, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 3)[1] == [52, 10, 0]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 52, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 52, 1).vecPos[0] == 0
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [20, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 10, jPos)
        assert pvr.getJR(0, 10, 1).vecPos[0] == 20

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 52, 1)[1].vecPos[0] == 20

    def test_冒烟09(self, prg='OrderSet/寄存器赋值指令/LRXX9.PRG'):
        """
        LR[X][X]=P[X][X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 52, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 52, 1).vecPos[1:3] == [0, 0]

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 52, 1)[1].vecPos[1:3] == [10, 910.445]

    def test_冒烟10(self, prg='OrderSet/寄存器赋值指令/LRXX10.PRG'):
        """
        LR[R[X]][R[X]]=P[R[X]][R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(1, 53)
        time.sleep(0.5)
        pvr.setR(2, 0)
        time.sleep(0.5)
        pvr.setR(3, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 3)[1] == [53, 0, 1]
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 53, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 53, 1).vecPos[:2] == [0, 0]

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
        # 验证LRXX赋值
        assert pvr.getLR(0, 53, 1)[1].vecPos[:2] == [-80, -474.121]