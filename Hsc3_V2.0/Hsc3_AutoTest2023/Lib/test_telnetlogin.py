import logging
import telnetlib
import time
import os


class TelnetClient():
    def __init__(self, ):
        self.tn = telnetlib.Telnet()

    # 此函数实现telnet登录主机
    def login_host(self, host_ip, username, password):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(host_ip, port=23)
        except:
            logging.warning('%s网络连接失败' % host_ip)
            return False
        # 等待login出现后输入用户名，最多等待10秒
        print(self.tn.read_very_eager().decode('ascii'))
        self.tn.read_until(b'Fszb login:', timeout=5)
        self.tn.write(username.encode('ascii') + b"\r\n")
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password:', timeout=5)
        self.tn.write(password.encode('ascii') + b"\r\n")
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('ascii')
        print(command_result)
        if 'Login incorrect' not in command_result:
            logging.warning('%s登录成功' % host_ip)
            return True
        else:
            logging.warning('%s登录失败，用户名或密码错误' % host_ip)
            return False

    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self, command):
        # 执行命令
        self.tn.write(command.encode('ascii') + b"\r\n")
        time.sleep(1)
        # 获取命令结果
        command_result = self.tn.read_very_eager().decode('ascii')
        time.sleep(3)
        #logging.warning('命令执行结果：\n%s' % command_result)
        print('命令执行结果：\n%s' % command_result)
        baconFile = open('result.txt', 'w', encoding='utf-8')
        baconFile.write(command_result)
        baconFile.close()
    # 退出telnet
    def logout_host(self):
        self.tn.close()


#示例
#if __name__ == '__main__':
#    host_ip = '10.10.56.214'
#    username = 'root'
#    password = '111111'
#    command = 'ps;ls'
#    telnet_client = TelnetClient()
#    # 如果登录结果返加True，则执行命令，然后退出
#    if telnet_client.login_host(host_ip, username, password):
#        telnet_client.execute_some_command(command)
#        time.sleep(3)
#        telnet_client.logout_host()