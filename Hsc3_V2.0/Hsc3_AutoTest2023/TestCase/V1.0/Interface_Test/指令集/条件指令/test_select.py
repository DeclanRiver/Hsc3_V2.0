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


class Test_select:
    def test_冒烟0(self,prg='OrderSet/条件指令/SELECT0.PRG'):
        """
        case lbl，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(3):
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
        assert pvr.getR(1, 2)[1] == [0, 1]  # check

    def test_冒烟1(self,prg='OrderSet/条件指令/SELECT1.PRG'):
        """
        case call，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 100)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 100
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
        assert pvr.getR(10, 1)[1][0] == 10  # check

    def test_冒烟2(self,prg='OrderSet/条件指令/SELECT2.PRG'):
        """
        case lbl*10，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(1, 11):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
        pvr.setR(0, 108)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 108

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
        assert pvr.getR(9, 1)[1][0] == 1  # check
        assert pvr.getR(10, 1)[1][0] == 1
        for i in range(1, 9):
            assert pvr.getR(i, 1)[1][0] == 0

    def test_冒烟3(self,prg='OrderSet/条件指令/SELECT3.PRG'):
        """
        case call*10，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(10, 12):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
        pvr.setR(0, 105)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 105

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
        assert pvr.getR(10, 2)[1] == [0, 11]  # check

    def test_冒烟4(self,prg='OrderSet/条件指令/SELECT4.PRG'):
        """
        (case lbl+case call)*5，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(1, 6):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
        pvr.setR(0, 109)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 109
        for i in range(10, 12):
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
        assert pvr.getR(10, 2)[1] == [0, 11]  # check
        for i in range(1, 6):
            assert pvr.getR(1, 5)[1] == [0, 0, 0, 0, 0]

    def test_冒烟5(self,prg='OrderSet/条件指令/SELECT5.PRG'):
        """
        case lbl else lbl，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(3):
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
        assert pvr.getR(1, 2)[1] == [0, 1]  # check

    def test_冒烟6(self,prg='OrderSet/条件指令/SELECT6.PRG'):
        """
        case lbl else call，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(2):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
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
        assert pvr.getR(10, 1)[1][0] == 10  # check
        assert pvr.getR(1, 1)[1][0] == 1

    def test_冒烟7(self,prg='OrderSet/条件指令/SELECT7.PRG'):
        """
        case call else lbl，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(1):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check
        assert pvr.getR(10, 1)[1][0] == 0

    def test_冒烟8(self,prg='OrderSet/条件指令/SELECT8.PRG'):
        """
        case call else call，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(10, 12):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
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
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(10, 2)[1] == [0, 11] # check

    def test_冒烟9(self,prg='OrderSet/条件指令/SELECT9.PRG'):
        """
        select R[R[]]，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(10, 0)
        time.sleep(0.5)
        assert pvr.getR(10, 1)[1][0] == 0
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
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pvr.getR(10, 1)[1][0] == 10  # check

    def test_冒烟10(self,prg='OrderSet/条件指令/SELECT10.PRG'):
        """
        条件不符合，验证SELECT符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(10, 0)
        time.sleep(0.5)
        assert pvr.getR(10, 1)[1][0] == 0
        pvr.setR(1, 1.3)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 1.3

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
        assert pvr.getR(10, 1)[1][0] == 0  # check
