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


class Test_end:
    def test_冒烟01(self, prg='程序控制指令/END01.PRG'):
        """
        end在主程序内生效，主程序结束运行，end后面的指令不再执行
        :param prg: 主程序
        :return: NONE
        """
        # 前置R[0]=0
        pvr.setR(0, 1)
        time.sleep(0.2)
        assert pvr.getR(0, 1)[1][0] == 1

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        comm.execCmd('vm.startAll()', 5)
        time.sleep(0.2)
        while pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_RUNNING:
            time.sleep(1)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY  # 执行end指令后程序就绪状态
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        assert pvr.getR(0, 1)[1][0] == 1  # 执行end后指令不再执行


