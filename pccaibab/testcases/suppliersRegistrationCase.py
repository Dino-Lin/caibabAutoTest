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
# 招募供应商时间问题脚本
# 用例1：在招募供应商活动开始之前报名
# 用例2：招募开始报名
# 用例3：招募时间已结束


class suppliersRegistrationCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonFunction.CommonFunction.aRecruitSuppliers(commonFunction.CommonFunction,cls.driver)

    #  用例1：在招募供应商活动开始之前报名
    def test_001(self):
                now_time = datetime.datetime.now()  # 获取当前时间
                start = now_time + datetime.timedelta(days=3)  # 招募开始时间
                end = now_time + datetime.timedelta(days=7)  # 招募结束时间
                start = datetime.datetime.strftime(start, '%Y-%m-%d %H:%M')  # 格式化
                end = datetime.datetime.strftime(end, '%Y-%m-%d %H:%M')  # 格式化
                self.driver.find_element_by_xpath('//input[@id="activityStartDt"]').send_keys(start)  # 填写开始时间
                self.driver.find_element_by_xpath('//input[@id = "activityEndDt"]').send_keys(end)  # 填写结束时间
                self.driver.find_element_by_xpath('//input[@class="recruit-name-input"]').send_keys('水泥')  # 招募品类
                self.driver.find_element_by_xpath('//input[@id="itemNameSum"]').send_keys('2000')  # 年计划采购金额
                self.driver.find_element_by_xpath('//*[@value="确定"]').click()  # 确定
                self.driver.find_elements_by_xpath('//a[@href="#"]')[3].click()  # 发布
                self.driver.find_element_by_xpath('// a[text() = "确定"]').click()  # div弹窗 确定发布
                sleep(1)
                commonFunction.CommonFunction.cgcomsExamineRecruitSuppliers(commonFunction.CommonFunction,self.driver) # 后台审核
                sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])
                js = 'window.open("https://www.baidu.com");'  # 通过执行js，开启一个新的窗口
                self.driver.execute_script(js)
                self.driver.switch_to.window(self.driver.window_handles[1])
                commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin,self.driver)   # 供应商报名
                self.driver.find_elements_by_xpath('//a[text()="集采招募"]')[1].click()  # 点击集采招募
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
                self.driver.find_elements_by_xpath('//*[text()="查看详情"]')[0].click()  # 点击立即报名按钮
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
                button = self.driver.find_element_by_xpath('//*[@id="activity-view"]/div[2]/div[1]/div[2]/div/button').text   # 断言
                self.assertEqual(button,"报名未开始")
                # 退出登录操作：鼠标悬停显示二级菜单，再点击二级菜单或下拉列表
                # 步骤1：使用find_element_by_xpath找到顶级菜单，并将鼠标移动到上面
                article = self.driver.find_element_by_xpath('//a[@class="orange-color"]')
                ActionChains(self.driver).move_to_element(article).perform()
                # 步骤2：使用find_element_by_xpath找到二级菜单，并点击
                log_out = self.driver.find_element_by_xpath('//a[text()="退出登录"]')
                log_out.click()
                sleep(1)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[2])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()
                sleep(1)

    # 用例2：招募开始报名
    def test_002(self):
                self.driver.switch_to.window(self.driver.window_handles[0])
                commonFunction.CommonFunction.aRecruitSuppliers(commonFunction.CommonFunction, self.driver)
                now_time = datetime.datetime.now()  # 获取当前时间
                start = now_time + datetime.timedelta(minutes=1)  # 招募开始时间
                end = now_time + datetime.timedelta(days=7)  # 招募结束时间
                start = datetime.datetime.strftime(start, '%Y-%m-%d %H:%M')  # 格式化
                end = datetime.datetime.strftime(end, '%Y-%m-%d %H:%M')  # 格式化
                self.driver.find_element_by_xpath('//input[@id="activityStartDt"]').send_keys(start)  # 填写开始时间
                self.driver.find_element_by_xpath('//input[@id = "activityEndDt"]').send_keys(end)  # 填写结束时间
                self.driver.find_element_by_xpath('//input[@class="recruit-name-input"]').send_keys('钢筋')  # 招募品类
                self.driver.find_element_by_xpath('//input[@id="itemNameSum"]').send_keys('5000')  # 年计划采购金额
                self.driver.find_element_by_xpath('//*[@value="确定"]').click()  # 确定
                self.driver.find_elements_by_xpath('//a[@href="#"]')[3].click()  # 发布
                self.driver.find_element_by_xpath('// a[text() = "确定"]').click()  # div弹窗 确定发布
                sleep(1)
                commonFunction.CommonFunction.cgcomsExamineRecruitSuppliers(commonFunction.CommonFunction,self.driver) # 后台审核
                sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.switch_to.window(self.driver.window_handles[0])
                js = 'window.open("https://www.baidu.com");'  # 通过执行js，开启一个新的窗口
                self.driver.execute_script(js)
                self.driver.switch_to.window(self.driver.window_handles[1])
                commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin,self.driver)   # 供应商报名
                self.driver.find_elements_by_xpath('//a[text()="集采招募"]')[1].click()  # 点击集采招募
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
                sleep(2)
                self.driver.find_elements_by_xpath('//*[text()="立即报名"]')[0].click()  # 点击立即报名按钮
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
                self.driver.find_element_by_css_selector('#activity-view > div._16_z2Kz8dbTY_XKw4iGuoH > div._1Bo2SNifE5tV-PuQtQC6wH > div.fs37qwgeiCKDX3eL-01Tr > div > button').click()  # 点击‘立即报名’
                self.driver.find_element_by_xpath('//a[text()="立即报名"]').click()       # 确认报名
                sleep(3)
                # 退出登录操作：鼠标悬停显示二级菜单，再点击二级菜单或下拉列表
                # 步骤1：使用find_element_by_xpath找到顶级菜单，并将鼠标移动到上面
                article = self.driver.find_element_by_xpath('//a[@class="orange-color"]')
                ActionChains(self.driver).move_to_element(article).perform()
                # 步骤2：使用find_element_by_xpath找到二级菜单，并点击
                log_out = self.driver.find_element_by_xpath('//a[text()="退出登录"]')
                log_out.click()
                sleep(1)
                self.driver.close()
                sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()

    # 用例3：招募时间已结束
    def test_003(self):
                self.driver.switch_to.window(self.driver.window_handles[0])
                commonFunction.CommonFunction.aRecruitSuppliers(commonFunction.CommonFunction, self.driver)
                now_time = datetime.datetime.now()  # 获取当前时间
                start = now_time + datetime.timedelta(minutes=1)  # 招募开始时间
                end = now_time + datetime.timedelta(minutes=2)  # 招募结束时间
                start = datetime.datetime.strftime(start, '%Y-%m-%d %H:%M')  # 格式化
                end = datetime.datetime.strftime(end, '%Y-%m-%d %H:%M')  # 格式化
                self.driver.find_element_by_xpath('//input[@id="activityStartDt"]').send_keys(start)  # 填写开始时间
                self.driver.find_element_by_xpath('//input[@id = "activityEndDt"]').send_keys(end)  # 填写结束时间
                self.driver.find_element_by_xpath('//input[@class="recruit-name-input"]').send_keys('木头')  # 招募品类
                self.driver.find_element_by_xpath('//input[@id="itemNameSum"]').send_keys('3000')  # 年计划采购金额
                self.driver.find_element_by_xpath('//*[@value="确定"]').click()  # 确定
                self.driver.find_elements_by_xpath('//a[@href="#"]')[3].click()  # 发布
                self.driver.find_element_by_xpath('// a[text() = "确定"]').click()  # div弹窗 确定发布
                sleep(1)
                commonFunction.CommonFunction.cgcomsExamineRecruitSuppliers(commonFunction.CommonFunction, self.driver)  # 后台审核
                sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])
                js = 'window.open("https://www.baidu.com");'  # 通过执行js，开启一个新的窗口
                self.driver.execute_script(js)
                self.driver.switch_to.window(self.driver.window_handles[1])
                sleep(100)
                commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin, self.driver)  # 供应商报名
                self.driver.find_elements_by_xpath('//a[text()="集采招募"]')[1].click()  # 点击集采招募
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
                self.driver.find_elements_by_xpath('//*[text()="查看详情"]')[0].click()  # 点击立即报名按钮
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
                button_2 = self.driver.find_element_by_xpath('//*[@id="activity-view"]/div[2]/div[1]/div[2]/div/button').text  # 断言
                self.assertEqual(button_2, "报名已结束")
                # 退出登录操作：鼠标悬停显示二级菜单，再点击二级菜单或下拉列表
                # 步骤1：使用find_element_by_xpath找到顶级菜单，并将鼠标移动到上面
                article = self.driver.find_element_by_xpath('//a[@class="orange-color"]')
                ActionChains(self.driver).move_to_element(article).perform()
                # 步骤2：使用find_element_by_xpath找到二级菜单，并点击
                log_out = self.driver.find_element_by_xpath('//a[text()="退出登录"]')
                log_out.click()
                sleep(1)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[2])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()
                sleep(1)




