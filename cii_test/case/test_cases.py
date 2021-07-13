import unittest
from cii_test.common.login_page import LoginPage
from cii_test.common.over_view import OverView
from cii_test.conf.proconf import *


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._L = OverView("chrome", URL)

    def tearDown(self) -> None:
        self._L.driver.close()

    def test01_login(self):
        """
        测试登录
        :return:
        """
        self._L.login_cii(*USER_ACCOUNT)
        self.assertEqual(self._L.assert_login_success(), "智能保险助手", "登录成功")

    def test02_over_view_data(self):
        """
        查看近一周，预览数据。
        :return:
        """
        self._L.login_cii(*USER_ACCOUNT)
        self._L.get_over_view_data()

    def test03_over_view_data(self):
        """
        查看近一年预览数据
        :return:
        """
        self._L.login_cii(*USER_ACCOUNT)
        self._L.get_over_view_data("近一年")

    def test04_get_b_report(self):
        """
        查看B超报告预览
        :return:
        """
        self._L.login_cii(*USER_ACCOUNT)
        self._L.get_b_report()

    @unittest.skip
    def test05_enter_structured_tasks(self):
        """
        测试打开结构化任务界面
        :return:
        """
        self._L.login_cii(*USER_ACCOUNT)
        self._L.enter_structured_tasks()


if __name__ == '__main__':
    # suit = unittest.TestSuite()
    # suit.addTest(TestCase("test03_over_view_data"))
    unittest.main()
    # unittest.TextTestRunner().run(suit)
