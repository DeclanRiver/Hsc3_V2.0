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


class Test_printf:
    def test_冒烟0(self,prg='OrderSet/其他指令/PRINTF00.PRG'):
        """
        输出一条，内容为空，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 100)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        assert '自定义消息 100.000' in msg[3]

    def test_冒烟1(self,prg='OrderSet/其他指令/PRINTF01.PRG'):
        """
        输出一条，单个汉字，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 100)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        assert '自定义消息 爸100.000' in msg[3]

    def test_冒烟2(self,prg='OrderSet/其他指令/PRINTF02.PRG'):
        """
        输出一条，单个数字，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 100)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        assert '自定义消息 1100.000' in msg[3]

    def test_冒烟3(self,prg='OrderSet/其他指令/PRINTF03.PRG'):
        """
        输出一条，单个小写字母，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 100)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        assert '自定义消息 a100.000' in msg[3]

    def test_冒烟4(self,prg='OrderSet/其他指令/PRINTF04.PRG'):
        """
        输出一条，单个大写字母，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 100)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        assert '自定义消息 A100.000' in msg[3]

    def test_冒烟5(self,prg='OrderSet/其他指令/PRINTF05.PRG'):
        """
        输出一条，单个中式标点，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 100)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        assert '自定义消息 ，100.000' in msg[3]

    def test_冒烟6(self,prg='OrderSet/其他指令/PRINTF06.PRG'):
        """
        输出一条，单个英式标点，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 100)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        assert '自定义消息 ,100.000' in msg[3]

    def test_冒烟7(self,prg='OrderSet/其他指令/PRINTF07.PRG'):
        """
        输出一条，单个空格，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        pvr.setR(1, 100)
        time.sleep(0.5)
        assert pvr.getR(1, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        assert '自定义消息  100.000' in msg[3]

    def test_冒烟8(self,prg='OrderSet/其他指令/PRINTF08.PRG'):
        """
        输出10条，内容均为空，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(1, 11):
            pvr.setR(i, 100)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        text = '自定义消息 100.000;  100.000;  100.000;  100.000;  100.000;  100.000;  100.000;  100.000;  100.000;  100.000'
        assert text in msg[3]

    def test_冒烟9(self,prg='OrderSet/其他指令/PRINTF09.PRG'):
        """
        输出10条，每条内容均为最长50个汉字字符，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(11):
            pvr.setR(i, 100)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        text = '自定义消息 哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈呵呵呵呵呵呵呵呵呵呵嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻100.000'
        assert text in msg[3]

    def test_冒烟10(self,prg='OrderSet/其他指令/PRINTF10.PRG'):
        """
        输出10条，每条均为最长50个数字字符，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(11):
            pvr.setR(i, 100)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        text = '自定义消息 11111111112222222222333333333344444444445555555555100.000;  ' \
               '11111111112222222222333333333344444444445555555555100.000;  ' \
               '11111111112222222222333333333344444444445555555555100.000;  ' \
               '11111111112222222222333333333344444444445555555555100.000;  ' \
               '11111111112222222222333333333344444444445555555555100.000;  ' \
               '11111111112222222222333333333344444444445555555555100.000;  ' \
               '11111111112222222222333333333344444444445555555555100.000;  ' \
               '11111111112222222222333333333344444444445555555555100.000;  ' \
               '11111111112222222222333333333344444444445555555555100.000;  ' \
               '11111111112222222222333333333344444444445555555555100.000'
        assert text in msg[3]

    def test_冒烟11(self,prg='OrderSet/其他指令/PRINTF11.PRG'):
        """
        输出10条，每条均为最长50个小写字母字符，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(11):
            pvr.setR(i, 100)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        text = '自定义消息 aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000;  ' \
               'aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000;  ' \
               'aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000;  ' \
               'aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000;  ' \
               'aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000;  ' \
               'aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000;  ' \
               'aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000;  ' \
               'aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000;  ' \
               'aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000;  ' \
               'aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee100.000'
        assert text in msg[3]

    def test_冒烟12(self,prg='OrderSet/其他指令/PRINTF12.PRG'):
        """
        输出10条，每条均为最长50个大写字母字符，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(11):
            pvr.setR(i, 100)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        text = '自定义消息 AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000;  ' \
               'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000;  ' \
               'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000;  ' \
               'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000;  ' \
               'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000;  ' \
               'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000;  ' \
               'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000;  ' \
               'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000;  ' \
               'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000;  ' \
               'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE100.000'
        assert text in msg[3]

    def test_冒烟13(self,prg='OrderSet/其他指令/PRINTF13.PRG'):
        """
        输出10条，每条均为最长50个中英式标点+空格字符组合，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(11):
            pvr.setR(i, 100)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        text = '自定义消息 ，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000;  ' \
               '，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000;  ' \
               '，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000;  ' \
               '，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000;  ' \
               '，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000;  ' \
               '，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000;  ' \
               '，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000;  ' \
               '，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000;  ' \
               '，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000;  ' \
               '，，，，，，.......       。；！@#￥%……&,./!@#$%^&*（）()-=+_]100.000'
        assert text in msg[3]

    def test_冒烟14(self,prg='OrderSet/其他指令/PRINTF14.PRG'):
        """
        输出10条，每条均为最长50个汉字、数字、大小写字母、中英式标点+空格字符组合，验证PRINTF执行结果
        :param prg:主程序
        :return:NONE
        """
        # 前置
        for i in range(11):
            pvr.setR(i, 100)
            time.sleep(0.5)
            assert pvr.getR(i, 1)[1][0] == 100

        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        assert not pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_FAULT
        assert pvm.progState(prg)[1] == Hsc3ApiPy.AUTO_STATE_READY
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_NOTE
        text = '自定义消息 哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000;  ' \
               '哈哈哈哈哈哈哈哈哈哈1111111111aBaBaBaBaBaBaBaBaBaB,./，。、  ?!100.000'
        assert text in msg[3]

