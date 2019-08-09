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
from selenium.webdriver.support.ui import Select
import datetime

# 备注：该用例为后台审核采购单的用例。自动测试用例中，只有需要修改公示时间的采购单，才需要通过后台审核，否则都是易材通直接审核

class ExaminePurchaseOrderTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonLogin.CommonLogin.cgcomsLogin(commonLogin.CommonLogin,cls.driver)


   def tearDown(self):
       self.driver.get('http://cgcoms.caibab.com')

   # 用例1：已登录后台，审核采购单
   def test_ExaminePurchaseOrder(self):
        # 点击‘采购管理’
        self.driver.find_elements_by_xpath('//span[text()="采购管理"]')[0].click()
        sleep(1)

        # 点击‘采购审核’
        self.driver.find_element_by_xpath('//span[text()="采购审核"]').click()
        sleep(1)

        # 点击‘采购单审核’
        self.driver.find_element_by_xpath('//span[text()="采购单审核"]').click()
        sleep(2)

        # 首先定位到frame
        element1 = self.driver.find_element_by_css_selector('#container > div > div.layui-tab-content > div.layui-tab-item.layui-show > iframe')
        # 进入frame
        self.driver.switch_to.frame(element1)
        # 点击‘审核’
        self.driver.find_elements_by_xpath('//a[@data-title="采购单审核"]')[2].click()
        # 选择公开日期

        # 通过审核
        self.driver.find_element_by_xpath('//input[@value="通过"]').click()



