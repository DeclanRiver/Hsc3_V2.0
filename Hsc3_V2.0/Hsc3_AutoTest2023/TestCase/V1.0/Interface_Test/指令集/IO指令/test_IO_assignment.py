# !/usr/bin/env python3
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
from HSC3Api import ProxySys
comm = CommApi.CommApi('')
pvm = ProxyVm.ProxyVm(comm)
pMot = ProxyMotion.ProxyMotion(comm)
pio = ProxyIO.ProxyIO(comm)
pvr = ProxyVar.ProxyVar(comm)
psy = ProxySys.ProxySys(comm)
comm.connect('10.10.56.214', 23234)
time.sleep(1)
assert comm.isConnected()


class Test_io:
    def test_冒烟01(self, prg='OrderSet/IO赋值指令/DO_ON.PRG'):
        """
        主程序DO赋值全为ON
        :param prg: 主程序
        :return: NONE
        """
        pvm.load('./', prg)
        time.sleep(5)
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
        if 'HSC3' in psy.getVersion('Release')[1]:  # IPC版本
            for i in range(200):  # 验证DO赋值ON
                assert comm.execCmd('io.getDout(%d)' % i, 5)[1] == '"true"'
            for i in range(200, 206):  # 验证DO赋值ON
                assert comm.execCmd('io.getDout(%d)' % i, 5)[1] == '"false"'
            for i in range(206, 512):
                assert comm.execCmd('io.getDout(%d)' % i, 5)[1] == '"true"'
        if 'HSI' in psy.getVersion('Release')[1]:  # 驱控一体版本（没下工程）
            for i in range(512):  # 验证DO赋值ON
                assert comm.execCmd('io.getDout(%d)' % i, 5)[1] == '"true"'

    def test_冒烟02(self, prg='OrderSet/IO赋值指令/DO_OFF.PRG'):
        """
        主程序DO赋值全为OFF
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
        for i in range(512):  # 验证DO赋值OFF
            assert comm.execCmd('io.getDout(%d)' % i, 5)[1] == '"false"'

    def test_冒烟03(self, prg='OrderSet/IO赋值指令/DIO1.PRG'):
        """
        主程序内置DO=DO[x]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDout(2, 0)
        time.sleep(0.5)
        pio.setDout(3, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(2)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDout(3)', 5)[1] == '"true"'

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
        assert comm.execCmd('io.getDout(2)', 5)[1] == '"true"'  # 验证DO=DO[X]赋值
        assert comm.execCmd('io.getDout(3)', 5)[1] == '"false"'

    def test_冒烟04(self, prg='OrderSet/IO赋值指令/DIO2.PRG'):
        """
        验证DO[R[X]]=ON/OFF
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDout(4, 0)
        time.sleep(0.5)
        pio.setDout(5, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(4)', 5)[1] == '"false"'
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
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert comm.execCmd('io.getDout(4)', 5)[1] == '"true"'  # 验证赋值
        assert comm.execCmd('io.getDout(5)', 5)[1] == '"false"'

    def test_冒烟05(self, prg='OrderSet/IO赋值指令/DIO3.PRG'):
        """
        验证DO[R[X]]=DO[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDout(7, 0)
        time.sleep(0.5)
        pio.setDout(11, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(7)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDout(11)', 5)[1] == '"true"'

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
        assert comm.execCmd('io.getDout(7)', 5)[1] == '"true"'  # 验证赋值
        assert comm.execCmd('io.getDout(11)', 5)[1] == '"false"'

    def test_冒烟06(self, prg='OrderSet/IO赋值指令/DIO4.PRG'):
        """
        验证DO[]=DI[X]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDin(500, 1)
        time.sleep(0.5)
        pio.setDin(501, 0)
        time.sleep(0.5)
        pio.setDout(8, 0)
        time.sleep(0.5)
        pio.setDout(9, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(8)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDout(9)', 5)[1] == '"true"'
        assert comm.execCmd('io.getDin(500)', 5)[1] == '"true"'
        assert comm.execCmd('io.getDout(501)', 5)[1] == '"false"'

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
        assert comm.execCmd('io.getDout(8)', 5)[1] == '"true"'  # 验证赋值
        assert comm.execCmd('io.getDout(9)', 5)[1] == '"false"'

    def test_冒烟07(self, prg='OrderSet/IO赋值指令/DIO5.PRG'):
        """
        验证DO[R[X]]=DI[R[X]]
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDin(502, 1)
        time.sleep(0.5)
        pio.setDin(503, 0)
        time.sleep(0.5)
        pio.setDout(15, 0)
        time.sleep(0.5)
        pio.setDout(16, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(15)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDout(16)', 5)[1] == '"true"'
        assert comm.execCmd('io.getDin(502)', 5)[1] == '"true"'
        assert comm.execCmd('io.getDout(503)', 5)[1] == '"false"'

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
        assert comm.execCmd('io.getDout(15)', 5)[1] == '"true"'  # 验证赋值
        assert comm.execCmd('io.getDout(16)', 5)[1] == '"false"'

    def test_冒烟08(self, prg='OrderSet/IO赋值指令/DIO6.PRG'):
        """
        验证DO[]=1/0
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDout(20, 0)
        time.sleep(0.5)
        pio.setDout(21, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(20)', 5)[1] == '"false"'
        assert comm.execCmd('io.getDout(21)', 5)[1] == '"true"'

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
        assert comm.execCmd('io.getDout(20)', 5)[1] == '"true"'  # 验证赋值
        assert comm.execCmd('io.getDout(21)', 5)[1] == '"false"'

    def test_冒烟09(self, prg='OrderSet/IO赋值指令/DIO7.PRG'):
        """
        验证DO[]=R[X],R[X]=1/0
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pio.setDout(25, 1)
        time.sleep(0.5)
        pio.setDout(26, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(25)', 5)[1] == '"true"'
        assert comm.execCmd('io.getDout(26)', 5)[1] == '"false"'

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
        assert comm.execCmd('io.getDout(25)', 5)[1] == '"false"'  # 验证赋值
        assert comm.execCmd('io.getDout(26)', 5)[1] == '"true"'

