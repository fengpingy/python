# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from cii_test.conf.proconf import *
import json


class MyDriver(object):
    def __init__(self, browser, url):
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path="../resource/chromedriver")
            self.driver.get(url)
            self.driver.maximize_window()
        elif browser == "ie":

            raise print("还未安装IEdriver,请使用chrome")
        else:
            raise print("请使用chrome浏览器")

    def find_element(self, method: str, element: str):

        if method.lower() == "xpath":
            find_element = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_element(By.XPATH, element))

        elif method.lower() == "id":
            find_element = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_element(By.ID, element))

        elif method.lower() == "name":
            find_element = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_element(By.NAME, element))

        elif method.lower() == "class":
            find_element = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_element(By.CLASS_NAME,
                                                                                                      element))

        elif method.lower() == "css":
            find_element = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_element(By.CSS_SELECTOR,
                                                                                                      element))

        elif method.lower() == "link":
            find_element = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_element(By.LINK_TEXT,
                                                                                                      element))

        elif method.lower() == "part_link":
            find_element = WebDriverWait(self.driver, 20, 1).until(lambda d: self.
                                                                   driver.find_element(By.PARTIAL_LINK_TEXT, element))
        else:
            raise print("请选择正确的定位方式")

        return find_element

    def find_elements(self, method: str, element: str):

        if method.lower() == "xpath":
            find_elements = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_elements(By.XPATH, element))

        elif method.lower() == "id":
            find_elements = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_elements(By.ID, element))

        elif method.lower() == "name":
            find_elements = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_elements(By.NAME, element))

        elif method.lower() == "class":
            find_elements = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_elements(By.CLASS_NAME,
                                                                                                      element))

        elif method.lower() == "css":
            find_element = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_elements(By.CSS_SELECTOR,
                                                                                                      element))

        elif method.lower() == "link":
            find_elements = WebDriverWait(self.driver, 20, 1).until(lambda d: self.driver.find_elements(By.LINK_TEXT,
                                                                                                      element))

        elif method.lower() == "part_link":
            find_elements = WebDriverWait(self.driver, 20, 1).until(lambda d: self.
                                                                   driver.find_elements(By.PARTIAL_LINK_TEXT, element))
        else:
            raise print("请选择正确的定位方式")

        return find_elements

    def switch_to_frame(self, value):
        """
        切换iframe
        :param value:
        :return:
        """
        self.driver.switch_to.frame(value)

    def switch_to_default_content(self):
        """
        退回上一级iframe
        :return:
        """
        self.driver.switch_to.default_content()

    def get_window_handles(self):
        """
        :return: 获取打开的所有窗口句柄
        """
        _windows: list = self.driver.window_handles
        return _windows

    def get_current_window_handle(self):
        """
        :return: 获取当前窗口句柄
        """
        _window = self.driver.current_window_handle
        return _window

    def switch_to_window(self, window_handle):
        """
        切换窗口
        :param window_handle: 窗口句柄
        :return:
        """
        self.driver.switch_to.window(window_handle)

    def close_browse(self):
        """
        关闭打开的标签页
        :return:
        """
        self.driver.close()

    def quit_browse(self):
        """
        强制退出浏览器
        :return:
        """
        self.driver.quit()

    def select_element(self, method: str, element, value):
        """
        定位下拉框元素
        :param method: 定位元素方法
        :param element: 需要定位的元素
        :param value:通过value选择选择下拉框中元素
        :return:
        """
        select = Select(self.find_element(method, element))
        select.select_by_value(value)


if __name__ == '__main__':
    MD =MyDriver("chrome", "https://www.baidu.com")


