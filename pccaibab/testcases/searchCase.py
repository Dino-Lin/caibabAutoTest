import sys

sys.path.append('../')
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from commons import commonLogin
from commons import commonFunction
from utils import common
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import random
import string


'''备注：
搜索的脚本
1、未登录状态下搜索采购单
2、未登录状态下搜索材料
3、未登录状态下搜索采购商
4、未登录状态下搜索供应商
5、登录状态下搜索采购单
6、登录状态下搜索材料
7、登录状态下搜索采购商
8、登录状态下搜索供应商
'''

class registeTestCase(unittest.TestCase):
      def setUp(self):
          self.driver = webdriver.Chrome()
          self.driver.maximize_window()
          self.driver.get("http://www.caibab.com/member/new")
          self.driver.implicitly_wait(3)
          WebDriverWait(self.driver, 10).until(EC.title_contains("材巴巴"))

      def tearDown(self):
          self.driver.quit()

      #  用例1：供应商注册
      def test_001(self):
          value = ''.join(random.sample(string.ascii_letters + string.digits, 15))
          self.driver.find_element_by_xpath('//input[@name="account"]').send_keys(value) # 输入用户帐号
          self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('88888888') # 输入密码
          self.driver.find_element_by_xpath('//input[@name="apassword"]').send_keys('88888888') # 确认密码
          self.driver.find_element_by_xpath('//input[@placeholder="请输入联系人"]').send_keys('供应商')  # 联系人
          self.driver.find_element_by_xpath('//input[@name="mobilePhone"]').send_keys('18813675589')   # 手机号
          self.driver.find_element_by_xpath('//input[@name="supplierName"]').send_keys('我是供应商')    # 公司名称
          self.driver.find_element_by_xpath('//input[@name="mail"]').send_keys('1416778554@qq.com')   # 邮箱
          self.driver.find_element_by_xpath('//input[@name="majorIndustry"]').click()
          sleep(1)
          self.driver.find_element_by_xpath('//input[@value="21674942CAAAFDFBE050007F0100221E,人工"]').click()  # 选择人工
          self.driver.find_element_by_xpath('//div[text()="确定"]').click()
          sleep(1)
          self.driver.find_elements_by_xpath('//input[@name="file"]')[0].send_keys('E:\\132.png') # 上传图片
          js = "var q=document.documentElement.scrollTop=100000"   # 滚动条移到页面底部
          self.driver.execute_script(js)
          sleep(3)
          self.driver.find_element_by_css_selector('#registerType-B > div.text-center._1I-pTRxdSM1xdQnEzhoRNY > button').click() # 点击提交资料
          sleep(1.5)
          succese = self.driver.find_element_by_xpath('//div[text()="扫码关注材巴巴公众号"]').text
          self.assertEqual(succese,'扫码关注材巴巴公众号')

