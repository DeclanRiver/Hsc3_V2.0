import unittest
import uiautomator2 as u2
import time
import random
from HSC3Api import ProxyMotion
from HSC3Api import ProxyVar
from HSC3Api import CommApi
from HSC3Api import ProxyVm
from HSC3Api import ProxyIO
from HSC3Api import ProxySys
from HSC3Api import Hsc3ApiPy
from time import sleep
import pytest
import shutil

#
# # 连接系统


'''
连接系统
连接失败会一直尝试连接 30 分钟
ip : 系统IP地址 “...”
:return:
'''


# i = 0
# while comm.isConnected() == False:
#     comm.connect('10.10.57.213', 23234)
#     # comm.connect("10.10.57.213", 23234)
#     sleep(1)
#     if comm.isConnected() == True:
#         print("连接成功！！！")
#     elif comm.isConnected() == False:
#         print("第", i + 1, "次连接失败，重连中...")
#         i += 1
# comm = CommApi.CommApi("..\\log\\test")
# proMot = ProxyMotion.ProxyMotion(comm)  # 构造ProxyMotion对象
# pVm = ProxyVm.ProxyVm(comm)  # 构造ProxyVm对象
# proVar = ProxyVar.ProxyVar(comm)  # 构造ProVar对象
# proSys = ProxySys.ProxySys(comm)  # 构造ProSys对象
# proIO = ProxyIO.ProxyIO(comm)  # 构造ProIO对象


