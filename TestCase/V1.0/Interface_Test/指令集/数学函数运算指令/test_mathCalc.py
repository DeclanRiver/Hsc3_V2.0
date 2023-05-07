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


class Test_math_r:
    def test_冒烟01(self, prg='OrderSet/数学函数运算指令/MATH_R1.PRG'):
        """
        DIV
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(1, 15):
            pvr.setR(i, 5)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 5

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
        # check
        assert pvr.getR(1, 14)[1] == [2, 2, 2, 2, 2, 2, 2, 2, -2, -2, 0, 0, 0, 0]

    def test_冒烟02(self, prg='OrderSet/数学函数运算指令/MATH_R2.PRG'):
        """
        DIV R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(998, 0)
        time.sleep(0.5)
        pvr.setR(999, 2.5)
        time.sleep(0.5)
        assert pvr.getR(998, 2)[1] == [0, 2.5]
        pvr.setR(15, 1)
        time.sleep(0.5)
        assert pvr.getR(15, 1)[1][0] == 1

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
        # check
        assert pvr.getR(15, 1)[1][0] == 0

    def test_冒烟03(self, prg='OrderSet/数学函数运算指令/MATH_R3.PRG'):
        """
        MOD
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(17, 30):
            pvr.setR(i, 5)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 5

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
        # check
        assert pvr.getR(17, 13)[1] == [1, 0, 1.3, 0.2, -1, 0, -0.2, -1.2, 1, 0, 1, -1, -1.5]

    def test_冒烟04(self, prg='OrderSet/数学函数运算指令/MATH_R4.PRG'):
        """
        MOD R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(998, -1.5)
        time.sleep(0.5)
        pvr.setR(999, 2.5)
        time.sleep(0.5)
        assert pvr.getR(998, 2)[1] == [-1.5, 2.5]
        pvr.setR(30, 1)
        time.sleep(0.5)
        assert pvr.getR(30, 1)[1][0] == 1

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
        # check
        assert pvr.getR(30, 1)[1][0] == -1.5

    def test_冒烟05(self, prg='OrderSet/数学函数运算指令/MATH_R5.PRG'):
        """
        ROUND
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(40, 47):
            pvr.setR(i, 1)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 1

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
        # check
        assert pvr.getR(40, 7)[1] == [2, 2, 3, 0, -1, -1, -2]

    def test_冒烟06(self, prg='OrderSet/数学函数运算指令/MATH_R6.PRG'):
        """
        ROUND R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(47, 0)
        time.sleep(0.5)
        assert pvr.getR(47, 1)[1][0] == 0
        pvr.setR(999, -1.9)
        time.sleep(0.5)
        assert pvr.getR(999, 1)[1][0] == -1.9

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
        # check
        assert pvr.getR(47, 1)[1][0] == -2

    def test_冒烟07(self, prg='OrderSet/数学函数运算指令/MATH_R7.PRG'):
        """
        TRUNC
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(60, 66):
            pvr.setR(i, 1)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 1

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
        # check
        assert pvr.getR(60, 6)[1] == [0, 5, 5, 5, -6, -6]

    def test_冒烟08(self, prg='OrderSet/数学函数运算指令/MATH_R8.PRG'):
        """
        TRUNC R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(998, -6.2)
        time.sleep(0.5)
        assert pvr.getR(998, 1)[1][0] == -6.2
        pvr.setR(999, -10.9)
        time.sleep(0.5)
        assert pvr.getR(999, 1)[1][0] == -10.9
        for i in range(66, 68):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0

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
        # check
        assert pvr.getR(66, 2)[1] == [-6, -10]

    def test_冒烟09(self, prg='OrderSet/数学函数运算指令/MATH_R9.PRG'):
        """
        ABS
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(80, 85):
            pvr.setR(i, 1)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 1

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
        # check
        assert pvr.getR(80, 5)[1] == [0, 5, 5.5, 2, 2.6]

    def test_冒烟10(self, prg='OrderSet/数学函数运算指令/MATH_R10.PRG'):
        """
        ABS R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(79, -6.5)
        time.sleep(0.5)
        assert pvr.getR(79, 1)[1][0] == -6.5
        pvr.setR(85, 1)
        time.sleep(0.5)
        assert pvr.getR(85, 1)[1][0] == 1

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
        # check
        assert pvr.getR(85, 1)[1][0] == 6.5

    def test_冒烟11(self, prg='OrderSet/数学函数运算指令/MATH_R11.PRG'):
        """
        ATAN2
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(92, 97):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0

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
        # check
        assert float('%.3f' % pvr.getR(92, 1)[1][0]) == 153.435
        assert float('%.3f' % pvr.getR(93, 1)[1][0]) == 26.565
        assert float('%.3f' % pvr.getR(94, 1)[1][0]) == -153.435
        assert pvr.getR(95, 2)[1] == [90, 0]

    def test_冒烟12(self, prg='OrderSet/数学函数运算指令/MATH_R12.PRG'):
        """
        ATAN2 R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(90, 0.5)
        time.sleep(0.5)
        assert pvr.getR(90, 1)[1][0] == 0.5
        pvr.setR(91, -1)
        time.sleep(0.5)
        assert pvr.getR(91, 1)[1][0] == -1
        pvr.setR(97, 0)
        time.sleep(0.5)
        assert pvr.getR(97, 1)[1][0] == 0

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
        # check
        assert float('%.3f' % pvr.getR(97, 1)[1][0]) == 153.435

    def test_冒烟13(self, prg='OrderSet/数学函数运算指令/MATH_R13.PRG'):
        """
        ATAN
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(110, 114):
            pvr.setR(i, 1)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 1

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
        # check
        assert pvr.getR(110, 1)[1][0] == 0
        assert float('%.3f' % pvr.getR(111, 1)[1][0]) == 26.565
        assert pvr.getR(112, 1)[1][0] == 45
        assert float('%.3f' % pvr.getR(113, 1)[1][0]) == -26.565

    def test_冒烟14(self, prg='OrderSet/数学函数运算指令/MATH_R14.PRG'):
        """
        ATAN R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(999, 0)
        time.sleep(0.5)
        assert pvr.getR(999, 1)[1][0] == 0
        pvr.setR(114, 1)
        time.sleep(0.5)
        assert pvr.getR(114, 1)[1][0] == 1

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
        # check
        assert pvr.getR(114, 1)[1][0] == 0

    def test_冒烟15(self, prg='OrderSet/数学函数运算指令/MATH_R15.PRG'):
        """
        ACOS
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(130, 135):
            pvr.setR(i, 1)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 1

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
        # check
        assert pvr.getR(130, 5)[1] == [90, 60, 120, 0, 180]

    def test_冒烟16(self, prg='OrderSet/数学函数运算指令/MATH_R16.PRG'):
        """
        ACOS R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(129, 0.5)
        time.sleep(0.5)
        assert pvr.getR(129, 1)[1][0] == 0.5
        pvr.setR(135, 1)
        time.sleep(0.5)
        assert pvr.getR(135, 1)[1][0] == 1

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
        # check
        assert pvr.getR(135, 1)[1][0] == 60

    def test_冒烟17(self, prg='OrderSet/数学函数运算指令/MATH_R17.PRG'):
        """
        ASIN
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(150, 155):
            pvr.setR(i, 1)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 1

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
        # check
        assert pvr.getR(150, 5)[1] == [0, 30, -30, 90, -90]

    def test_冒烟18(self, prg='OrderSet/数学函数运算指令/MATH_R18.PRG'):
        """
        ASIN R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(999, 0)
        time.sleep(0.5)
        assert pvr.getR(999, 1)[1][0] == 0
        pvr.setR(155, 1)
        time.sleep(0.5)
        assert pvr.getR(155, 1)[1][0] == 1

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
        # check
        assert pvr.getR(155, 1)[1][0] == 0

    def test_冒烟19(self, prg='OrderSet/数学函数运算指令/MATH_R19.PRG'):
        """
        TAN
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(170, 173):
            pvr.setR(i, 5)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 5

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
        # check
        assert pvr.getR(170, 3)[1] == [0, 1, -1]

    def test_冒烟20(self, prg='OrderSet/数学函数运算指令/MATH_R20.PRG'):
        """
        TAN R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(999, 0)
        time.sleep(0.5)
        assert pvr.getR(999, 1)[1][0] == 0
        pvr.setR(173, 1)
        time.sleep(0.5)
        assert pvr.getR(173, 1)[1][0] == 1

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
        # check
        assert pvr.getR(173, 1)[1][0] == 0

    def test_冒烟21(self, prg='OrderSet/数学函数运算指令/MATH_R21.PRG'):
        """
        COS
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(190, 195):
            pvr.setR(i, 5)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 5

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
        # check
        assert pvr.getR(190, 5)[1] == [1, 0, -1, 0, -1]

    def test_冒烟22(self, prg='OrderSet/数学函数运算指令/MATH_R22.PRG'):
        """
        COS R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(189, -360)
        time.sleep(0.5)
        assert pvr.getR(189, 1)[1][0] == -360
        pvr.setR(195, 0)
        time.sleep(0.5)
        assert pvr.getR(195, 1)[1][0] == 0

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
        # check
        assert pvr.getR(195, 1)[1][0] == 1

    def test_冒烟23(self, prg='OrderSet/数学函数运算指令/MATH_R23.PRG'):
        """
        SIN
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(310, 314):
            pvr.setR(i, 5)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 5

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
        # check
        assert pvr.getR(310, 4)[1] == [0, 1, 0, 1]

    def test_冒烟24(self, prg='OrderSet/数学函数运算指令/MATH_R24.PRG'):
        """
        SIN R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(309, -270)
        time.sleep(0.5)
        assert pvr.getR(309, 1)[1][0] == -270
        pvr.setR(314, 0)
        time.sleep(0.5)
        assert pvr.getR(314, 1)[1][0] == 0

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
        # check
        assert pvr.getR(314, 1)[1][0] == 1

    def test_冒烟25(self, prg='OrderSet/数学函数运算指令/MATH_R25.PRG'):
        """
        SQRT
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(330, 332):
            pvr.setR(i, 5)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 5

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
        # check
        assert pvr.getR(330, 2)[1] == [0, 6]

    def test_冒烟26(self, prg='OrderSet/数学函数运算指令/MATH_R26.PRG'):
        """
        SQRT R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(329, 1000)
        time.sleep(0.5)
        assert pvr.getR(329, 1)[1][0] == 1000
        pvr.setR(332, 0)
        time.sleep(0.5)
        assert pvr.getR(332, 1)[1][0] == 0

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
        # check
        assert float('%.3f' % pvr.getR(332, 1)[1][0]) == 31.623

    def test_冒烟27(self, prg='OrderSet/数学函数运算指令/MATH_R27.PRG'):
        """
        加法运算（+）
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(700, 702):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0

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
        # check
        assert pvr.getR(700, 2)[1] == [6827.017, -50]

    def test_冒烟28(self, prg='OrderSet/数学函数运算指令/MATH_R28.PRG'):
        """
        加法运算（+） R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(702, 704):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
        for i in range(6, 8):
            pvr.setR(i, 2)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 2

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
        # check
        assert pvr.getR(702, 2)[1] == [90.8, 4]

    def test_冒烟29(self, prg='OrderSet/数学函数运算指令/MATH_R29.PRG'):
        """
        加法运算（+） JR[][] LR[][] R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0 , jPos)
        time.sleep(0.5)
        assert pvr.getJR(0, 0, 1).vecPos[0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [-90, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 0, 1).vecPos[0] == -90
        pvr.setR(704, 0)
        time.sleep(0.5)
        assert pvr.getR(704, 1)[1][0] == 0

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
        # check
        assert pvr.getR(704, 1)[1][0] == -180

    def test_冒烟30(self, prg='OrderSet/数学函数运算指令/MATH_R30.PRG'):
        """
        加法运算（+），和数学函数运算结合
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(705, 0)
        time.sleep(0.5)
        assert pvr.getR(705, 1)[1][0] == 0

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
        # check
        assert pvr.getR(705, 1)[1][0] == 146

    def test_冒烟31(self, prg='OrderSet/数学函数运算指令/MATH_R31.PRG'):
        """
        减法运算（-）
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(710, 712):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0

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
        # check
        assert pvr.getR(710, 2)[1] == [6504.983, -130]

    def test_冒烟32(self, prg='OrderSet/数学函数运算指令/MATH_R32.PRG'):
        """
        减法运算（-） R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(712, 714):
            pvr.setR(i, 1)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 1
        for i in range(6, 8):
            pvr.setR(i, 2)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 2

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
        # check
        assert pvr.getR(712, 2)[1] == [86.8, 0]

    def test_冒烟33(self, prg='OrderSet/数学函数运算指令/MATH_R33.PRG'):
        """
        减法运算（-） R[] JR[][] LR[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(714, 0)
        time.sleep(0.5)
        assert pvr.getR(714, 1)[1][0] == 0
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        time.sleep(0.5)
        assert pvr.getJR(0, 0, 1).vecPos[0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [-90, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 0, 1).vecPos[0] == -90

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
        # check
        assert pvr.getR(714, 1)[1][0] == 180

    def test_冒烟34(self, prg='OrderSet/数学函数运算指令/MATH_R34.PRG'):
        """
        减法运算（-），与数学函数配合使用
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(715, 0)
        time.sleep(0.5)
        assert pvr.getR(715, 1)[1][0] == 0

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
        # check
        assert pvr.getR(715, 1)[1][0] == -116

    def test_冒烟35(self, prg='OrderSet/数学函数运算指令/MATH_R35.PRG'):
        """
        乘法运算（*）
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(720, 722):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0

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
        # check
        assert pvr.getR(720, 2)[1] == [4717521.2007, -3600]

    def test_冒烟36(self, prg='OrderSet/数学函数运算指令/MATH_R36.PRG'):
        """
        乘法运算（*） R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(722, 724):
            pvr.setR(i, 1)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 1
        for i in range(6, 8):
            pvr.setR(i, 2)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 2

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
        # check
        assert pvr.getR(722, 2)[1] == [1408, 4]

    def test_冒烟37(self, prg='OrderSet/数学函数运算指令/MATH_R37.PRG'):
        """
        乘法运算（*） R[] JR[][] LR[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(724, 1)
        time.sleep(0.5)
        assert pvr.getR(724, 1)[1][0] == 1
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        time.sleep(0.5)
        assert pvr.getJR(0, 0, 1).vecPos[0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [-90, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 0, 1).vecPos[0] == -90

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
        # check
        assert pvr.getR(724, 1)[1][0] == 0

    def test_冒烟38(self, prg='OrderSet/数学函数运算指令/MATH_R38.PRG'):
        """
        乘法运算（*），与数学函数配合使用
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(725, 0)
        time.sleep(0.5)
        assert pvr.getR(725, 1)[1][0] == 0

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
        # check
        assert pvr.getR(725, 1)[1][0] == 8100

    def test_冒烟39(self, prg='OrderSet/数学函数运算指令/MATH_R39.PRG'):
        """
        除法运算（/）
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(730, 732):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0

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
        # check
        assert pvr.getR(730, 2)[1] == [2000, -2.25]

    def test_冒烟40(self, prg='OrderSet/数学函数运算指令/MATH_R40.PRG'):
        """
        除法运算（/） R[]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(722, 724):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
        for i in range(6, 8):
            pvr.setR(i, 2)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 2

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
        # check
        assert pvr.getR(732, 2)[1] == [0.05, 1]

    def test_冒烟41(self, prg='OrderSet/数学函数运算指令/MATH_R41.PRG'):
        """
        除法运算（/） R[] JR[][] LR[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(734, 1)
        time.sleep(0.5)
        assert pvr.getR(734, 1)[1][0] == 1
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        time.sleep(0.5)
        assert pvr.getJR(0, 0, 1).vecPos[0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [-90, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        time.sleep(0.5)
        assert pvr.getLR(0, 0, 1).vecPos[0] == -90

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
        # check
        assert pvr.getR(734, 1)[1][0] == 0

    def test_冒烟42(self, prg='OrderSet/数学函数运算指令/MATH_R42.PRG'):
        """
        除法运算（/），与数学函数配合使用
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(735, 1)
        time.sleep(0.5)
        assert pvr.getR(735, 1)[1][0] == 1

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
        # check
        assert pvr.getR(735, 1)[1][0] == 0

    def test_冒烟43(self, prg='OrderSet/数学函数运算指令/MATH_R43.PRG'):
        """
        DIV P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(804, 0)
        time.sleep(0.5)
        assert pvr.getR(804, 1)[1][0] == 0

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
        # check
        assert pvr.getR(804, 1)[1][0] == 1

    def test_冒烟44(self, prg='OrderSet/数学函数运算指令/MATH_R44.PRG'):
        """
        MOD P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(805, 1)
        time.sleep(0.5)
        assert pvr.getR(805, 1)[1][0] == 1

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
        # check
        assert pvr.getR(805, 1)[1][0] == 0

    def test_冒烟45(self, prg='OrderSet/数学函数运算指令/MATH_R45.PRG'):
        """
        ROUND P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(806, 1)
        time.sleep(0.5)
        assert pvr.getR(806, 1)[1][0] == 1

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
        # check
        assert pvr.getR(806, 1)[1][0] == 10

    def test_冒烟46(self, prg='OrderSet/数学函数运算指令/MATH_R46.PRG'):
        """
        TRUNC P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(807, 1)
        time.sleep(0.5)
        assert pvr.getR(807, 1)[1][0] == 1

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
        # check
        assert pvr.getR(807, 1)[1][0] == 10

    def test_冒烟47(self, prg='OrderSet/数学函数运算指令/MATH_R47.PRG'):
        """
        ABS P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(808, 1)
        time.sleep(0.5)
        assert pvr.getR(808, 1)[1][0] == 1

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
        # check
        assert pvr.getR(808, 1)[1][0] == 90

    def test_冒烟48(self, prg='OrderSet/数学函数运算指令/MATH_R48.PRG'):
        """
        ATAN P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(809, 1)
        time.sleep(0.5)
        assert pvr.getR(809, 1)[1][0] == 1

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
        # check
        assert pvr.getR(809, 1)[1][0] == 0

    def test_冒烟49(self, prg='OrderSet/数学函数运算指令/MATH_R49.PRG'):
        """
        ACOS P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(810, 1)
        time.sleep(0.5)
        assert pvr.getR(810, 1)[1][0] == 1

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
        # check
        assert pvr.getR(810, 1)[1][0] == 90

    def test_冒烟50(self, prg='OrderSet/数学函数运算指令/MATH_R50.PRG'):
        """
        ASIN P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(811, 1)
        time.sleep(0.5)
        assert pvr.getR(811, 1)[1][0] == 1

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
        # check
        assert pvr.getR(811, 1)[1][0] == 0

    def test_冒烟51(self, prg='OrderSet/数学函数运算指令/MATH_R51.PRG'):
        """
        TAN P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(812, 1)
        time.sleep(0.5)
        assert pvr.getR(812, 1)[1][0] == 1

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
        # check
        assert pvr.getR(812, 1)[1][0] == 0

    def test_冒烟52(self, prg='OrderSet/数学函数运算指令/MATH_R52.PRG'):
        """
        TAN P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(813, 1)
        time.sleep(0.5)
        assert pvr.getR(813, 1)[1][0] == 1

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
        # check
        assert pvr.getR(813, 1)[1][0] == -1

    def test_冒烟53(self, prg='OrderSet/数学函数运算指令/MATH_R53.PRG'):
        """
        SIN P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(814, 1)
        time.sleep(0.5)
        assert pvr.getR(814, 1)[1][0] == 1

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
        # check
        assert pvr.getR(814, 1)[1][0] == 0

    def test_冒烟54(self, prg='OrderSet/数学函数运算指令/MATH_R54.PRG'):
        """
        SQRT P[][]
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(815, 1)
        time.sleep(0.5)
        assert pvr.getR(815, 1)[1][0] == 1

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
        # check
        assert pvr.getR(815, 1)[1][0] == 10


