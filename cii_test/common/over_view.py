# -*- coding:utf-8 -*-
# !/usr/bin/python3
from cii_test.common.login_page import LoginPage
from selenium.webdriver import ActionChains
from cii_test.conf.proconf import *


class OverView(LoginPage):
    """
    封装概览页元素
    """

    # 查看不同日期的概览数据（近一周、近一月、近一年）
    def get_over_view_data(self, date: str = '近一周'):
        """
        :param date: 可输入近一周、近一月、近一年
        :return:
        """
        _element: str = '//button[text() = "{}"]'.format(date)
        self.find_element("xpath", _element).click()

    # 查看b超报告预览。
    def get_b_report(self):
        self.find_element("xpath", '//button[text()="B超报告"]').click()

    # 点击查看详情，进入机构化任务。
    def enter_structured_tasks(self):
        self.find_element("xpath", '//div[@class="app-cii-grid app-cii-grid--split-line"]'
                                   '/div[1]/div/div/div[2]/div[2]/div[2]/div/span').click()

    # 点击查看详情，进入核保任务
    def enter_underwriting_tasks(self):
        self.find_element("xpath", '//div[@class="app-cii-grid app-cii-grid--split-line"]'
                                   '/div[2]/div/div/div[2]/div[2]/div[2]/div/span').click()

    # 点击查看详情，进入数据统计
    def enter_data_statistics(self):
        self.find_element("xpath", '//div[@class="app-cii-grid app-cii-grid--split-line"]'
                                   '/div[3]/div/div/div[2]/div[2]/div[2]/div/span').click()

    # 资源包概览，点击医疗结构化详情，进入资源包管理界面
    def enter_sources_package(self, sources_type: int):
        """
        :param sources_type: 资源包类型（1: structured结构化， 2: underwriting智能核保）
        :return:
        """
        if sources_type == 1:
            self.find_element("xpath", '//tr[@class="no-hover"][1]/td[4]/div/span/span').click()
        elif sources_type == 2:
            self.find_element("xpath", '//tr[@class="no-hover"][2]/td[4]/div/span/span').click()
        else:
            raise print("请选择1，或者2表示资源包类型")

    def enter_buy_page(self, value: str = "购买"):
        """
        :param value: 超链接文本，默认输入购买
        :return:
        """
        # 获取value文本元素列表
        elements: list = self.find_elements("link", value)
        elements[0].click()  # 点击购买


if __name__ == '__main__':
    OV = OverView("chrome", "https://console.cloud.tencent.com/cii")
    # OV.login_cii("QQ", "password")  # QQ账号
    OV.login_cii("287132798", "A18782269156")  # QQ账号
    # OV.get_b_report()
    # OV.enter_structured_tasks()
    # OV.enter_underwriting_tasks()
    # OV.enter_data_statistics()
    # OV.get_over_view_data()
    # OV.enter_sources_package(2)
    # OV.enter_buy_page()
