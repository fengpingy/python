# -*- coding:utf-8 -*-
import os
import sys
import time
import datetime
import random
import logging
import paramiko
import win32con
import win32gui


def upload(browser, file_path):
    """
    定位弹窗，上传文件
    :param browser: 浏览器类型：chrome,firefox,ie,edge
    :param file_path: 需要上传文件的绝对路径。
    :return:
    """
    if browser.lower() == "chrome":
        title = "打开"
    elif browser.lower() == "firefox":
        title = "文件上传"
    elif browser.lower() == "ie":
        title = "选择要加载的文件"
    else:
        raise print(f"{browser}浏览器类型还未添加，请自行设置")
    # 定位上传窗口
    dialog = win32gui.FindWindow("#32770", title)
    # 向下传递
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
    # 编辑按钮
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")
    # 输入文件的绝对路径，点击“打开”按钮
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)  # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

class ConnectLinux(object):
    """
    连接linux服务器
    """
    def __init__(self, host, port=22, username=None, password=None):
        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(host, port, username, password)  # 定义一个ssh实例

        self._transport = paramiko.Transport((host, port))
        self._transport.connect(username=username, password=password)

        self._ftp = paramiko.SFTPClient.from_transport(self._transport)  # 定义一个ftp实例

    def exec_command(self, commands: str):
        """
        执行linux命令，返回标准输入，输出，error
        :param commands: linux命令
        :return:
        """
        try:
            _ssh_in, _ssh_out, _ssh_error = self._ssh.exec_command(commands)

            print("输入命令为：{}".format(commands))  # 展示输入命令

            _out = _ssh_out.read().decode()  # 输出结果

            _error = _ssh_error.read().decode()  # 输出的error

        except Exception as E:
            raise E

        finally:
            self._ssh.close()

        return _out

    def ftp_get(self, linux_path, win_path):
        """
        上传和下载服务器文件
        :param linux_path: 服务器文件路劲
        :param win_path: 本地文件路径
        :return:
        """
        self._ftp.get(linux_path, win_path)  # 服务器下载文件
        self._ftp.close()
        self._transport.close()

    def ftp_put(self, win_path, linux_path):
        self._ftp.put(win_path, linux_path)  # 本地上传文件
        self._ftp.close()
        self._transport.close()


if __name__ == '__main__':
    C = ConnectLinux("139.186.197.203", username="root", password="Feng@1234")
    # a = C.exec_command("ls && cd fjp_file/ && pwd")
    C.ftp_get("Ui_Test.rar", r"E:\PythonFeng\cii_test.rar")
    # print(a)
    # print(type(a))
    # print()
    # logging.basicConfig(filename='example.log', filemode="w", encoding="utf-8", level=logging.DEBUG)
    # logging.info("fuck!")
    # print(os.name)
    # print(os.listdir(os.getcwd()))
    # print(sys.modules[__name__])








