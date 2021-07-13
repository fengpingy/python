# -*- coding:utf-8 -*-
# !/usr/bin/python3
from cii_test.common.over_view import OverView
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32con
import win32gui
import time
from public import *


class StructuredTasks(OverView):
    """
    封装结构化任务界面元素
    """
    def establish_task(self, policy_id: str):
        self.enter_structured_tasks()
        self.find_element("xpath", '//button[text()="新建"]').click()
        self.find_element("name", 'policyId').send_keys(policy_id)
        self.find_element("xpath", '//button[text()="选择文件"]').click()
        time.sleep(2)  # 设置等待，保证能定位到上传弹窗
        # 上传文件
        upload("chrome", r"E:\PythonFeng\Ui_Test\cii_test\data\医疗数据.pdf")
        time.sleep(5)  # 设置等待，确保打开文件成功
        self.find_element("xpath", '//button[text()="开始上传"]').click()
        time.sleep(5)  # 等待上传完成
        self.find_element("xpath", '//button[text()="创建"]').click()
        print("创建结构化任务成功")


if __name__ == '__main__':
    ST = StructuredTasks("chrome", "https://console.cloud.tencent.com/cii")
    # ST.login_cii("287132798", "A18782269156")
    ST.establish_task("qta")
