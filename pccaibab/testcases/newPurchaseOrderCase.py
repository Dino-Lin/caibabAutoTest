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

class NewPurchaseOrderTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonLogin.CommonLogin.cjkLogin(commonLogin.CommonLogin,cls.driver)

    def tearDown(self):
        self.driver.get('http://cjk.caibab.com')

    # 用例1：已登录集采通，新建一个报名已开始的采购单
    def test_NewSignupStartedPurchaseOrder(self):
        # 点击‘招标平台’
        self.driver.find_element_by_link_text('招标平台').click()

        # 等待页面加载
        flag = common.isElementExistWithLinkText(self.driver,'采购报价')
        self.assertEqual(True,flag)

        # 点击‘采购报价’
        self.driver.find_element_by_link_text('采购报价').click()

        # 点击‘添加采购单’
        self.driver.find_element_by_link_text('添加采购单').click()

        # 输入采购单名称
        self.driver.find_element_by_name('xjd.title').send_keys('一个当前日期的采购单')

        # 选择省份,如北京
        self.driver.find_element_by_name('xjd.province').find_element_by_xpath('//option[@value="11"]').click()

        # 选择地区，如东城区
        self.driver.find_element_by_name('xjd.city').find_element_by_xpath('//option[@value="1101"]').click()

        # 输入所在地
        self.driver.find_element_by_id('addr').send_keys('望京大厦')

        # 输入公示日期，比当前时间多1分
        self.driver.find_element_by_name('xjd.publicityDate').click()  # 查找公示日期输入框
        self.driver.find_element_by_name('xjd.publicityDate').clear()  # 清除公示日期输入框的内容
        now_time = datetime.datetime.now()
        print(datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M'))
        add_minute = now_time + datetime.timedelta(minutes=1)
        sleep(2)
        real_time = datetime.datetime.strftime(add_minute,'%Y-%m-%d %H:%M')
        self.driver.find_element_by_name('xjd.publicityDate').send_keys(real_time)
        sleep(2)

        # 添加材料
        self.driver.find_element_by_xpath('//input[@value="添加材料"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('.//a[@id="mat_all"]').click()
        sleep(1)
        self.driver.find_element_by_css_selector('.btn.btn-primary.btn-xs.dialog-link-sm').click()
        sleep(1)
        self.driver.find_element_by_css_selector('.ui-button-icon-primary.ui-icon.ui-icon-closethick').click()
        sleep(3)

        # 输入工程用量
        self.driver.find_element_by_xpath('//input[@vld="{required:true,number:true}"]').send_keys("1000")
        sleep(3)

        # 提交采购单
        self.driver.find_element_by_xpath('.//input[@value="提交"]').click()

        # 发布该采购单
        self.driver.find_element_by_link_text('招标平台').click()  # 点击‘招标平台’
        flag = common.isElementExistWithLinkText(self.driver, '采购报价')  # 等待页面加载
        self.assertEqual(True, flag)
        self.driver.find_element_by_link_text('采购报价').click()    # 点击‘采购报价’
        self.driver.find_element_by_link_text('发布').click()     # 点击‘发布’
        sleep(2)  # 等待弹框出现

        # 确认发布
        a = self.driver.switch_to.alert()
        sleep(1)
        print(a.text)   # 打印弹出框文本
        a.accept()    # 确定

        # 审核该采购单
        self.driver.find_element_by_link_text('招标平台').click()  # 点击‘招标平台’
        sleep(1)
        self.driver.find_element_by_xpath('//a[@href="/xjds/auditList"]').click()   # 点击‘采购审核’
        sleep(1)
        self.driver.find_element_by_xpath('//a[text()="审核"]').click()    # 点击‘审核’
        sleep(1)
        self.driver.find_element_by_xpath('//input[@value="通过"]').click()   # 点击‘通过’
        sleep(1)


    # 用例2：已登录集采通，新建一个报名未开始的采购单
    def test_SignupNotStartPurchaseOrder(self):
        # 点击‘招标平台’
        self.driver.find_element_by_link_text('招标平台').click()

        # 等待页面加载
        flag = common.isElementExistWithLinkText(self.driver, '采购报价')
        self.assertEqual(True, flag)

        # 点击‘采购报价’
        self.driver.find_element_by_link_text('采购报价').click()

        # 点击‘添加采购单’
        self.driver.find_element_by_link_text('添加采购单').click()

        # 输入采购单名称
        self.driver.find_element_by_name('xjd.title').send_keys('一个报名未开始的采购单')

        # 选择省份,如北京
        self.driver.find_element_by_name('xjd.province').find_element_by_xpath('//option[@value="11"]').click()

        # 选择地区，如东城区
        self.driver.find_element_by_name('xjd.city').find_element_by_xpath('//option[@value="1101"]').click()

        # 输入所在地
        self.driver.find_element_by_id('addr').send_keys('望京大厦')

        # 输入公示日期，比当前时间多3天
        self.driver.find_element_by_name('xjd.publicityDate').click()  # 查找公示日期输入框
        self.driver.find_element_by_name('xjd.publicityDate').clear()  # 清除公示日期输入框的内容
        now_time = datetime.datetime.now()
        print(datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M'))
        add_minute = now_time + datetime.timedelta(days=3)
        sleep(2)
        real_time = datetime.datetime.strftime(add_minute, '%Y-%m-%d %H:%M')
        self.driver.find_element_by_name('xjd.publicityDate').send_keys(real_time)
        sleep(2)

        # 添加材料
        self.driver.find_element_by_xpath('//input[@value="添加材料"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('.//a[@id="mat_all"]').click()
        sleep(1)
        self.driver.find_element_by_css_selector('.btn.btn-primary.btn-xs.dialog-link-sm').click()
        sleep(1)
        self.driver.find_element_by_css_selector('.ui-button-icon-primary.ui-icon.ui-icon-closethick').click()
        sleep(3)

        # 输入工程用量
        self.driver.find_element_by_xpath('//input[@vld="{required:true,number:true}"]').send_keys("1000")
        sleep(3)

        # 提交采购单
        self.driver.find_element_by_xpath('.//input[@value="提交"]').click()

        # 发布该采购单
        self.driver.find_element_by_link_text('招标平台').click()  # 点击‘招标平台’
        flag = common.isElementExistWithLinkText(self.driver, '采购报价')  # 等待页面加载
        self.assertEqual(True, flag)
        self.driver.find_element_by_link_text('采购报价').click()  # 点击‘采购报价’
        self.driver.find_element_by_link_text('发布').click()  # 点击‘发布’
        sleep(2)  # 等待弹框出现

        # 确认发布
        a = self.driver.switch_to.alert()
        print(a.text)  # 打印弹出框文本
        a.accept()  # 确定

        # 审核该采购单
        self.driver.find_element_by_link_text('招标平台').click()  # 点击‘招标平台’
        sleep(1)
        self.driver.find_element_by_xpath('//a[@href="/xjds/auditList"]').click()  # 点击‘采购审核’
        sleep(1)
        self.driver.find_element_by_xpath('//a[text()="审核"]').click()  # 点击‘审核’
        sleep(1)
        self.driver.find_element_by_xpath('//input[@value="通过"]').click()  # 点击‘通过’
        sleep(1)

    # 用例3：已登录集采通，新建一个报名已截止的采购单
    def test_SignupEndPurchaseOrder(self):
        # 点击‘招标平台’
        self.driver.find_element_by_link_text('招标平台').click()

        # 等待页面加载
        flag = common.isElementExistWithLinkText(self.driver, '采购报价')
        self.assertEqual(True, flag)

        # 点击‘采购报价’
        self.driver.find_element_by_link_text('采购报价').click()

        # 点击‘添加采购单’
        self.driver.find_element_by_link_text('添加采购单').click()

        # 输入采购单名称
        self.driver.find_element_by_name('xjd.title').send_keys('@@一个报名已截止的采购单@@')

        # 选择省份,如北京
        self.driver.find_element_by_name('xjd.province').find_element_by_xpath('//option[@value="11"]').click()

        # 选择地区，如东城区
        self.driver.find_element_by_name('xjd.city').find_element_by_xpath('//option[@value="1101"]').click()

        # 输入所在地
        self.driver.find_element_by_id('addr').send_keys('望京大厦')

        # 输入公示日期，比当前时间多1分钟
        self.driver.find_element_by_name('xjd.publicityDate').click()  # 查找公示日期输入框
        self.driver.find_element_by_name('xjd.publicityDate').clear()  # 清除公示日期输入框的内容
        now_time = datetime.datetime.now()
        print(datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M'))
        add_minute = now_time + datetime.timedelta(minutes=1)
        print(add_minute)
        sleep(1)
        real_time = datetime.datetime.strftime(add_minute,'%Y-%m-%d %H:%M')
        self.driver.find_element_by_name('xjd.publicityDate').send_keys(real_time)
        sleep(1)

        # 输入报价截止时间，比当前时间多2分钟
        # self.driver.find_element_by_name('xjd.endDt').click()  # 查找输入报价截止时间输入框
        self.driver.find_element_by_name('xjd.endDt').clear()  # 清除输入报价截止时间输入框的内容
        # ele1 = self.driver.find_element_by_name("xjd.endDt")
        # self.driver.execute_script('arguments[0].click()', ele1)
        now_time = datetime.datetime.now()
        print(datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M'))
        add_minute = now_time + datetime.timedelta(minutes=2)
        print(add_minute)
        sleep(1)
        real_time = datetime.datetime.strftime(add_minute, '%Y-%m-%d %H:%M')
        self.driver.find_element_by_xpath('//input[@name="xjd.endDt"]').send_keys(real_time)
        sleep(1)
        # 添加材料
        self.driver.find_element_by_xpath('//input[@value="添加材料"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('.//a[@id="mat_all"]').click()
        sleep(1)
        self.driver.find_element_by_css_selector('.btn.btn-primary.btn-xs.dialog-link-sm').click()
        sleep(1)
        self.driver.find_element_by_css_selector('.ui-button-icon-primary.ui-icon.ui-icon-closethick').click()
        sleep(1)

        # 输入工程用量
        self.driver.find_element_by_xpath('//input[@vld="{required:true,number:true}"]').send_keys("1000")
        sleep(1)

        # 提交采购单
        self.driver.find_element_by_xpath('.//input[@value="提交"]').click()

        # 发布该采购单
        self.driver.find_element_by_link_text('招标平台').click()  # 点击‘招标平台’
        flag = common.isElementExistWithLinkText(self.driver, '采购报价')  # 等待页面加载
        self.assertEqual(True, flag)
        self.driver.find_element_by_link_text('采购报价').click()  # 点击‘采购报价’
        sleep(1)
        # self.driver.find_element_by_link_text('发布').click()  # 点击‘发布’
        self.driver.find_element_by_xpath('//a[text()="发布"]').click()
        sleep(1)  # 等待弹框出现

        # 确认发布
        a = self.driver.switch_to.alert()
        print(a.text)  # 打印弹出框文本
        a.accept()  # 确定
        sleep(1)

        # 审核该采购单
        self.driver.find_element_by_link_text('招标平台').click()  # 点击‘招标平台’
        sleep(1)
        self.driver.find_element_by_xpath('//a[@href="/xjds/auditList"]').click()  # 点击‘采购审核’
        sleep(1)
        self.driver.find_element_by_xpath('//a[text()="审核"]').click()  # 点击‘审核’
        sleep(1)
        self.driver.find_element_by_xpath('//input[@value="通过"]').click()  # 点击‘通过’
        sleep(60)
    def tearDown(self):
        self.driver.get('http://www.caibab.com/purchase_orders')
        sleep(3)



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()



