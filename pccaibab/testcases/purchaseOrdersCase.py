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

    def tearDown(self):
        self.driver.get('http://www.caibab.com/index')

    # 已登录状态下，使用有报价权限的供应商去报价公示时间未开始的采购单
    def test_notShow(self):
        orderId = "WHZHX20190612015"
        #搜索单号
        self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
        self.driver.find_element_by_class_name("head-search-btn").click()
        #等待页面加载
        flag = common.isElementExistWithCssSelector(self.driver,'#root > div > div > div.wrap > div.clearfix._34phGAdkvl-wtAiyH9vAHc > div > div.clearfix > div > p')
        self.assertEqual(True,flag)

    # 已登录状态下，使用有报价权限的供应商去报价处于公示时间，报名未开始阶段的采购单
    def test_notStarted(self):
        orderId = "WHZHX20190612002"
        # 先清空 再搜索
        self.driver.find_element_by_class_name("head-search-input").clear()
        self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
        self.driver.find_element_by_class_name("head-search-btn").click()
        # 等待报价按钮出现
        submit = self.driver.find_element_by_link_text('立即报价')
        submit.click()
        # 等待详情页报价按钮出现
        self.driver.switch_to.window(self.driver.window_handles[-1])
        flag = common.isElementExistWithCssSelector(self.driver,'#root > div > div > div.wrap > div.clearfix._2EhXdGEzvtQG7cgG83tuPF > div.right._3wabwNSbYm9Vib0y4vqTw8 > div.iY946Gz-I5wmrBrCFS8Lv > div.clearfix._2vnIxjgzYdrwataLGpgJRU > div._3AsDEBG-vJW6ptvgvUHMjN > div > a')
        # 判断字段是否存在
        self.assertEqual(True, flag)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    # 已登录状态下，使用有报价权限的供应商去报价处于公示时间，报名已开始的采购单
    def test_signup_notStarted(self):
        # 点击搜索，进入采购单页面
        self.driver.find_element_by_class_name("head-search-btn").click()
        # 点击立即报价
        submit = self.driver.find_element_by_css_selector('#root > div > div > div.wrap > div.clearfix._34phGAdkvl-wtAiyH9vAHc > div > div.clearfix > div:nth-child(1) > div.clearfix._3FAgZnx0-H3B9UKC6CTJeb > div.right._21k08nZzyAB_e_XyaXVbtp > a')
        submit.click()
        # 切换到最新打开的窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])

        if(common.isElementExistWithLinkText(self.driver,'已报价')):
            print('已报价采购单，请重新生成一个最新的采购单')
            self.assertEqual(True,False)
        else:
            self.driver.find_element_by_link_text('立即报价').click()
            sleep(1)
            orderNo = self.driver.find_element_by_css_selector('#root > div > div > div > div.wrap > div.clearfix._2EhXdGEzvtQG7cgG83tuPF > div:nth-child(2) > div > div:nth-child(1) > div.iY946Gz-I5wmrBrCFS8Lv > div._2vnIxjgzYdrwataLGpgJRU > div._32Wen-44B49sTWSpEpyq9H._2gf688RCfd2KzrOmz8k7D9 > p:nth-child(1) > span').text
            # 填写报价单 再提交报价信息
            band = self.driver.find_element_by_xpath("//div[@class='_1Jq0ZnmRkRFttwcQ_LFz7j']/input")
            band.send_keys('欧派')
            price = self.driver.find_element_by_xpath("//div[@class='_30UfIj8PiM5jHq2LinrkU8']/input")
            price.send_keys('10000')
            div_submit = self.driver.find_element_by_css_selector('#root > div > div > div > div.wrap > div.clearfix._2EhXdGEzvtQG7cgG83tuPF > div:nth-child(2) > div > div:nth-child(1) > div._3RxYS4hMXuvGp1SB0MHE4U > div.text-center._2KqFvBb-3ndMUGaE2WOT7f > button:nth-child(2)')
            div_submit.click()
            sleep(1)
            self.driver.close()
            # 切回当前窗口
            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(0.5)
            # 搜索该采购单
            self.driver.find_element_by_xpath("//form[@id='pageForm']//input[@name='keyword']").send_keys(orderNo)
            self.driver.find_element_by_xpath("//form[@id='pageForm']//button[text()='搜索']").click()

            # 判断采购单是否存在
            flag = common.isElementExistWithCssSelector(self.driver,'#root > div > div > div.wrap > div.clearfix._34phGAdkvl-wtAiyH9vAHc > div > div.clearfix > div > div.clearfix._3pZvOZtS-Smo95JcxSKPOj > div.PEjczqWJTBByJt4C48alk')
            self.assertEqual(True, flag)

    # 已登录状态下，使用有报价权限的供应商去报名已截止的采购单
    def test_signup_End(self):
        orderId = "WHZHX20190612001"
        # 先清空 在搜索
        self.driver.find_element_by_class_name("head-search-input").clear()
        self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
        self.driver.find_element_by_class_name("head-search-btn").click()
        # 点击立即报价
        submit = self.driver.find_element_by_css_selector('#root > div > div > div.wrap > div.clearfix._34phGAdkvl-wtAiyH9vAHc > div > div.clearfix > div > div.clearfix._3FAgZnx0-H3B9UKC6CTJeb > div.right._21k08nZzyAB_e_XyaXVbtp > a')
        submit.click()
        # 等待详情页报价按钮出现
        self.driver.switch_to.window(self.driver.window_handles[-1])
        flag = common.isElementExistWithLinkText(self.driver, '报价已截止')
        # 判断字段是否存在
        self.assertEqual(True, flag)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    @classmethod
    def tearDownClass(cls) -> None:
            cls.driver.quit()