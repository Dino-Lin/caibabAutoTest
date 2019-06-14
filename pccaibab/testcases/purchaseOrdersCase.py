import sys
sys.path.append('../')
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from commons import commonLogin
from utils import common

class PurchaseOrdersTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin, cls.driver)

    # # 已登录状态下，使用有报价权限的供应商去报价公示时间未开始的采购单
    # def test_notShow(self):
    #     orderId = "WHZHX20190612015"
    #     #搜索单号
    #     self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
    #     self.driver.find_element_by_class_name("head-search-btn").click()
    #     #等待页面加载
    #     flag = common.isElementExistWithCssSelector(self.driver,'#root > div > div > div.wrap > div.clearfix._34phGAdkvl-wtAiyH9vAHc > div > div.clearfix > div > p')
    #     self.assertEqual(True,flag)
    #     sleep(2)
    # def tearDown(self):
    #     self.driver.get('http://www.caibab.com/index')
    #
    # # 已登录状态下，使用有报价权限的供应商去报价处于公示时间，报名未开始阶段的采购单
    # def test_notStarted(self):
    #     orderId = "WHZHX20190612002"
    #     # 先清空 再搜索
    #     self.driver.find_element_by_class_name("head-search-input").clear()
    #     self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
    #     self.driver.find_element_by_class_name("head-search-btn").click()
    #     # 等待报价按钮出现
    #     submit = self.driver.find_element_by_link_text('立即报价')
    #     submit.click()
    #     # 等待详情页报价按钮出现
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     flag = common.isElementExistWithCssSelector(self.driver,'#root > div > div > div.wrap > div.clearfix._2EhXdGEzvtQG7cgG83tuPF > div.right._3wabwNSbYm9Vib0y4vqTw8 > div.iY946Gz-I5wmrBrCFS8Lv > div.clearfix._2vnIxjgzYdrwataLGpgJRU > div._3AsDEBG-vJW6ptvgvUHMjN > div > a')
    #     # 判断字段是否存在
    #     self.assertEqual(True, flag)
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    # def tearDown(self):
    #     self.driver.get('http://www.caibab.com/index')

    # 已登录状态下，使用有报价权限的供应商去报价处于公示时间，报名已开始的采购单
    def test_signup_notStarted(self):
        orderId = "WHZHX20190613007"
        # 先清空 再搜索
        self.driver.find_element_by_class_name("head-search-input").clear()
        self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
        self.driver.find_element_by_class_name("head-search-btn").click()
        # 点击立即报价
        submit = self.driver.find_element_by_css_selector('#root > div > div > div.wrap > div.clearfix._34phGAdkvl-wtAiyH9vAHc > div > div.clearfix > div > div.clearfix._3FAgZnx0-H3B9UKC6CTJeb > div.right._21k08nZzyAB_e_XyaXVbtp > a')
        submit.click()
        # 等待详情页报价按钮出现
        self.driver.switch_to.window(self.driver.window_handles[-1])
        flag = common.isElementExistWithCssSelector(self.driver,'#root > div > div > div.wrap > div.clearfix._2EhXdGEzvtQG7cgG83tuPF > div.right._3wabwNSbYm9Vib0y4vqTw8 > div.iY946Gz-I5wmrBrCFS8Lv > div.clearfix._2vnIxjgzYdrwataLGpgJRU > div._3AsDEBG-vJW6ptvgvUHMjN > div > a')
        # 判断字段是否存在
        self.assertEqual(True,flag)

        # 填写报价单 再提交报价信息
        self.driver.find_element_by_name('items[${idx.index}].extBrand1').send_keys('欧派')
        self.driver.find_element_by_name('items[${idx.index}].extPrice1').send_keys('10000')
        div_submit = self.driver.find_element_by_css_selector('#root > div > div > div > div.wrap > div.clearfix._2EhXdGEzvtQG7cgG83tuPF > div:nth-child(2) > div > div:nth-child(1) > div._3RxYS4hMXuvGp1SB0MHE4U > div.text-center._2KqFvBb-3ndMUGaE2WOT7f > button:nth-child(2)')
        div_submit.click()
        # 切回当前窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 搜索该采购单
        submit = self.driver.find_element_by_css_selector('#pageForm > div > div:nth-child(1) > div > div > input.form-control')
        submit.send_keys('WHZHX20190613007')
        # 判断采购单是否存在
        self.driver.switch_to.window(self.driver.window_handles[-1])
        div = self.driver.find_element_by_css_selector('#pageForm > div > div:nth-child(2) > div > div > div > div > p')
        flag = common.isElementExistWithCssSelector(self.driver, '#pageForm > div > div:nth-child(2) > div > div > div > div > p')
        self.assertEqual(True, flag)
        sleep(10)
        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])

    def tearDown(self):
        self.driver.get('http://www.caibab.com/index')

#     # 已登录状态下，使用有报价权限的供应商去报名已截止的采购单
#     def test_signup_End(self):
#         orderId = "WHZHX20190612001"
#         # 先清空 在搜索
#         self.driver.find_element_by_class_name("head-search-input").clear()
#         self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
#         self.driver.find_element_by_class_name("head-search-btn").click()
#         # 等待报价按钮出现
#         submit = self.driver.find_element_by_link_text('报价已截止')
#         submit.click()
#         # 等待详情页报价按钮出现
#         self.driver.switch_to.window(self.driver.window_handles[-1])
#         flag = common.isElementExistWithLinkText(self.driver, '报价已截止')
#         # 判断字段是否存在
#         self.assertEqual(True, flag)
#         self.driver.close()
# def tearDown(self):

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()