class Test_同级运算:
    def test_冒烟01(self, prg='OrderSet/数学函数运算指令/MATH_AR001.PRG'):
        """
        SQRT SQRT
        :param prg:主程序
        :return:NONE
        """
        # 前置
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
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        # check
        assert pvr.getR(1, 1)[1][0] == 10.1

    def test_冒烟02(self, prg='OrderSet/数学函数运算指令/MATH_AR002.PRG'):
        """
        SQRT ABS
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(2, 0)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 0

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
        # check
        assert pvr.getR(2, 1)[1][0] == 10.1

    def test_冒烟03(self, prg='OrderSet/数学函数运算指令/MATH_AR003.PRG'):
        """
        SQRT TRUNC
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(3, 0)
        time.sleep(0.5)
        assert pvr.getR(3, 1)[1][0] == 0

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
        # check
        assert float('%.3f' % pvr.getR(3, 1)[1][0]) == 10.1

    def test_冒烟04(self, prg='OrderSet/数学函数运算指令/MATH_AR004.PRG'):
        """
        SQRT ROUND
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(4, 0)
        time.sleep(0.5)
        assert pvr.getR(4, 1)[1][0] == 0

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
        # check
        assert float('%.3f' % pvr.getR(4, 1)[1][0]) == 10.1

    def test_冒烟05(self, prg='OrderSet/数学函数运算指令/MATH_AR005.PRG'):
        """
        ABS SQRT
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(5, 0)
        time.sleep(0.5)
        assert pvr.getR(5, 1)[1][0] == 0

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
        # check
        assert pvr.getR(5, 1)[1][0] == 10.1

    def test_冒烟06(self, prg='OrderSet/数学函数运算指令/MATH_AR006.PRG'):
        """
        ABS ABS
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(6, 0)
        time.sleep(0.5)
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
        # check
        assert pvr.getR(5, 1)[1][0] == 102.01

    def test_冒烟07(self, prg='OrderSet/数学函数运算指令/MATH_AR007.PRG'):
        """
        ABS TRUNC
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(7, 0)
        time.sleep(0.5)
        assert pvr.getR(7, 1)[1][0] == 0

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
        # check
        assert pvr.getR(7, 1)[1][0] == 102

    def test_冒烟08(self, prg='OrderSet/数学函数运算指令/MATH_AR008.PRG'):
        """
        ABS ROUND
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(8, 0)
        time.sleep(0.5)
        assert pvr.getR(8, 1)[1][0] == 0

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
        # check
        assert pvr.getR(8, 1)[1][0] == 102

    def test_冒烟09(self, prg='OrderSet/数学函数运算指令/MATH_AR009.PRG'):
        """
        TRUNC SQRT
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(9, 0)
        time.sleep(0.5)
        assert pvr.getR(9, 1)[1][0] == 0

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
        # check
        assert pvr.getR(9, 1)[1][0] == 10

    def test_冒烟010(self, prg='OrderSet/数学函数运算指令/MATH_AR0010.PRG'):
        """
        TRUNC ABS
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
        # check
        assert pvr.getR(10, 1)[1][0] == 10.1

    def test_冒烟11(self, prg='OrderSet/数学函数运算指令/MATH_AR0011.PRG'):
        """
        TRUNC TRUNC
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
        # check
        assert pvr.getR(11, 1)[1][0] == 102

    def test_冒烟12(self, prg='OrderSet/数学函数运算指令/MATH_AR0012.PRG'):
        """
        TRUNC ROUND
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
        # check
        assert pvr.getR(12, 1)[1][0] == 102

    def test_冒烟13(self, prg='OrderSet/数学函数运算指令/MATH_AR0013.PRG'):
        """
        ROUND SQRT
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(13, 0)
        time.sleep(0.5)
        assert pvr.getR(13, 1)[1][0] == 0

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
        # check
        assert pvr.getR(13, 1)[1][0] == 10.1

    def test_冒烟14(self, prg='OrderSet/数学函数运算指令/MATH_AR0014.PRG'):
        """
        ROUND ABS
        :param prg:主程序
        :return:NONE
        """
        # 前置
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
        # check
        assert pvr.getR(14, 1)[1][0] == 102

    def test_冒烟15(self, prg='OrderSet/数学函数运算指令/MATH_AR0015.PRG'):
        """
        ROUND TRUNC
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(15, 0)
        time.sleep(0.5)
        assert pvr.getR(15, 1)[1][0] == 0

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
        # check
        assert pvr.getR(15, 1)[1][0] == 102

    def test_冒烟16(self, prg='OrderSet/数学函数运算指令/MATH_AR0016.PRG'):
        """
        ROUND ROUND
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(16, 0)
        time.sleep(0.5)
        assert pvr.getR(16, 1)[1][0] == 0

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
        # check
        assert pvr.getR(16, 1)[1][0] == 102