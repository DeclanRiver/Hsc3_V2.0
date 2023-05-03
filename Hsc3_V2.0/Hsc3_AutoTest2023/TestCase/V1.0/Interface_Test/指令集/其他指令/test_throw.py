# !usr/bin/env python3
# encoding=utf-8
"""
@author:少华
"""
import time
import pytest
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


class Test_throw:
    def test_冒烟0(self,prg='OrderSet/其他指令/THROW00.PRG'):
        """
        INFO，无内容，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"\\' in msg[3]

    def test_冒烟1(self,prg='OrderSet/其他指令/THROW01.PRG'):
        """
        INFO，单个汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"我\\' in msg[3]

    def test_冒烟2(self,prg='OrderSet/其他指令/THROW02.PRG'):
        """
        INFO，单个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"1\\' in msg[3]

    def test_冒烟3(self,prg='OrderSet/其他指令/THROW03.PRG'):
        """
        INFO,单个小写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"a\\' in msg[3]

    def test_冒烟4(self,prg='OrderSet/其他指令/THROW04.PRG'):
        """
        INFO，单个大写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"A\\' in msg[3]

    def test_冒烟5(self,prg='OrderSet/其他指令/THROW05.PRG'):
        """
        INFO,单个中式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"！\\' in msg[3]

    def test_冒烟6(self,prg='OrderSet/其他指令/THROW06.PRG'):
        """
        INFO，单个英式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"!\\' in msg[3]

    def test_冒烟7(self,prg='OrderSet/其他指令/THROW07.PRG'):
        """
        INFO，单个空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\" \\' in msg[3]

    def test_冒烟8(self,prg='OrderSet/其他指令/THROW08.PRG'):
        """
        INFO，32个最长汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻吼吼吼吼吼吼吼吼吼吼嘿嘿\\' in msg[3]

    def test_冒烟9(self,prg='OrderSet/其他指令/THROW09.PRG'):
        """
        INFO，最长32个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"11111111112222222222333333333366\\' in msg[3]

    def test_冒烟10(self,prg='OrderSet/其他指令/THROW10.PRG'):
        """
        INFO，最长32个大小写字母,验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"UuuuuuuuuuRrrrrrrrrrHhhhhhhhhhOo\\' in msg[3]

    def test_冒烟11(self,prg='OrderSet/其他指令/THROW11.PRG'):
        """
        INFO，最长32个标点符号+空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"!@#$%^&*(_+-,.? ？！@#￥%……&*（）——+：\\' in msg[3]

    def test_冒烟12(self,prg='OrderSet/其他指令/THROW12.PRG'):
        """
        INFO，最长32个混合字符，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_INFO
        assert '自定义消息 \\"asd士大夫ASD123，。、,./   收到JFK的司法会计考\\' in msg[3]

    def test_冒烟13(self,prg='OrderSet/其他指令/THROW13.PRG'):
        """
        NOTE，无内容，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"\\' in msg[3]

    def test_冒烟14(self,prg='OrderSet/其他指令/THROW14.PRG'):
        """
        NOTE，单个汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"我\\' in msg[3]

    def test_冒烟15(self,prg='OrderSet/其他指令/THROW15.PRG'):
        """
        NOTE，单个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"1\\' in msg[3]

    def test_冒烟16(self,prg='OrderSet/其他指令/THROW16.PRG'):
        """
        NOTE,单个小写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"a\\' in msg[3]

    def test_冒烟17(self,prg='OrderSet/其他指令/THROW17.PRG'):
        """
        NOTE，单个大写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"A\\' in msg[3]

    def test_冒烟18(self,prg='OrderSet/其他指令/THROW18.PRG'):
        """
        NOTE,单个中式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"！\\' in msg[3]

    def test_冒烟19(self,prg='OrderSet/其他指令/THROW19.PRG'):
        """
        NOTE，单个英式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"!\\' in msg[3]

    def test_冒烟20(self,prg='OrderSet/其他指令/THROW20.PRG'):
        """
        NOTE，单个空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\" \\' in msg[3]

    def test_冒烟21(self,prg='OrderSet/其他指令/THROW21.PRG'):
        """
        NOTE，32个最长汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻吼吼吼吼吼吼吼吼吼吼嘿嘿\\' in msg[3]

    def test_冒烟22(self,prg='OrderSet/其他指令/THROW22.PRG'):
        """
        NOTE，最长32个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"11111111112222222222333333333366\\' in msg[3]

    def test_冒烟23(self,prg='OrderSet/其他指令/THROW23.PRG'):
        """
        NOTE，最长32个大小写字母,验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"UuuuuuuuuuRrrrrrrrrrHhhhhhhhhhOo\\' in msg[3]

    def test_冒烟24(self,prg='OrderSet/其他指令/THROW24.PRG'):
        """
        NOTE，最长32个标点符号+空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"!@#$%^&*(_+-,.? ？！@#￥%……&*（）——+：\\' in msg[3]

    def test_冒烟25(self,prg='OrderSet/其他指令/THROW25.PRG'):
        """
        NOTE，最长32个混合字符，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert '自定义消息 \\"asd士大夫ASD123，。、,./   收到JFK的司法会计考\\' in msg[3]

    def test_冒烟26(self,prg='OrderSet/其他指令/THROW26.PRG'):
        """
        WARNING，无内容，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"\\' in msg[3]

    def test_冒烟27(self,prg='OrderSet/其他指令/THROW27.PRG'):
        """
        WARNING，单个汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"我\\' in msg[3]

    def test_冒烟28(self,prg='OrderSet/其他指令/THROW28.PRG'):
        """
        WARNING，单个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"1\\' in msg[3]

    def test_冒烟29(self,prg='OrderSet/其他指令/THROW29.PRG'):
        """
        WARNING,单个小写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"a\\' in msg[3]

    def test_冒烟30(self,prg='OrderSet/其他指令/THROW30.PRG'):
        """
        WARNING，单个大写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"A\\' in msg[3]

    def test_冒烟31(self,prg='OrderSet/其他指令/THROW31.PRG'):
        """
        WARNING,单个中式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"！\\' in msg[3]

    def test_冒烟32(self,prg='OrderSet/其他指令/THROW32.PRG'):
        """
        WARNING，单个英式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"!\\' in msg[3]

    def test_冒烟33(self,prg='OrderSet/其他指令/THROW33.PRG'):
        """
        WARNING，单个空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\" \\' in msg[3]

    def test_冒烟34(self,prg='OrderSet/其他指令/THROW34.PRG'):
        """
        WARNING，32个最长汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻吼吼吼吼吼吼吼吼吼吼嘿嘿\\' in msg[3]

    def test_冒烟35(self,prg='OrderSet/其他指令/THROW35.PRG'):
        """
        WARNING，最长32个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"11111111112222222222333333333366\\' in msg[3]

    def test_冒烟36(self,prg='OrderSet/其他指令/THROW36.PRG'):
        """
        WARNING，最长32个大小写字母,验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"UuuuuuuuuuRrrrrrrrrrHhhhhhhhhhOo\\' in msg[3]

    def test_冒烟37(self,prg='OrderSet/其他指令/THROW37.PRG'):
        """
        WARNING，最长32个标点符号+空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"!@#$%^&*(_+-,.? ？！@#￥%……&*（）——+：\\' in msg[3]

    def test_冒烟38(self,prg='OrderSet/其他指令/THROW38.PRG'):
        """
        WARNING，最长32个混合字符，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
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
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_WARNING
        assert '自定义消息 \\"asd士大夫ASD123，。、,./   收到JFK的司法会计考\\' in msg[3]

    def test_冒烟39(self,prg='OrderSet/其他指令/THROW39.PRG'):
        """
        ERROR，无内容，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟40(self,prg='OrderSet/其他指令/THROW40.PRG'):
        """
        ERROR，单个汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"我\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟41(self,prg='OrderSet/其他指令/THROW41.PRG'):
        """
        ERROR，单个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"1\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟42(self,prg='OrderSet/其他指令/THROW42.PRG'):
        """
        ERROR,单个小写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"a\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟43(self,prg='OrderSet/其他指令/THROW43.PRG'):
        """
        ERROR，单个大写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"A\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟44(self,prg='OrderSet/其他指令/THROW44.PRG'):
        """
        ERROR,单个中式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"！\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟45(self,prg='OrderSet/其他指令/THROW45.PRG'):
        """
        ERROR，单个英式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"!\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟46(self,prg='OrderSet/其他指令/THROW46.PRG'):
        """
        ERROR，单个空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\" \\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟47(self,prg='OrderSet/其他指令/THROW47.PRG'):
        """
        ERROR，32个最长汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻吼吼吼吼吼吼吼吼吼吼嘿嘿\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟48(self,prg='OrderSet/其他指令/THROW48.PRG'):
        """
        ERROR，最长32个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"11111111112222222222333333333366\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟49(self,prg='OrderSet/其他指令/THROW49.PRG'):
        """
        ERROR，最长32个大小写字母,验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"UuuuuuuuuuRrrrrrrrrrHhhhhhhhhhOo\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟50(self,prg='OrderSet/其他指令/THROW50.PRG'):
        """
        ERROR，最长32个标点符号+空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"!@#$%^&*(_+-,.? ？！@#￥%……&*（）——+：\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟51(self,prg='OrderSet/其他指令/THROW51.PRG'):
        """
        ERROR，最长32个混合字符，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_ERROR
        assert '自定义消息 \\"asd士大夫ASD123，。、,./   收到JFK的司法会计考\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟52(self,prg='OrderSet/其他指令/THROW52.PRG'):
        """
        FATAL，无内容，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟53(self,prg='OrderSet/其他指令/THROW53.PRG'):
        """
        FATAL，单个汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"我\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟54(self,prg='OrderSet/其他指令/THROW54.PRG'):
        """
        FATAL，单个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"1\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟55(self,prg='OrderSet/其他指令/THROW55.PRG'):
        """
        FATAL,单个小写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"a\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟56(self,prg='OrderSet/其他指令/THROW56.PRG'):
        """
        FATAL，单个大写字母，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"A\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟57(self,prg='OrderSet/其他指令/THROW57.PRG'):
        """
        FATAL,单个中式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"！\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟58(self,prg='OrderSet/其他指令/THROW58.PRG'):
        """
        FATAL，单个英式标点符号，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"!\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟59(self,prg='OrderSet/其他指令/THROW59.PRG'):
        """
        FATAL，单个空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\" \\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟60(self,prg='OrderSet/其他指令/THROW60.PRG'):
        """
        FATAL，32个最长汉字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"哈哈哈哈哈哈哈哈哈哈嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻吼吼吼吼吼吼吼吼吼吼嘿嘿\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟61(self,prg='OrderSet/其他指令/THROW61.PRG'):
        """
        FATAL，最长32个数字，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"11111111112222222222333333333366\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟62(self,prg='OrderSet/其他指令/THROW62.PRG'):
        """
        FATAL，最长32个大小写字母,验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"UuuuuuuuuuRrrrrrrrrrHhhhhhhhhhOo\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟63(self,prg='OrderSet/其他指令/THROW63.PRG'):
        """
        FATAL，最长32个标点符号+空格，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"!@#$%^&*(_+-,.? ？！@#￥%……&*（）——+：\\' in msg[3]
        # 后置
        psy.reset()

    def test_冒烟64(self,prg='OrderSet/其他指令/THROW64.PRG'):
        """
        FATAL，最长32个混合字符，验证THROW执行结果
        :param prg:主程序
        :return:NONE
        """
        pvm.load('./', prg)
        time.sleep(3)
        assert pvm.mainProgNames()[1] == [prg]
        pMot.setGpEn(0, 1)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 1
        pvm.start(prg)
        msg = psy.getMessage(10000)
        pMot.setGpEn(0, 0)
        time.sleep(1)
        assert pMot.getGpEn(0)[1] == 0
        pvm.stop(prg)
        pvm.unload(prg)
        time.sleep(1)
        assert not pvm.mainProgNames()[1]
        assert msg[1] == Hsc3ApiPy.ErrLevel.ERR_LEVEL_FATAL
        assert '自定义消息 \\"asd士大夫ASD123，。、,./   收到JFK的司法会计考\\' in msg[3]
        # 后置
        psy.reset()