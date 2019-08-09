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


# 备注：
# 集采招募报名脚本
# 用例1：供应商已登录（已认证）  test_001
# 用例2：供应商已登录（未认证）  test_002
# 用例3：供应商未登录          test_003
# 用例4：账号为采购商          test_004

class RecruitSuppliersTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonFunction.CommonFunction.newRecruitSuppliers(commonFunction.CommonFunction,cls.driver)

    # 用例1：供应商已登录（已认证）,报名招募供应商
    def test_001(self):
        # 登录材巴巴平台报名招募供应商
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换第一个窗口
        sleep(3)
        self.driver.find_element_by_xpath('//a[text()="材巴巴采购平台"]').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        self.driver.find_elements_by_xpath('//a[text()="登录"]')[0].click()
        sleep(2)
        self.driver.find_element_by_xpath('//input[@placeholder="请输入账号名"]').send_keys('huahua123456') # 账号密码
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('huahua123456')
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()   # 登录
        self.driver.find_elements_by_xpath('//a[text()="集采招募"]')[1].click()   # 点击集采招募
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        self.driver.find_elements_by_xpath('//a[text()="立即报名"]')[0].click()    #点击立即报名按钮
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        self.driver.find_element_by_css_selector('#activity-view > div._16_z2Kz8dbTY_XKw4iGuoH > div._1Bo2SNifE5tV-PuQtQC6wH > div.fs37qwgeiCKDX3eL-01Tr > div > button').click()
        self.driver.find_element_by_xpath('//a[text()="立即报名"]').click()
        self.driver.close()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[3])
        sleep(1)
        self.driver.close()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[2])
        sleep(1)
        # 退出登录操作：鼠标悬停显示二级菜单，再点击二级菜单或下拉列表
        # 步骤1：使用find_element_by_xpath找到顶级菜单，并将鼠标移动到上面
        article = self.driver.find_element_by_xpath('//a[@class="orange-color"]')
        ActionChains(self.driver).move_to_element(article).perform()
        # 步骤2：使用find_element_by_xpath找到二级菜单，并点击
        log_out = self.driver.find_element_by_xpath('//a[text()="退出登录"]')
        log_out.click()
        sleep(1)
        self.driver.close()

    # 用例2： 供应商已登录（未认证）
    def test_002(self):
        # 登录材巴巴平台报名招募供应商
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换第一个窗口
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="材巴巴采购平台"]').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        sleep(1)
        self.driver.find_elements_by_xpath('//a[text()="登录"]')[0].click()
        self.driver.find_element_by_xpath('//input[@placeholder="请输入账号名"]').send_keys('gys233')  # 账号密码
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('12345678')
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()  # 登录
        self.driver.find_elements_by_xpath('//a[text()="集采招募"]')[1].click()  # 点击集采招募
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        self.driver.find_elements_by_xpath('//a[text()="立即报名"]')[0].click()  # 点击立即报名按钮
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        sleep(3)
        self.driver.find_element_by_css_selector('#activity-view > div._16_z2Kz8dbTY_XKw4iGuoH > div._1Bo2SNifE5tV-PuQtQC6wH > div.fs37qwgeiCKDX3eL-01Tr > div > button').click()
        sleep(3)
        note = self.driver.find_element_by_xpath('//*[text()="您的账号正在审核中,请耐心等待..."]').text
        self.assertEqual(note, '您的账号正在审核中,请耐心等待...')
        self.driver.close()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[3])
        sleep(1)
        self.driver.close()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[2])
        sleep(1)
        # 退出登录操作：鼠标悬停显示二级菜单，再点击二级菜单或下拉列表
        # 步骤1：使用find_element_by_xpath找到顶级菜单，并将鼠标移动到上面
        article = self.driver.find_element_by_xpath('//a[@class="orange-color"]')
        ActionChains(self.driver).move_to_element(article).perform()
        # 步骤2：使用find_element_by_xpath找到二级菜单，并点击
        log_out = self.driver.find_element_by_xpath('//a[text()="退出登录"]')
        log_out.click()
        sleep(1)
        self.driver.close()

    # 用例3：供应商未登录
    def test_003(self):
        # 在材巴巴平台报名招募供应商
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换第一个窗口
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="材巴巴采购平台"]').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        sleep(1)
        self.driver.find_elements_by_xpath('//a[text()="集采招募"]')[1].click()  # 点击集采招募
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        self.driver.find_elements_by_xpath('//a[text()="立即报名"]')[0].click()    #点击立即报名按钮
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        sleep(2)
        self.driver.find_element_by_css_selector('#activity-view > div._16_z2Kz8dbTY_XKw4iGuoH > div._1Bo2SNifE5tV-PuQtQC6wH > div.fs37qwgeiCKDX3eL-01Tr > div > button').click()  # 点击立即报名按钮
        sleep(1)
        note = self.driver.find_element_by_xpath('//*[text()="材巴巴会员"]').text
        self.assertEqual(note,'材巴巴会员')
        self.driver.close()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[3])
        sleep(1)
        self.driver.close()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[2])
        sleep(1)
        self.driver.close()


    #  用例4：账号为采购商
    def test_004(self):
        # 登录材巴巴平台报名招募供应商
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换第一个窗口
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="材巴巴采购平台"]').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        sleep(2)
        self.driver.find_elements_by_xpath('//a[text()="登录"]')[0].click()
        sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder="请输入账号名"]').send_keys('cgs111') # 账号密码
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('12345678')
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()   # 登录
        self.driver.find_elements_by_xpath('//a[text()="集采招募"]')[1].click()   # 点击集采招募
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        self.driver.find_elements_by_xpath('//a[text()="立即报名"]')[0].click()    #点击立即报名按钮
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
        self.driver.find_element_by_css_selector('#activity-view > div._16_z2Kz8dbTY_XKw4iGuoH > div._1Bo2SNifE5tV-PuQtQC6wH > div.fs37qwgeiCKDX3eL-01Tr > div > button').click()
        sleep(1)
        note = self.driver.find_element_by_xpath('//*[text()="该活动只允许供应商参加"]').text
        self.assertEqual(note,"该活动只允许供应商参加")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()



