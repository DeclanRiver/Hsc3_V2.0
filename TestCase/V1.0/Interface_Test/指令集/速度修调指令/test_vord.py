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


class Test_vord:
    def test_冒烟01(self,prg='OrderSet/倍率修调指令/VORD01.PRG'):
        """
        手动T1模式，VORD赋值成功，手动和自动模式倍率相互独立
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pMot.setJogVord(50)
        time.sleep(0.5)
        assert pMot.getJogVord()[1] == 50
        pMot.setVord(50)
        time.sleep(0.5)
        assert pMot.getVord()[1] == 50
        pMot.setOpMode(opMode=Hsc3ApiPy.OpMode.OP_T1)
        time.sleep(0.5)
        assert pMot.getOpMode()[1] == Hsc3ApiPy.OpMode.OP_T1

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pMot.getJogVord()[1] == 90  # check
        assert pMot.getVord()[1] == 50

    def test_冒烟02(self,prg='OrderSet/倍率修调指令/VORD01.PRG'):
        """
        手动T2模式，VORD赋值成功，手动和自动模式倍率相互独立
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pMot.setJogVord(50)
        time.sleep(0.5)
        assert pMot.getJogVord()[1] == 50
        pMot.setVord(50)
        time.sleep(0.5)
        assert pMot.getVord()[1] == 50
        pMot.setOpMode(opMode=Hsc3ApiPy.OpMode.OP_T2)
        time.sleep(0.5)
        assert pMot.getOpMode()[1] == Hsc3ApiPy.OpMode.OP_T2

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pMot.getJogVord()[1] == 90  # check
        assert pMot.getVord()[1] == 50

    def test_冒烟03(self,prg='OrderSet/倍率修调指令/VORD01.PRG'):
        """
        自动模式，VORD赋值成功，手动和自动模式倍率相互独立
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pMot.setJogVord(50)
        time.sleep(0.5)
        assert pMot.getJogVord()[1] == 50
        pMot.setVord(50)
        time.sleep(0.5)
        assert pMot.getVord()[1] == 50
        pMot.setOpMode(opMode=Hsc3ApiPy.OpMode.OP_AUT)
        time.sleep(0.5)
        assert pMot.getOpMode()[1] == Hsc3ApiPy.OpMode.OP_AUT

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pMot.getJogVord()[1] == 50  # check
        assert pMot.getVord()[1] == 90

    def test_冒烟04(self, prg='OrderSet/倍率修调指令/VORD01.PRG'):
        """
        外部模式，VORD赋值成功，手动和自动模式倍率相互独立
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pMot.setJogVord(50)
        time.sleep(0.5)
        assert pMot.getJogVord()[1] == 50
        pMot.setVord(50)
        time.sleep(0.5)
        assert pMot.getVord()[1] == 50
        pMot.setOpMode(opMode=Hsc3ApiPy.OpMode.OP_EXT)
        time.sleep(0.5)
        assert pMot.getOpMode()[1] == Hsc3ApiPy.OpMode.OP_EXT

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pMot.getJogVord()[1] == 50  # check
        assert pMot.getVord()[1] == 90

    def test_冒烟05(self, prg='OrderSet/倍率修调指令/VORD02.PRG'):
        """
        vord R[] 手动模式
        :param prg: 主程序
        :return: NONE
        """
        # 前置
        pMot.setJogVord(50)
        time.sleep(0.5)
        assert pMot.getJogVord()[1] == 50
        pMot.setVord(50)
        time.sleep(0.5)
        assert pMot.getVord()[1] == 50
        pMot.setOpMode(opMode=Hsc3ApiPy.OpMode.OP_T1)
        time.sleep(0.5)
        assert pMot.getOpMode()[1] == Hsc3ApiPy.OpMode.OP_T1
        pvr.setR(0, 80)
        time.sleep(0.5)
        assert pvr.getR(0, 1)[1][0] == 80

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        time.sleep(0.2)
        while not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert pMot.getJogVord()[1] == 80  # check
        assert pMot.getVord()[1] == 50