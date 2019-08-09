import sys
sys.path.append("../")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils import common
from time import sleep
import datetime

# 公用的功能:
# 集采通发布招募供应商，然后后台审核
# 新建招募供应商
# 新建招募供应商

class CommonFunction:
            # 集采通发布招募供应商，然后后台审核
            def newRecruitSuppliers(self,driver):
                self.driver = driver
                self.driver.maximize_window()
                self.driver.get("http://cjk.caibab.com")  # 打开网站
                self.driver.implicitly_wait(2)
                WebDriverWait(self.driver, 10).until(EC.title_contains("易材通"))  # 输入账号密码
                self.driver.find_element_by_xpath('//*[@name="loginName"]').send_keys('whwh')
                self.driver.find_element_by_xpath('//input[@id="password"]').send_keys('888888')# 输入校验码qwer
                self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')# 点击登录
                self.driver.find_element_by_class_name('btn-orange').click()
                self.driver.find_element_by_link_text('招标平台').click()  # 点击’招标平台‘
                self.driver.find_element_by_xpath('//a[text()="招募供应商"]').click()  # 点击‘招募供应商’
                self.driver.find_element_by_xpath('//a[text()="新建招募"]').click()  # 点击‘新建招募供应商’
                self.driver.find_element_by_xpath('//*[@id="activityTitle"]').send_keys('广轻大厦第三期装修工程')  # 填写招募名称
                self.driver.find_element_by_xpath('//input[@id="contacts"]').send_keys('广轻大厦物业')  # 填写联系人
                self.driver.find_element_by_xpath('//input[@id="tel"]').send_keys('15678964553')  # 填写联系电话
                now_time = datetime.datetime.now()  # 获取当前时间
                start = now_time + datetime.timedelta(minutes=1)  # 招募开始时间
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

                # cgcoms后台审核
                self.driver.execute_script("window.open('http://cgcoms.caibab.com/login.do')")  # 切换到后台
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到最新打开的窗口（cgcoms）
                self.driver.find_element_by_xpath('//input[@name="loginName"]').clear()
                self.driver.find_element_by_xpath('//input[@name="password"]').clear()
                self.driver.find_element_by_xpath('//input[@name="loginName"]').send_keys('admin')  # 输入账号密码
                self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('111111')
                self.driver.find_element_by_xpath('//a[text()="登录"]').click()  # 点击登录
                self.driver.find_elements_by_xpath('//*[text()="活动管理"]')[0].click()  # 点击活动管理
                self.driver.find_elements_by_xpath('//*[text()="活动管理"]')[1].click()  # 点击第二层级的活动管理
                self.driver.find_element_by_xpath('//*[text()="招募活动审核"]').click()  # 点击招募活动审核
                iframe = self.driver.find_element_by_xpath('//iframe[@src="/activity/listY?&kitId=asdsadsa"]')
                self.driver.switch_to.frame(iframe)
                sleep(3)
                self.driver.find_elements_by_xpath('//a[text()="审核"]')[6].click()  # 审核
                self.driver.find_element_by_xpath('//a[text()="通过"]').click()  # 通过

            # 新建招募供应商
            def aRecruitSuppliers(self,driver):
                self.driver = driver
                self.driver.maximize_window()
                self.driver.get("http://cjk.caibab.com")  # 打开网站
                self.driver.implicitly_wait(2)
                WebDriverWait(self.driver, 10).until(EC.title_contains("易材通"))  # 输入账号密码
                self.driver.find_element_by_xpath('//*[@name="loginName"]').clear()
                self.driver.find_element_by_xpath('//input[@id="password"]').clear()  # 输入校验码qwer
                self.driver.find_element_by_xpath('//*[@name="loginName"]').send_keys('whwh')
                self.driver.find_element_by_xpath('//input[@id="password"]').send_keys('888888')# 输入校验码qwer
                self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')# 点击登录
                self.driver.find_element_by_class_name('btn-orange').click()
                sleep(5)
                self.driver.find_element_by_link_text('招标平台').click()  # 点击’招标平台‘
                self.driver.find_element_by_xpath('//a[text()="招募供应商"]').click()  # 点击‘招募供应商’
                self.driver.find_element_by_xpath('//a[text()="新建招募"]').click()  # 点击‘新建招募供应商’
                self.driver.find_element_by_xpath('//*[@id="activityTitle"]').send_keys('测试供应商报名时间')  # 填写招募名称
                self.driver.find_element_by_xpath('//input[@id="contacts"]').send_keys('广轻大厦物业')  # 填写联系人
                self.driver.find_element_by_xpath('//input[@id="tel"]').send_keys('15678964553')  # 填写联系电话

            # 后台审核招募供应商活动模块
            def cgcomsExamineRecruitSuppliers(self,driver):
                self.driver.execute_script("window.open('http://cgcoms.caibab.com/login.do')")  # 切换到后台
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到最新打开的窗口（cgcoms）
                self.driver.find_element_by_xpath('//input[@name="loginName"]').clear()
                self.driver.find_element_by_xpath('//input[@name="password"]').clear()
                self.driver.find_element_by_xpath('//input[@name="loginName"]').send_keys('admin')  # 输入账号密码
                self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('111111')
                self.driver.find_element_by_xpath('//a[text()="登录"]').click()  # 点击登录
                self.driver.find_elements_by_xpath('//*[text()="活动管理"]')[0].click()  # 点击活动管理
                self.driver.find_elements_by_xpath('//*[text()="活动管理"]')[1].click()  # 点击第二层级的活动管理
                self.driver.find_element_by_xpath('//*[text()="招募活动审核"]').click()  # 点击招募活动审核
                iframe = self.driver.find_element_by_xpath('//iframe[@src="/activity/listY?&kitId=asdsadsa"]')
                self.driver.switch_to.frame(iframe)
                sleep(3)
                self.driver.find_elements_by_xpath('//a[text()="审核"]')[6].click()  # 审核
                self.driver.find_element_by_xpath('//a[text()="通过"]').click()  # 通过
                self.driver.close()

            # 供应商报名
            def registration(self,driver):
                self.driver.execute_script("window.open('http://www.caibab.com')")
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.find_element_by_xpath('//*[text()="登录"]')
                self.driver.find_element_by_xpath('//input[@placeholder="请输入账号名"]').send_keys('cgs111')  # 账号密码
                self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('12345678')
                self.driver.find_element_by_xpath('//button[text()="登录"]').click()  # 登录
                self.driver.find_elements_by_xpath('//a[text()="集采招募"]')[1].click()  # 点击集采招募
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
                self.driver.find_elements_by_xpath('//a[text()="立即报名"]')[0].click()  # 点击立即报名按钮
                self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换最新
                self.driver.find_element_by_css_selector('#activity-view > div._16_z2Kz8dbTY_XKw4iGuoH > div._1Bo2SNifE5tV-PuQtQC6wH > div.fs37qwgeiCKDX3eL-01Tr > div > button').click()
                sleep(1)

            # 新建一个集中采购招募单
            def new(self,driver):
                self.driver = driver
                self.driver.maximize_window()
                self.driver.get("http://cjk.caibab.com")  # 打开网站
                self.driver.implicitly_wait(2)
                WebDriverWait(self.driver, 10).until(EC.title_contains("易材通"))  # 输入账号密码
                self.driver.find_element_by_xpath('//*[@name="loginName"]').send_keys('whwh')
                self.driver.find_element_by_xpath('//input[@id="password"]').send_keys('888888')
                self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')  # 输入校验码qwer
                self.driver.find_element_by_class_name('btn-orange').click()   # 点击 登录
                self.driver.find_element_by_xpath('//a[text()="招标平台"]').click()    # 点击 招标平台
                self.driver.find_element_by_xpath('//a[text()="集中采购"]').click()     # 点击 集中采购
                self.driver.find_element_by_xpath('//a[text()="新建集中采购"]').click()   # 点击  新建集中采购
                self.driver.find_element_by_xpath('//input[@id="activityTitle"]').send_keys('@这是一个集中采购')  # 输入标题
                self.driver.find_element_by_xpath('//input[@id="activitySum"]').send_keys('500')   # 输入活动总金额
                self.driver.find_element_by_xpath('//input[@id="contacts"]').send_keys('材总')   # 输入联系人
                self.driver.find_element_by_xpath('//input[@id="tel"]').send_keys('13800138000')
                now_time = datetime.datetime.now()
                end = now_time + datetime.timedelta(days=7)  # 招募结束时间
                end = datetime.datetime.strftime(end, '%Y-%m-%d %H:%M')  # 格式化
                self.driver.find_element_by_xpath('//input[@id="activityEndDt"]').send_keys(end)
                self.driver.find_element_by_xpath('//input[@id="uploadFile1"]').send_keys('C:/Users/bijp/Desktop/picture/222222.png')   # 上传图片
                self.driver.find_element_by_xpath('//input[@value="确定"]').click()   # 确定
                self.driver.find_elements_by_xpath('//a[@href="#"]')[3].click()    # 发布
                self.driver.find_element_by_xpath('//a[@class="layui-layer-btn0"]').click()   # 确定

            # 后台审核新建的集中采购单
            def examineCentralizeProcurement(self,driver):
                self.driver = driver
                self.driver.get('http://cgcoms.caibab.com')
                #self.driver.execute_script("window.open('http://cgcoms.caibab.com')")
                self.driver.implicitly_wait(2)
                self.driver.find_element_by_xpath('//input[@name="loginName"]').send_keys('admin')  # 输入账号密码
                self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('111111')
                # self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')  # 输入校验码qwer
                self.driver.find_element_by_xpath('//a[text()="登录"]').click()    # 点击登录
                self.driver.find_elements_by_xpath('//*[text()="活动管理"]')[0].click()  # 点击活动管理
                self.driver.find_elements_by_xpath('//*[text()="活动管理"]')[1].click()  # 点击第二层级的活动管理
                self.driver.find_elements_by_xpath('//span[text()="集采活动管理"]')[0].click()  # 点击集采活动管理
                ifrme = self.driver.find_element_by_xpath('//iframe[@src="/activity/listN?acttype=B&kitId=activityN"]')
                self.driver.switch_to.frame(ifrme)
                sleep(2)
                self.driver.find_element_by_xpath('//a[text()="审核"]').click()    # 审核
                sleep(2)
                self.driver.find_element_by_xpath('//a[text()="通过"]').click()   # 通过
                sleep(1)
                self.driver.close()


