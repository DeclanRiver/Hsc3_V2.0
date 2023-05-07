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


class Test_if:
    def test_冒烟0(self,prg='条件指令/IF0.PRG'):
        """
        R[0]=R[0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(2):
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟1(self,prg='条件指令/IF1.PRG'):
        """
        R[0]=JR[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(2):
            pvr.setR(i, 101)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 101
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [101, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[0] == 101

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

    def test_冒烟2(self,prg='条件指令/IF2.PRG'):
        """
        R[0]=LR[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(2):
            pvr.setR(i, 20)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 20
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [20, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[0] == 20

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

    def test_冒烟3(self,prg='条件指令/IF3.PRG'):
        """
        R[0]=P[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(2):
            pvr.setR(i, -4.53)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == -4.53

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

    def test_冒烟4(self,prg='条件指令/IF4.PRG'):
        """
        JR[0][0]=R[0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(2):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[0] == 0

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

    def test_冒烟5(self,prg='条件指令/IF5.PRG'):
        """
        JR[0][0]=JR[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [101, 101, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[:2] == [101, 101]
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟6(self,prg='条件指令/IF6.PRG'):
        """
        JR[0][0]=LR[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [234, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[0] == 234
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [234, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[0] == 234

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

    def test_冒烟7(self,prg='条件指令/IF7.PRG'):
        """
        JR[0][0]=P[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [-4.53, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[0] == -4.53

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

    def test_冒烟8(self,prg='条件指令/IF8.PRG'):
        """
        LR[0][0]=R[0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(2):
            pvr.setR(i, 0)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[0] == 0

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

    def test_冒烟9(self,prg='条件指令/IF9.PRG'):
        """
        LR[0][0]=JR[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [333, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[0] == 333
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [333, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[0] == 333

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

    def test_冒烟10(self,prg='条件指令/IF10.PRG'):
        """
        LR[0][0]=LR[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [333, 333, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[:2] == [333, 333]

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

    def test_冒烟11(self,prg='条件指令/IF11.PRG'):
        """
        LR[0][0]=P[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [-4.53, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[0] == -4.53

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

    def test_冒烟12(self,prg='条件指令/IF12.PRG'):
        """
        P[0][0]=R[0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(2):
            pvr.setR(i, 178.444)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 178.444

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

    def test_冒烟13(self,prg='条件指令/IF13.PRG'):
        """
        P[0][0]=JR[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [77.042, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[0] == 77.042

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

    def test_冒烟14(self,prg='条件指令/IF14.PRG'):
        """
        P[0][0]=LR[0][0]，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [-4.53, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[0] == -4.53

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

    def test_冒烟15(self,prg='条件指令/IF15.PRG'):
        """
        P[0][0]=P[0][0]，验证IF符合时执行结果
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟16(self,prg='条件指令/IF16.PRG'):
        """
        R[0]=X，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        pvr.setR(0, 35)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 35

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

    def test_冒烟17(self,prg='条件指令/IF17.PRG'):
        """
        JR[0][0]=X，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        jPos = Hsc3ApiPy.JntPos()
        jPos.vecPos = [35, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setJR(0, 0, jPos)
        assert pvr.getJR(0, 0, 1)[1].vecPos[0] == 35

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

    def test_冒烟18(self,prg='条件指令/IF18.PRG'):
        """
        LR[0][0]=X，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 0)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 0
        lPos = Hsc3ApiPy.LocPos()
        lPos.ufNum = 0
        lPos.utNum = 0
        lPos.config = 0
        lPos.vecPos = [35, 0, 0, 0, 0, 0, 0, 0, 0]
        pvr.setLR(0, 0, lPos)
        assert pvr.getLR(0, 0, 1)[1].vecPos[0] == 35

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

    def test_冒烟19(self,prg='条件指令/IF19.PRG'):
        """
        P[0][0]=X，验证IF符合时执行结果
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟20(self,prg='条件指令/IF20.PRG'):
        """
        DIV，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 2)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 2
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟21(self,prg='条件指令/IF21.PRG'):
        """
        MOD，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 100)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 100
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟22(self,prg='条件指令/IF22.PRG'):
        """
        SQRT，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 30)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 30
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟23(self,prg='条件指令/IF23.PRG'):
        """
        SIN，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟24(self,prg='条件指令/IF24.PRG'):
        """
        COS，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 0.5)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0.5
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟25(self,prg='条件指令/IF25.PRG'):
        """
        TAN，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 1)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 1
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟26(self,prg='条件指令/IF26.PRG'):
        """
        ASIN，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 30)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 30
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟27(self,prg='条件指令/IF27.PRG'):
        """
        ACOS，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟28(self,prg='条件指令/IF28.PRG'):
        """
        ATAN，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟29(self,prg='条件指令/IF29.PRG'):
        """
        ABS，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 67)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 67
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟30(self,prg='条件指令/IF30.PRG'):
        """
        TRUNC，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 89)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 89
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟31(self,prg='条件指令/IF31.PRG'):
        """
        ROUND，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 90)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 90
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟32(self,prg='条件指令/IF32.PRG'):
        """
        +，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 70)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 70
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟33(self,prg='条件指令/IF33.PRG'):
        """
        -，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 95)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 95
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟34(self,prg='条件指令/IF34.PRG'):
        """
        *，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 400)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 400
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟35(self,prg='条件指令/IF35.PRG'):
        """
        /，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟36(self,prg='条件指令/IF36.PRG'):
        """
        ()，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 40)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 40
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟37(self,prg='条件指令/IF37.PRG'):
        """
        DI[500]=ON，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pio.setDin(500, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(500)', 5)[1] == '"true"'
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟38(self,prg='条件指令/IF38.PRG'):
        """
        DI[500]=OFF，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pio.setDin(500, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(500)', 5)[1] == '"false"'
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟39(self,prg='条件指令/IF39.PRG'):
        """
        DO[500]=ON，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pio.setDout(500, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(500)', 5)[1] == '"true"'
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟40(self,prg='条件指令/IF40.PRG'):
        """
        DO[500]=OFF，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pio.setDout(500, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(500)', 5)[1] == '"false"'
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟41(self,prg='条件指令/IF41.PRG'):
        """
        >，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 11)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 11
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟42(self,prg='条件指令/IF42.PRG'):
        """
        >=，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟43(self,prg='条件指令/IF43.PRG'):
        """
        <，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟44(self,prg='条件指令/IF44.PRG'):
        """
        <=，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟45(self,prg='条件指令/IF45.PRG'):
        """
        <>，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 10.9)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10.9
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

    def test_冒烟46(self,prg='条件指令/IF46.PRG'):
        """
        not..，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，执行]前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

        # [条件不符合，不执行]前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟47(self,prg='条件指令/IF47.PRG'):
        """
        ..and..，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，执行]前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

        # [条件不符合，不执行]前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟48(self,prg='条件指令/IF48.PRG'):
        """
        ..or..，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，执行]前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

        # [条件不符合，不执行]前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟49(self,prg='条件指令/IF49.PRG'):
        """
        not..and not..，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，执行]前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

        # [条件不符合，不执行]前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟50(self,prg='条件指令/IF50.PRG'):
        """
        not and ..，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，执行]前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

        # [条件不符合，不执行]前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟51(self,prg='条件指令/IF51.PRG'):
        """
        not..or not..，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，执行]前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

        # [条件不符合，不执行]前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟52(self,prg='条件指令/IF52.PRG'):
        """
        not or ..，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # [条件符合，执行]前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 1  # check

        # [条件不符合，不执行]前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
        pvr.setR(1, 2)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 2

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
        assert pvr.getR(1, 1)[1][0] == 2  # check

    def test_冒烟53(self,prg='条件指令/IF16.PRG'):
        """
        =条件不符合，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟54(self,prg='条件指令/IF42.PRG'):
        """
        >=条件不符合，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟55(self,prg='条件指令/IF43.PRG'):
        """
        <条件不符合，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 111)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 111
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟56(self,prg='条件指令/IF44.PRG'):
        """
        <=条件不符合，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 111)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 111
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟57(self,prg='条件指令/IF45.PRG'):
        """
        <>条件不符合，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 10)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 10
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

    def test_冒烟58(self,prg='条件指令/IF41.PRG'):
        """
        >条件不符合，验证IF符合时执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(0, 0)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 0
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
        assert pvr.getR(1, 1)[1][0] == 0  # check

