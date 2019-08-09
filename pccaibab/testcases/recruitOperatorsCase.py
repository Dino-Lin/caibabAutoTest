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
# 在材巴巴平台运营商入驻的脚本
# 用例1：运营商公司申请入驻报名


class recruitOperatorsCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.caibab.com/index/sellerRegison#yysRegister")

    #  用例1：运营商公司申请入驻报名
    def test_001(self):
        value = ''.join(random.sample(string.ascii_letters + string.digits, 15))
        self.driver.find_element_by_xpath('//input[@name="name"]').send_keys(value)  #随机输入公司名字
        self.driver.find_element_by_xpath('//input[@name="cnames"]').send_keys('材总')  # 输入联系人
        self.driver.find_element_by_xpath('//input[@name="uniqueCode"]').send_keys('18813758876')   # 输入手机号
        self.driver.find_element_by_xpath('//input[@name="inviteAccount"]').send_keys('广州')
        self.driver.find_element_by_xpath('//input[@name="inviteCode"]').send_keys('1416785332@qq.com')   # 联系邮箱
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()   # 点击立即申请
        sleep(1)
        texta = self.driver.find_element_by_xpath('//ul[@class="clearfix"]').text
        self.assertEqual(texta,'申请成功!')


        # 登录后台管理系统审核运营商
        commonLogin.CommonLogin.cgcomsLogin(commonLogin.CommonLogin,self.driver)
        sleep(1)
        self.driver.find_element_by_xpath('//span[text()="运营管理"]').click()   # 点击运营管理
        sleep(1)
        self.driver.find_element_by_xpath('//span[text()="运营商"]').click()    # 点击运营商
        self.driver.find_element_by_xpath('//span[text()="运营商审核"]').click()   # 点击运营商审核
        iframe = self.driver.find_element_by_xpath('//iframe[@src="/drm/seller/auditList?kitId=drm-seller-audit-list"]')
        self.driver.switch_to.frame(iframe)
        sleep(2)
        self.driver.find_elements_by_xpath('//a[@data-title="运营商审核"]')[0].click()   #  点击审核
        account = ''.join(random.sample(string.ascii_letters + string.digits, 20))
        self.driver.find_element_by_xpath('//input[@name="account"]').send_keys(account)
        self.driver.find_element_by_xpath('//select[@name="roleId"]').find_element_by_xpath('//option[@data-code="yysrole"]').click()   # 选择运营商角
        sleep(1)
        self.driver.find_elements_by_xpath('//input[@name="sex"]')[0].click()   # 性别男
        self.driver.find_element_by_xpath('//input[@name="channelName"]').send_keys('材巴巴')
        code = account = ''.join(random.sample(string.ascii_letters + string.digits, 25))
        self.driver.find_element_by_xpath('//input[@name="channelCode"]').send_keys(code)  #
        self.driver.find_element_by_xpath('//input[@value="通过"]').click()   # 通过
        success = self.driver.find_element_by_xpath('//*[text()="审核成功，默认密码88888888！"]').text
        self.assertEqual(success,"审核成功，默认密码88888888！")
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()



