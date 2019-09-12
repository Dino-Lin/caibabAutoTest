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

'''
1、普通采购商的忘记密码
2、商城的忘记密码
3、普通供应商账号的忘记密码
'''

class FindPasswordTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.caibab.com")
        self.driver.implicitly_wait(3)
        WebDriverWait(self.driver, 10).until(EC.title_contains("材巴巴"))
        self.driver.find_element_by_xpath("//a[@class='orange-color']").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("passport"))
        # self.driver.find_element_by_xpath('//a[text()="登录"]').click()
        self.driver.find_element_by_xpath('//a[text()="忘记登录密码?"]').click()

    def tearDown(self):
        self.driver.quit()

    '''1、普通采购商的忘记密码'''
    def test_001(self):
                ''' 找回密码'''
                self.driver.find_element_by_xpath('//input[@name="account"]').send_keys('caigoushang1') # 用户名
                self.driver.find_element_by_xpath('//input[@name="mobilePhone"]').send_keys('18813759943')  # 手机号
                self.driver.find_element_by_xpath('//input[@value="下一步"]').click()   # 下一步
                sleep(1)
                self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')
                self.driver.find_element_by_xpath('//input[@value="下一步"]').click()   # 下一步
                sleep(1)
                ''' 输入新密码'''
                self.driver.find_element_by_xpath('//input[@placeholder="请输入新密码"]').send_keys('88888888')
                self.driver.find_element_by_xpath('//input[@placeholder="请再次输入密码"]').send_keys('88888888')
                self.driver.find_element_by_xpath('//input[@value="下一步"]').click()   # 下一步
                sleep(1)
                '''验证:用新密码登录'''
                self.driver.find_element_by_xpath('//input[@id="username"]').clear()
                self.driver.find_element_by_xpath('//input[@id="username"]').send_keys('caigoushang1')
                self.driver.find_element_by_xpath('//input[@id="password"]').clear()
                self.driver.find_element_by_xpath('//input[@id="password"]').send_keys('88888888')
                self.driver.find_element_by_xpath('//button[text()="登录"]').click()

    '''2、商城的忘记密码'''
    def test_002(self):
                self.driver.find_element_by_xpath('//input[@name="account"]').send_keys('hm')  # 用户名
                self.driver.find_element_by_xpath('//input[@name="mobilePhone"]').send_keys('13376555455')  # 手机号
                self.driver.find_element_by_xpath('//input[@value="下一步"]').click()  # 下一步
                sleep(1)
                self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')
                self.driver.find_element_by_xpath('//input[@value="下一步"]').click()  # 下一步
                sleep(1)
                ''' 输入新密码'''
                self.driver.find_element_by_xpath('//input[@placeholder="请输入新密码"]').send_keys('88888888')
                self.driver.find_element_by_xpath('//input[@placeholder="请再次输入密码"]').send_keys('88888888')
                self.driver.find_element_by_xpath('//input[@value="下一步"]').click()  # 下一步
                sleep(1)
                '''验证:用新密码登录'''
                self.driver.find_element_by_xpath('//input[@id="username"]').clear()
                self.driver.find_element_by_xpath('//input[@id="username"]').send_keys('hm')
                self.driver.find_element_by_xpath('//input[@id="password"]').clear()
                self.driver.find_element_by_xpath('//input[@id="password"]').send_keys('88888888')
                self.driver.find_element_by_xpath('//button[text()="登录"]').click()

    '''3、普通供应商账号的忘记密码'''
    def test_003(self):
                self.driver.find_element_by_xpath('//input[@name="account"]').send_keys('huahua1234')  # 用户名
                self.driver.find_element_by_xpath('//input[@name="mobilePhone"]').send_keys('18813759900')  # 手机号
                self.driver.find_element_by_xpath('//input[@value="下一步"]').click()  # 下一步
                sleep(1)
                self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')
                self.driver.find_element_by_xpath('//input[@value="下一步"]').click()  # 下一步
                sleep(1)
                ''' 输入新密码'''
                self.driver.find_element_by_xpath('//input[@placeholder="请输入新密码"]').send_keys('88888888')
                self.driver.find_element_by_xpath('//input[@placeholder="请再次输入密码"]').send_keys('88888888')
                self.driver.find_element_by_xpath('//input[@value="下一步"]').click()  # 下一步
                sleep(1)
                '''验证:用新密码登录'''
                self.driver.find_element_by_xpath('//input[@id="username"]').clear()
                self.driver.find_element_by_xpath('//input[@id="username"]').send_keys('huahua1234')
                self.driver.find_element_by_xpath('//input[@id="password"]').clear()
                self.driver.find_element_by_xpath('//input[@id="password"]').send_keys('88888888')
                self.driver.find_element_by_xpath('//button[text()="登录"]').click()




