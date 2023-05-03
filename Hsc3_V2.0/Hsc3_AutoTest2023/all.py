# coding=utf-8
"""
@Time : 2023/04/11
@author 系统部郭松江
@Content est_demo.py
"""
import pytest
import os
from datetime import datetime


if __name__=='__main__':
    pytest.main()
    now = datetime.now()
    timestr = now.strftime("%Y_%m_%d_%H_%M_%S")
    print(now)
    print('年_月_日_时_分_秒',timestr)
    dir = os.getcwd()+'\\reports'+'\\'+'自动化测试报告'+timestr
    if os.path.exists(dir):
        print("相同时间测试报告文件夹已存在")
    else:
        os.system("allure generate ./temp -o "+dir+" --clean")