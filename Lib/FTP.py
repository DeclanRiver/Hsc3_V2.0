# !/usr/bin/env python3
# coding=utf-8
from ftplib import FTP
import os


class MyFtp(object):
    """
    ftp上传下载接口类
    """
    ftp = FTP()

    def __init__(self, ip, port=21, timeout=5):
        self.ftp.connect(ip, port, timeout)
        self.ftp.encoding = 'utf-8'
        self.ftp.set_debuglevel(0)

    def login(self, user, passwd):
        """
        登录
        :param user: 用户名
        :param passwd: 密码
        :return: 返回self，支持链式调用
        """
        self.ftp.login(user, passwd)
        print(self.ftp.getwelcome())
        return self

    def close(self):
        self.ftp.quit()

    def download_file(self, remove_path, local_path, prg):
        """
        下载单个文件，将 remove_path 的文件下载到 local_path。
        :param remove_path: ftp目录文件地址
        :param local_path: 本地文件地址
        :param prg: 文件名
        :return:返回True/false，是否成功的标志
        """
        if not os.path.exists(local_path):
            os.mkdir(local_path)
        file_handel = open(local_path + '/' + prg, 'wb')
        self.ftp.retrbinary('RETR ' + remove_path + '/' + prg, file_handel.write, 1024)
        file_handel.close()

    def upload_file(self, remove_path, local_path, prg):
        """
        上传单个文件，将 local_path 的文件上传到 remove_path。
        :param remove_path: ftp目录文件地址
        :param local_path: 本地文件地址
        :param prg: 文件名
        :return: 返回True/false，是否成功标志
        """
        file_handle = open(local_path + '/' + prg, 'rb')
        self.ftp.storbinary('STOR ' + remove_path + '/' + prg, file_handle, 1024)
        file_handle.close()

    def download_dir(self, remote_dir, local_dir):
        """
        下载整个目录
        :param remote_dir: ftp目录
        :param local_dir: 本地目录
        :return: 返回True/false，是否成功的标志
        """
        if not os.path.exists(local_dir):
            os.mkdir(local_dir)
        self.ftp.cwd(remote_dir)
        dir_files = self.ftp.nlst()
        for file in dir_files:
            # 识别为目录 递归
            if file.find('.') == -1:
                local = os.path.join(local_dir + '/', file)
                if not os.path.exists(local):
                    os.mkdir(local)
                dep_dir = remote_dir + '/' + file
                self.download_dir(dep_dir, local)
            else:
                # 识别为文件进行下载
                file_handel = open(local_dir + '/' + file, 'wb')
                self.ftp.retrbinary('RETR ' + remote_dir + '/' + file, file_handel.write, 1024)
        self.ftp.cwd('..')  # 返回上一级目录

    def upload_dir(self, remote_path, local_path):
        """
        上传整个目录
        :param remote_path: ftp远程目录
        :param local_path: 本地目录
        :return: 是否成功的标志
        """
        if not os.path.exists(local_path):
            print('LocalPath not exits')
            return False
        dir_files = os.listdir(local_path)
        for file in dir_files:
            if file.find('.') == -1:  # 识别为文件夹
                new_lpath = local_path + '/' + file
                new_rpath = remote_path + '/' + file
                self.ftp.cwd(remote_path)
                if not file in self.ftp.nlst():
                    self.ftp.mkd(new_rpath)
                self.upload_dir(new_rpath, new_lpath)
            else:
                # 识别为文件
                file_handle = open(local_path + '/' + file, 'rb')
                self.ftp.storbinary('STOR ' + remote_path + '/' + file, file_handle, 1024)
                file_handle.close()
        os.chdir('..')

    # --------------------------------------------分割线-------------------------------------------

    def udl_file(self, remove_path, local_path, prg, lgo):
        """
        上传/下载单个文件
        :param lgo: 上传为0，下载为1
        :param remove_path: ftp远程目录地址
        :param local_path: 本地目录地址
        :param prg: 文件名
        :return: 是否成功的标志
        """
        try:
            if lgo:
                print('downloading...')
                self.download_file(remove_path, local_path, prg)
                print('download finished')
                return True
            else:
                print('uploading...')
                self.upload_file(remove_path, local_path, prg)
                print('upload finished')
                return True
        except Exception as err:
            print('download/upload failed: ', repr(err))
            return False

    def udl_dir(self, remove_dir, local_dir, lgo):
        """
        上传/下载目录接口
        :param remove_dir: ftp远程目录地址
        :param local_dir: 本地目录地址
        :param lgo: 上传为0，下载为1
        :return: 成功与否的标志
        """
        try:
            if lgo:
                print('downloading...')
                self.download_dir(remove_dir, local_dir)
                print('download finished')
                return True
            else:
                print('uploading...')
                self.ftp.cwd(remove_dir)
                dir_path = remove_dir + '/' + os.path.basename(local_dir)
                if not os.path.basename(local_dir) in self.ftp.nlst():
                    self.ftp.mkd(dir_path)
                self.upload_dir(dir_path, local_dir)
                print('upload finished')
                return True
        except Exception as err:
            print('download/upload failed: ', repr(err))
            return False
