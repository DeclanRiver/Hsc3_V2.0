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


# 脉冲输出周期监控放宽到±30ms
class Test_pulse:
    def test_冒烟01(self,prg='OrderSet/输出脉冲指令/PULSE01.PRG'):
        """
        DO[],原DO置OFF 计时1s
        :param prg:主程序
        :return:NONE
        """
        # 前置
        b = 0
        pio.setDout(1, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(1)', 5)[1] == '"false"'

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        a = time.time()  # start check
        while comm.execCmd('io.getDout(1)', 5)[1] == '"true"':
            b = time.time()
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        c = b-a
        assert 0.97 <= c <= 1.03  # check

    def test_冒烟02(self,prg='OrderSet/输出脉冲指令/PULSE01.PRG'):
        """
        DO[],原DO置ON 计时1s
        :param prg:主程序
        :return:NONE
        """
        # 前置
        b = 0
        pio.setDout(1, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(1)', 5)[1] == '"true"'

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        a = time.time()  # start check
        while comm.execCmd('io.getDout(1)', 5)[1] == '"true"':
            b = time.time()
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        c = b-a
        assert 0.970 <= c <= 1.03  # check

    def test_冒烟03(self, prg='OrderSet/输出脉冲指令/PULSE02.PRG'):
        """
        DO[],原DO置OFF 计时0.1s
        :param prg:主程序
        :return:NONE
        """
        # 前置
        b = 0
        pio.setDout(1, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(1)', 5)[1] == '"false"'

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        a = time.time()  # start check
        while comm.execCmd('io.getDout(1)', 5)[1] == '"true"':
            b = time.time()
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        c = b-a
        assert 0.07 <= c <= 0.103  # check

    def test_冒烟04(self, prg='OrderSet/输出脉冲指令/PULSE03.PRG'):
        """
        DO[],原DO置ON 计时25500ms
        :param prg:主程序
        :return:NONE
        """
        # 前置
        b = 0
        pio.setDout(1, 1)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(1)', 5)[1] == '"true"'

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        a = time.time()  # start check
        while comm.execCmd('io.getDout(1)', 5)[1] == '"true"':
            b = time.time()
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        c = b-a
        assert 25.470 <= c <= 25.530  # check

    def test_冒烟05(self, prg='OrderSet/输出脉冲指令/PULSE04.PRG'):
        """
        DO[R[]],原DO置OFF 计时555ms
        :param prg:主程序
        :return:NONE
        """
        # 前置
        b = 0
        pvr.setR(0, 1)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 1
        pio.setDout(1, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(1)', 5)[1] == '"false"'

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        a = time.time()  # start check
        while comm.execCmd('io.getDout(1)', 5)[1] == '"true"':
            b = time.time()
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        c = b-a
        assert 0.525 <= c <= 0.585  # check

    def test_冒烟06(self, prg='OrderSet/输出脉冲指令/PULSE03.PRG'):
        """
        中途卸载程序，脉冲被中断
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pio.setDout(1, 0)
        time.sleep(0.5)
        assert comm.execCmd('io.getDout(1)', 5)[1] == '"false"'

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.02)
        while comm.execCmd('io.getDout(1)', 5)[1] == '"true"':  # start check
            pvm.unload(prg)
        time.sleep(0.1)
        assert comm.execCmd('io.getDout(1)', 5)[1] == '"false"'  # check
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        assert not pvm.mainProgNames()[1]
