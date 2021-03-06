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
import datetime

# 备注：已登录和未登录情况下是否可以报价采购单和竞价单
# 用例1：已登录，报价采购单
# 用例2：未登录，报价采购单
# 用例3：已登录，报价竞价单
# 用例4，未登录，报价竞价单

class loginStatusTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    '''用例1、供应商已登录，报价采购单'''
    def test_001(self):
        commonFunction.CommonFunction.purchaseOrder(commonFunction.CommonFunction.purchaseOrder, self.driver)   # 发布采购单并审核
        self.driver.execute_script('window.open("http://www.caibab.com/")')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin,self.driver)  # 供应商登录
        sleep(60)
        self.driver.find_elements_by_xpath('//a[text()="采购清单"]')[1].click()   # 点击采购清单
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//a[text()="立即报价"]').click()  #点击立即报价
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(1)
        self.driver.refresh()
        self.driver.find_element_by_xpath('//a[text()="立即报价"]').click()   #点击立即报价
        sleep(2)
        self.driver.find_element_by_xpath('//input[@name="items[${idx.index}].extBrand1"]').send_keys('万豪') # 输入品牌
        self.driver.find_element_by_xpath('//input[@name="items[${idx.index}].extPrice1"]').send_keys('2000') # 报价
        self.driver.find_element_by_xpath('//button[text()="提交报价信息"]').click()   # 提交
        self.driver.switch_to.window(self.driver.window_handles[-1]) # 返回最新页面
        real = self.driver.find_element_by_xpath('//*[text()="一个当前日期的采购单"]').text
        self.assertEqual(real, '一个当前日期的采购单')  # 断言
        self.driver.quit()

    '''用例2：供应商未登录，报价采购单'''
    def test_002(self):
        commonFunction.CommonFunction.purchaseOrder(commonFunction.CommonFunction.purchaseOrder,self.driver)  # 发布采购单并审核
        self.driver.execute_script('window.open("http://www.caibab.com/")')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(60)
        self.driver.find_elements_by_xpath('//a[text()="采购清单"]')[1].click()  # 点击采购清单
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//a[text()="立即报价"]').click()  # 点击立即报价
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #self.driver.find_element_by_xpath('//a[text()="立即报价"]').send_keys(Keys.ENTER)
        sleep(1)
        self.driver.find_element_by_xpath('//a[text()="立即报价"]').click()   #点击立即报价
        sleep(1)
        value = self.driver.find_element_by_xpath('//p[text()="该信息仅支持材巴巴注册会员查看，您可通过下方进行会员注册、登录。感谢您对材巴巴的关注！"]').text
        self.assertEqual(value,"该信息仅支持材巴巴注册会员查看，您可通过下方进行会员注册、登录。感谢您对材巴巴的关注！")
        self.driver.quit()

    '''用例3：供应商已登录，报价竞价单'''
    def test_003(self):
        commonFunction.CommonFunction.new_a_bidding_list(commonFunction.CommonFunction.new_a_bidding_list, self.driver)
        self.driver.execute_script("window.open('http://baidu.com')")  # 新建一个选项卡，打开cgcoms后台
        current_handle = self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到最新打开的窗口（cgcoms）
        commonFunction.CommonFunction.exam_a_bidding_list(commonFunction.CommonFunction.exam_a_bidding_list,self.driver)  # 审核竞价单
        self.driver.close()  # 关闭后台

        # 登录材巴巴
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到集采通
        self.driver.execute_script('window.open("https://www.baidu.com")')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin, self.driver)  # 供应商登录材巴巴
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div/div/div/div/ul/li[2]/div/div/ul/li[1]/a').click()  # 点击采购清单
        # 获取采购清单列表窗口句柄
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.refresh()
        self.driver.find_element_by_xpath('//a[text()="参与竞价"]').click()  # 点击参与竞价
        # 获得竞价单详情页窗口句柄
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到竞价单详情页
        # 点击立即报名
        self.driver.find_element_by_css_selector(
            '#root > div > div > div.wrap > div.clearfix.row > div.right._3wabwNSbYm9Vib0y4vqTw8 > div._1jipg0fO-gmd-AP4EX2eNy > div:nth-child(4) > div > div > a').click()
        # 报名然后确定
        self.driver.find_element_by_xpath('//button[text()="报名"]').click()
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()

        # cgcoms后台审核竞价报名
        self.driver.execute_script('window.open("https://www.baidu.com")')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        commonFunction.CommonFunction.exam_bidding_list_enroll(commonFunction.CommonFunction.exam_bidding_list_enroll,
                                                               self.driver)  # 审核竞价单

        # 切换到竞价单详情页
        self.driver.switch_to.window(self.driver.window_handles[3])
        # 点击查看竞价大厅
        self.driver.find_element_by_xpath('//a[text()="查看竞价大厅"]').click()

        # 点击’正式竞价‘-----首轮竞价
        sleep(80)  # 等待页面到点刷新
        self.driver.refresh()  # 刷新竞价单详情窗口
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="正式竞价"]')))  # 等待元素出现
        self.driver.find_element_by_xpath('//*[text()="正式竞价"]').click()
        self.driver.find_element_by_xpath('// input[ @ placeholder = "请输入单价"]').send_keys('2000')  # 输入报价
        self.driver.find_element_by_xpath('//button[text()="提交报价"]').click()  # 提交

        # 点击’正式竞价‘-----次轮竞价
        sleep(130)
        self.driver.refresh()  # 刷新页面
        self.driver.find_element_by_xpath('//*[text()="正式竞价"]').click()
        self.driver.find_element_by_xpath('// input[ @ placeholder = "请输入单价"]').send_keys('999')  # 输入报价
        self.driver.find_element_by_xpath('//button[text()="提交报价"]').click()  # 提交

        # 点击‘正式竞价’-----末轮竞价
        sleep(110)
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[text()="正式竞价"]').click()
        self.driver.find_element_by_xpath('// input[ @ placeholder = "请输入单价"]').send_keys('888')  # 输入报价
        self.driver.find_element_by_xpath('//button[text()="提交报价"]').click()  # 提交
        sleep(1)

        # 页面切换回集采通
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(0.5)

        # 选择中标
        self.driver.find_element_by_xpath('//a[@id="bjdsButton"]').click()  # 点击左边功能栏的’选择中标‘
        self.driver.refresh()
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="竞价清单"]').click()  # 点击’竞价清单‘
        self.driver.refresh()
        sleep(0.5)
        self.driver.find_elements_by_xpath('//a[text()="编辑"]')[0].click()  # 点击’编辑‘
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="竞价信息"]').click()  # 点击’竞价信息‘
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="中标"]').click()  # 选择第一个供应商，中标
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()  # 确定
        sleep(0.5)

        # 中标采购
        self.driver.find_element_by_xpath('//a[@href="/cgd/list"]').click()  # 点击功能栏的’中标采购
        self.driver.find_elements_by_xpath('//a[text()="操作"]')[0].click()  # 点击第一个竞价单的操作按钮
        self.driver.find_element_by_xpath('//input[@value="提交"]').click()  # 点击‘提交’按钮
        self.driver.switch_to.alert.accept()  # 确认弹框

    '''用例4：供应商未登录，报价竞价单'''
    def test_004(self):
        commonFunction.CommonFunction.new_a_bidding_list(commonFunction.CommonFunction.new_a_bidding_list, self.driver)
        self.driver.execute_script("window.open('http://baidu.com')")  # 新建一个选项卡，打开cgcoms后台
        current_handle = self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到最新打开的窗口（cgcoms）
        commonFunction.CommonFunction.exam_a_bidding_list(commonFunction.CommonFunction.exam_a_bidding_list,self.driver)  # 审核竞价单
        self.driver.close()  # 关闭后台
        # 登录材巴巴
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到集采通
        self.driver.execute_script('window.open("http://www.caibab.com/")')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin, self.driver)  # 供应商登录材巴巴
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div/div/div/div/ul/li[2]/div/div/ul/li[1]/a').click()  # 点击采购清单
        # 获取采购清单列表窗口句柄
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.refresh()
        self.driver.find_element_by_xpath('//a[text()="参与竞价"]').click()  # 点击参与竞价
        # 获得竞价单详情页窗口句柄
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到竞价单详情页
        # 点击立即报名
        self.driver.find_element_by_css_selector('#root > div > div > div.wrap > div.clearfix.row > div.right._3wabwNSbYm9Vib0y4vqTw8 > div._1jipg0fO-gmd-AP4EX2eNy > div:nth-child(4) > div > div > a').click()
        # 断言
        value = self.driver.find_element_by_xpath('//*[text()="该信息仅支持材巴巴注册会员查看，您可通过下方进行会员注册、登录。感谢您对材巴巴的关注！"]').text
        self.assertEqual(value,'该信息仅支持材巴巴注册会员查看，您可通过下方进行会员注册、登录。感谢您对材巴巴的关注！')

