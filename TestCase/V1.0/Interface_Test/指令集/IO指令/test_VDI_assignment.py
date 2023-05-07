# !usr/bin/env python3
# encoding=utf-8
"""
@author:少华
"""
import time
from HSC3Api import Hsc3ApiPy
from HSC3Api import CommApi
from HSC3Api import ProxyVm
from HSC3Api import ProxyMotion
from HSC3Api import ProxyIO
from HSC3Api import ProxyVar
comm = CommApi.CommApi('')
pvm = ProxyVm.ProxyVm(comm)
pMot = ProxyMotion.ProxyMotion(comm)
pio = ProxyIO.ProxyIO(comm)
pvr = ProxyVar.ProxyVar(comm)
comm.connect('10.10.56.214', 23234)
time.sleep(1)
assert comm.isConnected()


class Test_vdi:
    def test_冒烟01(self, prg='OrderSet/IO赋值指令/VDI_ON.PRG'):
        """
        主程序内置VDI置ON指令
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
        for i in range(512):  # 检查VDI赋值
            assert comm.execCmd('io.getDin(%d)' % i, 5)[1] == '"true"'

    def test_冒烟02(self, prg='OrderSet/IO赋值指令/VDI_OFF.PRG'):
        """
        主程序内置VDI置OFF指令
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
        for i in range(512):  # 检查VDI赋值
            assert comm.execCmd('io.getDin(%d)' % i, 5)[1] == '"false"'

    def test_冒烟03(self, prg='OrderSet/IO赋值指令/VDI1.PRG'):
        """
        VDI=DI[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDin(402, 0)
        time.sleep(0.5)
        pio.setDin(403, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(402)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDin(403)', 5)[1] == '"true"'

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
        assert comm.execCmd('io.getDin(402)', 5)[1] == '"true"'  # 检查赋值
        assert comm.execCmd('io.getDin(403)', 5)[1] == '"false"'

    def test_冒烟04(self, prg='OrderSet/IO赋值指令/VDI2.PRG'):
        """
        VDI=DI[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDout(11, 0)
        time.sleep(0.5)
        pio.setDout(10, 1)
        time.sleep(0.5)
        pio.setDin(404, 0)
        time.sleep(0.5)
        pio.setDin(405, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(404)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDin(405)', 5)[1] == '"true"'

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
        assert comm.execCmd('io.getDin(404)', 5)[1] == '"true"'  # 检查赋值
        assert comm.execCmd('io.getDin(405)', 5)[1] == '"false"'

    def test_冒烟05(self, prg='OrderSet/IO赋值指令/VDI3.PRG'):
        """
        VDI[R[X]]=DI[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 406)
        pvr.setR(1, 407)
        pvr.setR(2, 408)
        pvr.setR(3, 409)
        pio.setDin(406, 1)
        pio.setDin(408, 0)
        pio.setDin(407, 0)
        pio.setDin(409, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(407)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDin(409)', 5)[1] == '"true"'

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
        assert comm.execCmd('io.getDin(407)', 5)[1] == '"true"'  # 检查赋值
        assert comm.execCmd('io.getDin(409)', 5)[1] == '"false"'

    def test_冒烟06(self, prg='OrderSet/IO赋值指令/VDI4.PRG'):
        """
        VDI[R[X]]=DO[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pvr.setR(0, 410)
        pvr.setR(1, 411)
        pvr.setR(2, 412)
        pvr.setR(3, 413)
        pio.setDout(410, 1)
        pio.setDout(412, 0)
        pio.setDin(411, 0)
        pio.setDin(413, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(411)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDin(413)', 5)[1] == '"true"'

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
        assert comm.execCmd('io.getDin(411)', 5)[1] == '"true"'  # 检查赋值
        assert comm.execCmd('io.getDin(413)', 5)[1] == '"false"'

    def test_冒烟07(self, prg='OrderSet/IO赋值指令/VDI5.PRG'):
        """
        VDI[X]=1/0
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDin(415, 0)
        time.sleep(0.5)
        pio.setDin(416, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDin(415)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDin(416)', 5)[1] == '"true"'

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
        assert comm.execCmd('io.getDin(415)', 5)[1] == '"true"'  # 检查赋值
        assert comm.execCmd('io.getDin(416)', 5)[1] == '"false"'


