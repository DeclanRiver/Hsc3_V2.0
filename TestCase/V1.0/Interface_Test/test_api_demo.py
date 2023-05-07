# -*- coding:utf-8 _*_
"""
@Time : 2023/02/22
@author 系统部郭松江
@Content test_冒烟测试用例.py
"""

import pytest
import html
from time import *
from HSC3Api import CommApi
from HSC3Api import ProxyCollect
from HSC3Api import ProxyVm
from HSC3Api import Hsc3ApiPy
from HSC3Api import ProxyMotion
from HSC3Api import ProxyVar
from HSC3Api import ProxySys
from HSC3Api import ProxyIO

comm = CommApi.CommApi("")
proMot = ProxyMotion.ProxyMotion(comm)  # 构造ProxyMotion对象
pVm = ProxyVm.ProxyVm(comm)  # 构造ProxyVm对象
proVar = ProxyVar.ProxyVar(comm)  # 构造ProVar对象
proSys = ProxySys.ProxySys(comm)  # 构造ProSys对象
proIO = ProxyIO.ProxyIO(comm)  # 构造ProIO对象
ip_adress='10.10.56.214'
wait =0.2
robot_type="JR605"

class TestEn:

    # @pytest.mark.skipif(robot_type!="JR605","输入跳过该用例的原因")
    def test_002_en(self):
        print("开始用例执行")
        # comm.connect(ip_adress, 23234)
        # sleep(1)
        # if proSys.isReady() == (0, True):
        #     proMot.setGpEn(0,1)
        #     sleep(wait)
        #     assert proMot.getGpEn(0)==(0, True),"打开使能失败"
        #     proMot.setGpEn(0, 0)
        #     sleep(wait)
        #     assert proMot.getGpEn(0) == (0, False), "关闭使能失败"
    # @pytest.mark.run(order=-1)
    # @pytest.mark.smoke
    # @pytest.mark.DriverControlOne
    # @pytest.mark.skip(reason="输入跳过该用例的原因")
    def test_001_en(self):
        print("test2")
            

