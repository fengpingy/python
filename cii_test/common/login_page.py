# -*- coding:utf-8 -*-
from cii_test.conf.proconf import *
from cii_test.common.base import MyDriver
import time


class LoginPage(MyDriver):

    def login_cii(self, uname: str, upassword: str):
        self.find_element("xpath", '//*[@id="loginBox"]/div/div/div[4]/div[2]/div[2]/a').click()
        self.switch_to_frame('ptlogin_iframe')
        self.find_element("xpath", '/html/body/div[1]/div[9]/a[1]').click()
        self.find_element("xpath", '//*[@id="u"]').send_keys(uname)
        self.find_element("xpath", '//*[@id="p"]').send_keys(upassword)
        self.find_element("xpath", '//*[@id="login_button"]').click()

    def assert_login_success(self):
        text = self.find_element('css', '.sdk-menus-h2').text
        return text


if __name__ == '__main__':
    LP =LoginPage("chrome", URL)
    LP.login_cii(*USER_ACCOUNT)  # QQ账号
