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


# 备注：
# 注册的脚本
# 用例1：供应商注册
# 用例2：采购商注册
# 用例3：集采通注册


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

      # 用例2：采购商注册
      def test_002(self):
          self.driver.find_element_by_xpath('//li[text()="采购商注册"]').click()
          value = ''.join(random.sample(string.ascii_letters + string.digits, 15))
          self.driver.find_element_by_xpath('//input[@name="account"]').send_keys(value)  # 输入用户帐号
          self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('88888888')  # 输入密码
          self.driver.find_element_by_xpath('//input[@name="apassword"]').send_keys('88888888')  # 确认密码
          self.driver.find_element_by_xpath('//input[@placeholder="您的公司名称"]').send_keys('我是采购商')
          self.driver.find_element_by_xpath('//select[@name="purchaseType"]').find_element_by_xpath('//option[@value="施工企业"]').click()   # 选择类型
          self.driver.find_element_by_xpath('//input[@placeholder="您的公司地址"]').send_keys('广州越秀区广轻大厦')
          self.driver.find_element_by_xpath('//input[@placeholder="您的公司邮箱"]').send_keys('1416784330@qq.com')
          self.driver.find_element_by_xpath('//input[@placeholder="您的姓名"]').send_keys('材巴巴')
          self.driver.find_element_by_xpath('//input[@placeholder="您的手机号"]').send_keys('18813678865')
          self.driver.find_element_by_xpath('//input[@type="checkbox"]').click()
          self.driver.find_element_by_css_selector('#registerType-C > div.text-center._1I-pTRxdSM1xdQnEzhoRNY > button').click()
          sleep(1)
          succese = self.driver.find_element_by_xpath('//div[text()="扫码关注材巴巴公众号"]').text
          self.assertEqual(succese,'扫码关注材巴巴公众号')

      # 用例3：集采通注册
      def test_003(self):
          self.driver.find_element_by_xpath('//li[text()="集采通注册"]').click()
          self.driver.find_element_by_xpath('//input[@placeholder="请输入企业名称"]').send_keys('我是集采通')
          self.driver.find_element_by_xpath('//select[@name="purchaserType"]').find_element_by_xpath('//option[@value="装饰设计"]').click()
          self.driver.find_element_by_xpath('//input[@placeholder="请输入姓名"]').send_keys('材总')  #  决策人姓名
          self.driver.find_element_by_xpath('//input[@placeholder="请输入联系方式"]').send_keys('18813675587')  # 联系方式
          self.driver.find_element_by_xpath('//input[@placeholder="请输入职务名称"]').send_keys('经理')   # 决策人职务
          self.driver.find_element_by_xpath('//input[@placeholder="请输入邮箱联系方式"]').send_keys('1415668883@qq.com')   # 邮箱
          self.driver.find_element_by_xpath('//input[@type="checkbox"]').click()
          self.driver.find_elements_by_xpath('//a[@href="javascript:;"]')[-1].click()
          sleep(1)
          succese = self.driver.find_element_by_xpath('//p[text()="您的资料已提交，请耐心等待审核结果"]').text
          self.assertEqual(succese, '您的资料已提交，请耐心等待审核结果')
          sleep(1)