class 工具库_hd(object):

    def __init__(self, comm):
        """
        :param comm:CommApi对象
        """
        self.comm = comm
        if self.comm.isConnected():
            print("已获取连接状态")
            self.proMot = ProxyMotion.ProxyMotion(self.comm)  # 构造ProxyMotion对象
            self.pVm = ProxyVm.ProxyVm(self.comm)  # 构造ProxyVm对象
            self.proVar = ProxyVar.ProxyVar(self.comm)  # 构造ProVar对象
            self.proSys = ProxySys.ProxySys(self.comm)  # 构造ProSys对象
            self.proIO = ProxyIO.ProxyIO(self.comm)  # 构造ProIO对象
        else:
            print("获取失败")

    def 遍历生成文件(self):
        """
        请自行前往修改所需信息
        :return:
        """
        m = 1
        while m < 10000:
            n = '%04d' % m
            # time.sleep(111111)
            print(n)
            # p = "C:\\Users\\0389\Desktop\\1.6.9泉州外部\PRG\\"+n+".PRG"
            shutil.copy("C:\\Users\\0389\Desktop\\1.6.9泉州外部\PRG\\0000.PRG",
                        "C:\\Users\\0389\Desktop\\1.6.9泉州外部\PRG\\" + n + ".PRG")
            m += 1

        print("FINISH")

    def 获取本地时间(self):
        """
        获取本地时间
        :return: 当前本地时间
        """
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 二进制数拆分转数组     主要用于IO转换
    def decToBin(self, a):
        """
        # 二进制数拆分转数组     主要用于IO转换
        第 0 组 第 12个IO：
        0*32 +12=12
        decToBin(proIO.getDinGrp(0)[1])[12]
        :param a:
        :return:
        """
        arry = []
        while True:
            arry.append(int(a % 2))
            a = a // 2
            if a == 0:
                break
        return arry

    def 关节位置误差判断(self, jp, accuracy0, accuracy1):
        """
        关节位置误差判断
        关节位置误差判断函数
        python实现关节式与笛卡尔式目标点检查函数/接口，目标点不正确时报错提示具体误差轴（供自动化测试使用）
        gpId::=轴组号
        jp::=目标点位关节位置数据
        accuracy0::=内部轴精度  单位:度    取值范围：非负实数
        accuracy1::=外部轴精度  单位:毫米  取值范围：非负实数
        ajp::=实际关节位置    (0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])::=(<轴号>,[关节点位])
        af::=保留的小数点位数  保留a位小数
       :return: 返回self，支持链式调用
       """

        # 获取相同轴号的实际关节位置
        assert accuracy0 >= 0, "内部轴精度有误"
        assert accuracy1 >= 0, "外部轴精度有误"
        ajp = (self.proMot.getJntData(jp[0]))
        i = 0
        j = 4  # 精度
        while i <= 8:
            if i < 6:
                assert (((round(jp[1][i], j)) - accuracy0 <= (round(ajp[1][i], j))) and (
                    (round(jp[1][i], j) + accuracy0 >= round(ajp[1][i], j)))), "内部轴不在目标点精度范围内"
            elif 6 <= i < 9:
                assert (round(jp[1][i], j)) - accuracy1 <= (round(ajp[1][i], j)) and (
                        round(jp[1][i], j) + accuracy1 >= round(ajp[1][i], j)), "外部轴不在目标点精度范围内"
            i += 1
            if i == 6:
                print("内部轴位置误差在精度范围内")
            if i == 8:
                print("外部轴位置误差在精度范围内")

    # 空间位置误差判断函数
    # python实现关节式与笛卡尔式目标点检查函数/接口，目标点不正确时报错提示具体误差轴（供自动化测试使用）
    # gpId::=轴组号
    # lp::=目标点位空间位置数据
    # accuracy0::=空间精度、外部轴精度  单位:毫米  取值范围：非负实数
    # accuracy1::=形态位精度  单位：度    取值范围：非负实数
    # accuracy2::=外部轴精度  单位:毫米  取值范围：非负实数
    # ap::=实际位置    (0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])::=(<轴号>,[关节点位])

    def 空间位置误差判断(self, lp, accuracy0, accuracy1, accuracy2):
        # 获取相同轴号的实际关节位置
        assert accuracy0 >= 0, "空间精度有误"
        assert accuracy1 >= 0, "形态位精度有误"
        alp = (self.proMot.getLocData(lp[0]))
        i = 0
        j = 4  # 精度
        while i <= 8:
            if i < 3:
                # TCP空间位置目标点与实际位置之间的距离误差
                assert ((lp[1][0] - alp[1][0]) ** 2 + (lp[1][1] - alp[1][1]) ** 2 + (
                        lp[1][2] - alp[1][2]) ** 2 <= accuracy0 ** 2), "空间位置误差不在精度范围内"
                i += 3
            elif 3 <= i < 6:
                # 目标点形态位与实际位置形态位的误差
                assert (round(lp[1][i], j)) - accuracy1 <= (round(alp[1][i], j)) and (
                        round(lp[1][i], j) + accuracy1 >= round(alp[1][i], j)), "形态位位置不在目标点精度范围内"
                i += 1
            elif i >= 6:
                # 外部轴目标位置与实际位置的误差
                assert (((round(lp[1][i], j)) - accuracy2 <= (round(alp[1][i], j))) and (
                    (round(lp[1][i], j) + accuracy2 >= round(alp[1][i], j)))), "外部轴位置不在目标点精度范围内"
                i += 1
            if i == 3:
                print("TCP空间位置目标点与实际位置之间的距离误差在精度范围内")
            if i == 6:
                print("目标点形态位与实际位置形态位的误差在精度范围内")
            if i == 8:
                print("外部轴目标位置与实际位置的误差在精度范围内")

    # 例1： test_jp=proMot.getJntData(0) print("当前实际关节位置：",proMot.getJntData(0)) # test_jp= (0, [-0.0002951,
    # -89.9997276, 180.001362, 1.0001716, 89.9998983, -1.00022270000000000002, 0.0, 0.0, 0.0]) # j=4 # print(round(
    # test_jp[1][i],3j)) # sleep(200) # 关节位置误差判断(test_jp,1,1)
    #
    # # 例2：
    # print("当前实际空间位置：",proMot.getLocData(0))
    # # test_lp=proMot.getLocData(0)
    # test_lp=(0, [805.4816291, 14.8074247, 1071.5755817, -178.9464931, -0.8087444, 179.9997196, 0.0, 0.0, 0.0])
    # 空间位置误差判断(test_lp,1,1,1)

    # # unittest断言使用
    # class Unittest(unittest.TestCase):
    #     def unittest断言(self):
    #         # 常用断言
    #         assertEqual(1, 1)
    #         assert a <= b <= c, "say something you want to"
    #         assertEqual(a, b)  # a == b
    #         assertNotEqual(a, b)  # a != b
    #         assertTrue(x)  # bool(x) is True
    #         assertFalse(x)  # bool(x) is False
    #         assertIs(a, b)  # a is b
    #         assertIsNot(a, b)  # a is not b
    #         assertIsNone(x)  # x is None
    #         assertIsNotNone(x)  # x is not None
    #         assertIn(a, b)  # a in b
    #         assertNotIn(a, b)  # a not in b
    #         assertIsInstance(a, b)  # isinstance(a, b)
    #         assertNotIsInstance(a, b)  # not isinstance(a, b)
    #
    #         # 其他断言
    #         assertAlmostEqual(a, b)  # round(a-b, 7) == 0
    #         assertNotAlmostEqual(a, b)  # round(a-b, 7) != 0
    #         assertGreater(a, b)  # a > b
    #         assertGreaterEqual(a, b)  # a >= b
    #         assertLess(a, b)  # a < b
    #         assertLessEqual(a, b)  # a <= b
    #         assertRegexpMatches(s, re)  # regex.search(s)
    #         assertNotRegexpMatches(s, re)  # not regex.search(s)
    #         assertItemsEqual(a, b)  # sorted(a) == sorted(b) and works with unhashable objs
    #         assertDictContainsSubset(a, b)  # all the key/value pairs in a exist in b
    #         assertMultiLineEqual(a, b)  # strings
    #         assertSequenceEqual(a, b)  # sequences
    #         assertListEqual(a, b)  # lists
    #         assertTupleEqual(a, b)  # tuples
    #         assertSetEqual(a, b)  # sets or frozensets
    #         assertDictEqual(a, b)  # dicts
    #         assertMultiLineEqual(a, b)  # strings
    #         assertSequenceEqual(a, b)  # sequences
    #         assertListEqual(a, b)  # lists
    #         assertTupleEqual(a, b)  # tuples
    #         assertSetEqual(a, b)  # sets or frozensets
    #         assertDictEqual(a, b)  # dicts
    #

    # pytest断言
    # def 断言demo1(self,):
    #     a = 1
    #     assert a, "say something you want to"
    #
    # def 断言demo2(self):
    #     a = 0
    #     assert not a
    #
    # def 断言demo3(self):
    #     s = 'hello'
    #     assert 'h' in s
    #
    # def 断言demo4(self):
    #     a = 3
    #     assert a == 3
    #
    # def 断言demo5(self):
    #     a = 4
    #     assert a != 3
    #
    # def 断言demo6(self):
    #     a = 0
    #     b = 1
    #     assert a and b
    #
    # def 断言demo7(self):
    #     a = 0
    #     b = 1
    #     assert a or b

    def 自定义断言(self, a, b, c=1, ):
        """
        :param a: 比较对象
        :param b: 比较对象
        :param c: 操作符   1. ==      2. ！=     3. not a      4. a int b
        :return: 通过无返回，不通过报警返回报警原因
        """
        if c == 1:
            if a == b:
                print(a, "==", b)
            else:
                print("报错原因：", a, "!=", b)
                raise AssertionError
        if c == 2:
            if a != b:
                print(a, "!=", b)
            else:
                print("报错原因：", a, "==", b)
                raise AssertionError
        if c == 3:
            if not a:
                print("not", a)
            else:
                print("报错原因：", a, "==True")
                raise AssertionError
        if c == 4:
            if a in b:
                print(a, "in", b)
            else:
                print("报错原因：", a, "not in", b)
                raise AssertionError

    def IO虚拟(self):
        i = 32
        while i + 1:
            # 设置数字输入状态值  true - 虚拟；false - 真实
            self.proIO.setDinMaskBit(i, True)
            i -= 1
            self.proMot.setEstop(False)
        print("IO虚拟完成")

    def 等待就绪(self):
        """
        重启系统并等待系统就绪，复位报错信息
        :return:
        """
        if self.proMot.getGpEn(0):
            self.proMot.setGpEn(0, False)
            sleep(0.1)
        self.proSys.reboot()
        while 1:
            while 1:
                sleep(5)
                i = 0
                j = 0
                # 等待业务层启动完成
                while not self.comm.isConnected():
                    print("第", i + 1, "次连接失败，重连中...")
                    sleep(5)
                    i += 1
                # 等待系统就绪
                while not self.proSys.isReady()[1]:
                    j += 1
                    print("等待系统就绪   ", j)
                    # 半个小时没有启动成功
                    if j >= 6 * 30:
                        print("启动失败")
                        sleep(99999999)
                    sleep(5)
                break
            self.proSys.reset()
            break
