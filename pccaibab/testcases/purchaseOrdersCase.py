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

    #已登录状态下，使用有报价权限的供应商去报价公示时间未开始的采购单
    def test_notShow(self):
        orderId = "WHZHX20190612015"
        #搜索单号
        self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
        self.driver.find_element_by_class_name("head-search-btn").click()
        #等待页面加载
        flag = common.isElementExistWithCssSelector(self.driver,'#root > div > div > div.wrap > div.clearfix._34phGAdkvl-wtAiyH9vAHc > div > div.clearfix > div > p')

        self.assertEqual(True,flag)

        sleep(2)


    # 已登录状态下，使用有报价权限的供应商去报价处于公示时间，报名未开始阶段的采购单
    def test_notStarted(self):
        orderId = "WHZHX20190612002"
        #先清空 再搜索
        self.driver.find_element_by_class_name("head-search-input").clear()
        self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
        self.driver.find_element_by_class_name("head-search-btn").click()
        #等待报价按钮出现

        submit = self.driver.find_element_by_css_selector('#root > div > div > div.wrap > div.clearfix._34phGAdkvl-wtAiyH9vAHc > div > div.clearfix > div > div.clearfix._3FAgZnx0-H3B9UKC6CTJeb > div.right._21k08nZzyAB_e_XyaXVbtp > a')
        submit.click()
        #等待详情页报价按钮出现
        self.driver.switch_to.window(self.driver.window_handles[-1])


        flag = common.isElementExistWithCssName(self.driver,'dAAhumYvkC172oE9iHX0j')


        #判断灰色报价按钮是否存在
        self.assertEqual(True, flag)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

#已登录状态下，使用有报价权限的供应商去报价处于公示时间，报名已开始的采购单
    def test_signup_notStarted(self):
        orderId = "WHZHX20190612005"
        # 先清空 在搜索
        self.driver.find_element_by_class_name("head-search-input").clear()
        self.driver.find_element_by_class_name("head-search-input").send_keys(orderId)
        self.driver.find_element_by_class_name("head-search-btn").click()
        #等待报价按钮出现
        submit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-radius.btn-orange')))
        submit.click()
        #等待详情页报价按钮出现
        submit1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '_39Rmm8kXoslEUEZqPhI2EA')))
        submit1.click()
        #判断点击后是页面标题是否还是详情而不是跳转到报价
        self.assertEqual(u"采购清单详情-材巴巴", self.driver.title)
    def tearDown(self):
        self.driver.get('http://www.caibab.com/index')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()