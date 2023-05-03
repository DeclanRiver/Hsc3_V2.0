# -*- coding:utf-8 _*_
"""
@Time : 2023/02/22
@author 系统部郭松江
@Content test_冒烟测试用例.py
"""
import pytest



class Test_HSC3冒烟测试:

    def test_冒烟测试1(self):
        a=1
        b=1
        assert a==b,"a不等于b"

    def test_冒烟测试2(self):
        c = 1
        d = 2
        assert c==d, "断言失败"

    @pytest.mark.skip(reason="V2.0不支持telnet协议")
    def test_冒烟测试3(self):
        G = 1
        t = 2
        assert G==t, "断言失败"

    def test_冒烟测试4(self):
        pass




