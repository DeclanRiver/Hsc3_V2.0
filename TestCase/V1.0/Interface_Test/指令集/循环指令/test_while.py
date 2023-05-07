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


class Test_while:
    def test_冒烟01(self,prg='OrderSet/循环指令/WHILE01.PRG'):
        """
        R[X] = X，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(9, 132)
        time.sleep(0.5)
        assert pvr.getR(9, 1)[1][0] == 132
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
            while pvr.getR(10, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(10, 1)[1][0] >= 10  # check

    def test_冒烟02(self,prg='OrderSet/循环指令/WHILE02.PRG'):
        """
        JR[X][X] = X，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [132, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[0] == 132
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
            while pvr.getR(11, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(11, 1)[1][0] >= 10  # check

    def test_冒烟03(self,prg='OrderSet/循环指令/WHILE03.PRG'):
        """
        LR[X][X] = X，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [132, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[0] == 132
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
            while pvr.getR(12, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(12, 1)[1][0] >= 10  # check

    def test_冒烟04(self,prg='OrderSet/循环指令/WHILE04.PRG'):
        """
        关节点P[][] = X，验证while符合时执行结果；
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
            while pvr.getR(13, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(13, 1)[1][0] >= 10  # check

    def test_冒烟05(self,prg='OrderSet/循环指令/WHILE05.PRG'):
        """
        空间点P[][] = X，验证while符合时执行结果；
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
            while pvr.getR(14, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(14, 1)[1][0] >= 10  # check

    def test_冒烟06(self,prg='OrderSet/循环指令/WHILE06.PRG'):
        """
        DI[X] = ON，验证while符合时执行结果；
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(15, 0)
        time.sleep(0.5)
        assert pvr.getR(15, 1)[1][0] == 0
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
            while pvr.getR(15, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(15, 1)[1][0] >= 10  # check

    def test_冒烟07(self,prg='OrderSet/循环指令/WHILE07.PRG'):
        """
        DO[X] = ON，验证while符合时执行结果；
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(16, 0)
        time.sleep(0.5)
        assert pvr.getR(16, 1)[1][0] == 0
        pio.setDout(5, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(5)', 5)[1] == '"true"'

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(16, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(16, 1)[1][0] >= 10  # check

    def test_冒烟08(self,prg='OrderSet/循环指令/WHILE08.PRG'):
        """
        SQRT，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(17, 0)
        time.sleep(0.5)
        assert pvr.getR(17, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(17, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(17, 1)[1][0] >= 10  # check

    def test_冒烟09(self,prg='OrderSet/循环指令/WHILE09.PRG'):
        """
        ABS，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(18, 0)
        time.sleep(0.5)
        assert pvr.getR(18, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(18, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(18, 1)[1][0] >= 10  # check

    def test_冒烟10(self,prg='OrderSet/循环指令/WHILE10.PRG'):
        """
        TRUNC，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(19, 0)
        time.sleep(0.5)
        assert pvr.getR(19, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(19, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(19, 1)[1][0] >= 10  # check

    def test_冒烟11(self,prg='OrderSet/循环指令/WHILE11.PRG'):
        """
        ROUND，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(20, 0)
        time.sleep(0.5)
        assert pvr.getR(20, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(20, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(20, 1)[1][0] >= 10  # check

    def test_冒烟12(self,prg='OrderSet/循环指令/WHILE12.PRG'):
        """
        SIN，验证while符合时执行结果
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
            while pvr.getR(21, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(21, 1)[1][0] >= 10  # check

    def test_冒烟13(self, prg='OrderSet/循环指令/WHILE13.PRG'):
        """
        COS，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(22, 0)
        time.sleep(0.5)
        assert pvr.getR(22, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(22, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(22, 1)[1][0] >= 10  # check

    def test_冒烟14(self, prg='OrderSet/循环指令/WHILE14.PRG'):
        """
        TAN，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(23, 0)
        time.sleep(0.5)
        assert pvr.getR(23, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(23, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(23, 1)[1][0] >= 10  # check

    def test_冒烟15(self, prg='OrderSet/循环指令/WHILE15.PRG'):
        """
        ASIN，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(24, 0)
        time.sleep(0.5)
        assert pvr.getR(24, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(24, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(24, 1)[1][0] >= 10  # check

    def test_冒烟16(self, prg='OrderSet/循环指令/WHILE16.PRG'):
        """
        ACOS，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(25, 0)
        time.sleep(0.5)
        assert pvr.getR(25, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(25, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(25, 1)[1][0] >= 10  # check

    def test_冒烟17(self, prg='OrderSet/循环指令/WHILE17.PRG'):
        """
        ATAN，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(26, 0)
        time.sleep(0.5)
        assert pvr.getR(26, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(26, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(26, 1)[1][0] >= 10  # check

    def test_冒烟18(self, prg='OrderSet/循环指令/WHILE18.PRG'):
        """
        DIV，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(27, 0)
        time.sleep(0.5)
        assert pvr.getR(27, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(27, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(27, 1)[1][0] >= 10  # check

    def test_冒烟19(self, prg='OrderSet/循环指令/WHILE19.PRG'):
        """
        MOD，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(28, 0)
        time.sleep(0.5)
        assert pvr.getR(28, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(28, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(28, 1)[1][0] >= 10  # check

    def test_冒烟20(self,prg='OrderSet/循环指令/WHILE20.PRG'):
        """
        +，验证while符合时执行结果
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
            while pvr.getR(30, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(30, 1)[1][0] >= 10  # check

    def test_冒烟21(self,prg='OrderSet/循环指令/WHILE21.PRG'):
        """
        -，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(31, 0)
        time.sleep(0.5)
        assert pvr.getR(31, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(31, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(31, 1)[1][0] >= 10  # check

    def test_冒烟22(self,prg='OrderSet/循环指令/WHILE22.PRG'):
        """
        *，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(32, 0)
        time.sleep(0.5)
        assert pvr.getR(32, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(32, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(32, 1)[1][0] >= 10  # check

    def test_冒烟23(self,prg='OrderSet/循环指令/WHILE23.PRG'):
        """
        /，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(33, 0)
        time.sleep(0.5)
        assert pvr.getR(33, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(33, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(33, 1)[1][0] >= 10  # check

    def test_冒烟24(self,prg='OrderSet/循环指令/WHILE24.PRG'):
        """
        ()，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(34, 0)
        time.sleep(0.5)
        assert pvr.getR(34, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(34, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(34, 1)[1][0] >= 10  # check

    def test_冒烟25(self,prg='OrderSet/循环指令/WHILE25.PRG'):
        """
        R[]=R[]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
        pvr.setR(1, 10)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 10
        pvr.setR(35, 0)
        time.sleep(0.5)
        assert pvr.getR(35, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(35, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(35, 1)[1][0] >= 10  # check

    def test_冒烟26(self,prg='OrderSet/循环指令/WHILE26.PRG'):
        """
        R[]=JR[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 100)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 100
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [100, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[0] == 100
        pvr.setR(36, 0)
        time.sleep(0.5)
        assert pvr.getR(36, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(36, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(36, 1)[1][0] >= 10  # check

    def test_冒烟27(self,prg='OrderSet/循环指令/WHILE27.PRG'):
        """
        R[]=LR[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 23)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 23
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [23, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 5, lPos)
        assert pvr.getLR(0, 5, 1)[1].vecPos[0] == 23
        pvr.setLR(0, 0, lPos)
        pvr.setR(37, 0)
        time.sleep(0.5)
        assert pvr.getR(37, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(37, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(37, 1)[1][0] >= 10  # check

    def test_冒烟28(self,prg='OrderSet/循环指令/WHILE28.PRG'):
        """
        R[]=P[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 304.068)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 304.068
        pvr.setR(38, 0)
        time.sleep(0.5)
        assert pvr.getR(38, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(38, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(38, 1)[1][0] >= 10  # check

    def test_冒烟29(self,prg='OrderSet/循环指令/WHILE29.PRG'):
        """
        JR[][]=R[]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [0, 10, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[1] == 10
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
        pvr.setR(39, 0)
        time.sleep(0.5)
        assert pvr.getR(39, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(39, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(39, 1)[1][0] >= 10  # check

    def test_冒烟30(self,prg='OrderSet/循环指令/WHILE30.PRG'):
        """
        JR[][]=JR[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [10, 10, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[:2] == [10, 10]
        pvr.setR(40, 0)
        time.sleep(0.5)
        assert pvr.getR(40, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(40, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(40, 1)[1][0] >= 10  # check

    def test_冒烟31(self,prg='OrderSet/循环指令/WHILE31.PRG'):
        """
        JR[][]=LR[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [0, 0, 90, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 1, jPos)
        lPos = Hsc3ApiPy.LocPos()
        assert pvr.getJR(0, 1, 1)[1].vecPos[2] == 90
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 90, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[1] == 90
        pvr.setR(41, 0)
        time.sleep(0.5)
        assert pvr.getR(41, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(41, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(41, 1)[1][0] >= 10  # check

    def test_冒烟32(self,prg='OrderSet/循环指令/WHILE32.PRG'):
        """
        JR[][]=P[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [304.068, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 5, jPos)
        assert pvr.getJR(0, 5, 1)[1].vecPos[0] == 304.068
        pvr.setR(42, 0)
        time.sleep(0.5)
        assert pvr.getR(42, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(42, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(42, 1)[1][0] >= 10  # check

    def test_冒烟33(self,prg='OrderSet/循环指令/WHILE33.PRG'):
        """
        LR[][]=R[]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(42, 0)
        pvr.setR(43, 0)
        time.sleep(0.5)
        assert pvr.getR(43, 1)[1][0] == 0
        assert pvr.getR(42, 1)[1][0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 5, lPos)
        assert pvr.getLR(0, 5, 1)[1].vecPos[0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(43, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(43, 1)[1][0] >= 10  # check

    def test_冒烟34(self,prg='OrderSet/循环指令/WHILE34.PRG'):
        """
        LR[][]=JR[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [0, 50, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 5, jPos)
        assert pvr.getJR(0, 5, 1)[1].vecPos[1] == 50
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 50, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 5, lPos)
        assert pvr.getLR(0, 5, 1)[1].vecPos[1] == 50
        pvr.setR(44, 0)
        time.sleep(0.5)
        assert pvr.getR(44, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(44, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(44, 1)[1][0] >= 10  # check

    def test_冒烟35(self,prg='OrderSet/循环指令/WHILE35.PRG'):
        """
        LR[][]=LR[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 345, 345, 0, 0, 0]
        pvr.setLR(0, 5, lPos)
        assert pvr.getLR(0, 5, 1)[1].vecPos[4:6] == [345, 345]
        pvr.setR(45, 0)
        time.sleep(0.5)
        assert pvr.getR(45, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(45, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(45, 1)[1][0] >= 10  # check

    def test_冒烟36(self,prg='OrderSet/循环指令/WHILE36.PRG'):
        """
        LR[][]=P[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, -450.897, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 6, lPos)
        assert pvr.getLR(0, 6, 1)[1].vecPos[1] == -450.897
        pvr.setR(46, 0)
        time.sleep(0.5)
        assert pvr.getR(46, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(46, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(46, 1)[1][0] >= 10  # check

    def test_冒烟37(self,prg='OrderSet/循环指令/WHILE37.PRG'):
        """
        P[][]=R[]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 69.7487)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 69.7487
        pvr.setR(47, 0)
        time.sleep(0.5)
        assert pvr.getR(47, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(47, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(47, 1)[1][0] >= 10  # check

    def test_冒烟38(self,prg='OrderSet/循环指令/WHILE38.PRG'):
        """
        P[][]=JR[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [137.241, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 10, jPos)
        assert pvr.getJR(0, 10, 1)[1].vecPos[0] == 137.241
        pvr.setR(48, 0)
        time.sleep(0.5)
        assert pvr.getR(48, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(48, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(48, 1)[1][0] >= 10  # check

    def test_冒烟39(self,prg='OrderSet/循环指令/WHILE39.PRG'):
        """
        P[][]=LR[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [-1.841, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 10, lPos)
        assert pvr.getLR(0, 10, 1)[1].vecPos[0] == -1.841
        pvr.setR(49, 0)
        time.sleep(0.5)
        assert pvr.getR(49, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(49, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(49, 1)[1][0] >= 10  # check

    def test_冒烟40(self,prg='OrderSet/循环指令/WHILE40.PRG'):
        """
        P[][]=P[][]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 0)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(50, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(50, 1)[1][0] >= 10  # check

    def test_冒烟41(self,prg='OrderSet/循环指令/WHILE41.PRG'):
        """
        >，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 3)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 3
        pvr.setR(51, 0)
        time.sleep(0.5)
        assert pvr.getR(51, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(51, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(51, 1)[1][0] >= 10  # check

    def test_冒烟42(self,prg='OrderSet/循环指令/WHILE42.PRG'):
        """
        >=，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 1)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 1
        pvr.setR(52, 0)
        time.sleep(0.5)
        assert pvr.getR(52, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(52, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(52, 1)[1][0] >= 10  # check

    def test_冒烟43(self,prg='OrderSet/循环指令/WHILE43.PRG'):
        """
        <，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 0.1)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 0.1
        pvr.setR(53, 0)
        time.sleep(0.5)
        assert pvr.getR(53, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(53, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(53, 1)[1][0] >= 10  # check

    def test_冒烟44(self,prg='OrderSet/循环指令/WHILE44.PRG'):
        """
        <=，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 1)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 1
        pvr.setR(54, 0)
        time.sleep(0.5)
        assert pvr.getR(54, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(54, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(54, 1)[1][0] >= 10  # check

    def test_冒烟45(self,prg='OrderSet/循环指令/WHILE45.PRG'):
        """
        <>，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 4)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 4
        pvr.setR(55, 0)
        time.sleep(0.5)
        assert pvr.getR(55, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(55, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(55, 1)[1][0] >= 10  # check

    def test_冒烟46(self,prg='OrderSet/循环指令/WHILE41.PRG'):
        """
        条件不符合，>，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 1)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 1
        pvr.setR(51, 0)
        time.sleep(0.5)
        assert pvr.getR(51, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(51, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(51, 1)[1][0] == 0  # check

    def test_冒烟47(self,prg='OrderSet/循环指令/WHILE42.PRG'):
        """
        条件不符合，>=，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 0.9)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 0.9
        pvr.setR(52, 0)
        time.sleep(0.5)
        assert pvr.getR(52, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(52, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(52, 1)[1][0] == 0  # check

    def test_冒烟48(self,prg='OrderSet/循环指令/WHILE43.PRG'):
        """
        不符合条件，<，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 1)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 1
        pvr.setR(53, 0)
        time.sleep(0.5)
        assert pvr.getR(53, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(53, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(53, 1)[1][0] == 0  # check

    def test_冒烟49(self,prg='OrderSet/循环指令/WHILE44.PRG'):
        """
        不符合条件，<=，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 2)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 2
        pvr.setR(54, 0)
        time.sleep(0.5)
        assert pvr.getR(54, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(54, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(54, 1)[1][0] == 0  # check

    def test_冒烟50(self,prg='OrderSet/循环指令/WHILE45.PRG'):
        """
        不符合条件，<>，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(50, 1)
        time.sleep(0.5)
        assert pvr.getR(50, 1)[1][0] == 1
        pvr.setR(55, 0)
        time.sleep(0.5)
        assert pvr.getR(55, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(55, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(55, 1)[1][0] == 0  # check

    def test_冒烟51(self,prg='OrderSet/循环指令/WHILE01.PRG'):
        """
        不符合条件，=，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(9, 1)
        time.sleep(0.5)
        assert pvr.getR(9, 1)[1][0] == 1
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
            while pvr.getR(10, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(10, 1)[1][0] == 0  # check

    def test_冒烟52(self,prg='OrderSet/循环指令/WHILE46.PRG'):
        """
        DO[X] = OFF，验证while符合时执行结果；
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(56, 0)
        time.sleep(0.5)
        assert pvr.getR(56, 1)[1][0] == 0
        pio.setDout(5, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(5)', 5)[1] == '"false"'

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(56, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(56, 1)[1][0] >= 10  # check

    def test_冒烟53(self,prg='OrderSet/循环指令/WHILE47.PRG'):
        """
        DI[X] = OFF，验证while符合时执行结果；
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(57, 0)
        time.sleep(0.5)
        assert pvr.getR(57, 1)[1][0] == 0
        pio.setDin(500, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(500)', 5)[1] == '"false"'

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(57, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(57, 1)[1][0] >= 10  # check

    def test_冒烟54(self,prg='OrderSet/循环指令/WHILE48.PRG'):
        """
        嵌套5层循环，验证while符合时执行结果；
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(60, 65):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
        pio.setDout(500, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(500)', 5)[1] == '"true"'
        pio.setDin(500, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(500)', 5)[1] == '"false"'
        pvr.setR(0, 1)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 1
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [10, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
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
            while pvr.getR(60, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(60, 1)[1][0] >= 10  # check
        for i in range(61, 65):
            assert pvr.getR(i, 1)[1][0] == 1

    def test_冒烟55(self,prg='OrderSet/循环指令/WHILE49.PRG'):
        """
        not R[]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，不执行]前置
        pvr.setR(1, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1
        pvr.setR(70, 0)
        time.sleep(0.5)
        assert pvr.getR(70, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(70, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(70, 1)[1][0] == 0  # check

        # [条件不符合，执行]前置
        pvr.setR(1, 2)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 2
        pvr.setR(70, 0)
        time.sleep(0.5)
        assert pvr.getR(70, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(70, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(70, 1)[1][0] >= 10  # check

    def test_冒烟56(self,prg='OrderSet/循环指令/WHILE50.PRG'):
        """
        R[] AND R[]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，执行]前置
        pvr.setR(1, 1.5)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1.5
        pvr.setR(2, 2.2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2.2
        pvr.setR(71, 0)
        time.sleep(0.5)
        assert pvr.getR(71, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(71, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(71, 1)[1][0] >= 10  # check

        # [条件不符合，不执行]前置
        pvr.setR(1, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1
        pvr.setR(2, 2.2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2.2
        pvr.setR(71, 0)
        time.sleep(0.5)
        assert pvr.getR(71, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(71, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(71, 1)[1][0] == 0  # check

    def test_冒烟57(self,prg='OrderSet/循环指令/WHILE51.PRG'):
        """
        R[] OR R[]，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合。执行]前置
        pvr.setR(1, 1.5)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1.5
        pvr.setR(2, 2.2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2.2
        pvr.setR(72, 0)
        time.sleep(0.5)
        assert pvr.getR(72, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(72, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(72, 1)[1][0] >= 10  # check

        # [条件不符合。不执行]前置
        pvr.setR(1, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1
        pvr.setR(2, 2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2
        pvr.setR(72, 0)
        time.sleep(0.5)
        assert pvr.getR(72, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(72, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(72, 1)[1][0] == 0  # check

    def test_冒烟58(self,prg='OrderSet/循环指令/WHILE52.PRG'):
        """
        not and not，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，不执行]前置
        pvr.setR(1, 1.5)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1.5
        pvr.setR(2, 2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2
        pvr.setR(73, 0)
        time.sleep(0.5)
        assert pvr.getR(73, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(73, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(73, 1)[1][0] == 0  # check

        # [条件不符合，执行]前置
        pvr.setR(1, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1
        pvr.setR(2, 2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2
        pvr.setR(73, 0)
        time.sleep(0.5)
        assert pvr.getR(73, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(73, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(73, 1)[1][0] >= 10  # check

    def test_冒烟59(self,prg='OrderSet/循环指令/WHILE53.PRG'):
        """
        not and ..，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，执行]前置
        pvr.setR(1, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1
        pvr.setR(2, 2.2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2.2
        pvr.setR(74, 0)
        time.sleep(0.5)
        assert pvr.getR(74, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(74, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(74, 1)[1][0] >= 10  # check

        # [条件不符合，不执行]前置
        pvr.setR(1, 1.5)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1.5
        pvr.setR(2, 2.2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2.2
        pvr.setR(74, 0)
        time.sleep(0.5)
        assert pvr.getR(74, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(74, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(74, 1)[1][0] == 0  # check

    def test_冒烟60(self,prg='OrderSet/循环指令/WHILE54.PRG'):
        """
        not or not，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，不执行]前置
        pvr.setR(1, 1.5)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1.5
        pvr.setR(2, 2.2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2.2
        pvr.setR(75, 0)
        time.sleep(0.5)
        assert pvr.getR(75, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(75, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(75, 1)[1][0] == 0  # check

        # [条件不符合，执行]前置
        pvr.setR(1, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1
        pvr.setR(2, 2.2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2.2
        pvr.setR(75, 0)
        time.sleep(0.5)
        assert pvr.getR(75, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(75, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(75, 1)[1][0] >= 10  # check

    def test_冒烟61(self, prg='OrderSet/循环指令/WHILE55.PRG'):
        """
        not or .。，验证while符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，不执行]前置
        pvr.setR(1, 1.5)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1.5
        pvr.setR(2, 2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2
        pvr.setR(76, 0)
        time.sleep(0.5)
        assert pvr.getR(76, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(76, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(76, 1)[1][0] == 0  # check

        # [条件不符合，执行]前置
        pvr.setR(1, 1)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1
        pvr.setR(2, 2)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 2
        pvr.setR(76, 0)
        time.sleep(0.5)
        assert pvr.getR(76, 1)[1][0] == 0

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            while pvr.getR(76, 1)[1][0] >= 10:
                pvm.pause(prg)
                time.sleep(1)
                break
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_PAUSED
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(76, 1)[1][0] >= 10  # check


class Test_break:
    def test_冒烟01(self,prg='OrderSet/循环指令/BREAK01.PRG'):
        """
        break
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(1, 1.5)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1.5
        pvr.setR(2, 0)
        time.sleep(0.5)
        assert pvr.getR(2, 1)[1][0] == 0
        pvr.setR(80, 0)
        time.sleep(0.5)
        assert pvr.getR(80, 1)[1][0] == 0

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
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(80, 1)[1][0] == 1  # check
        assert pvr.getR(2, 1)[1][0] == 0
