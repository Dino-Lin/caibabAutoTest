import sys
sys.path.append("../")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import common
from commons import  commonLogin
from time import sleep
import datetime

'''
公用的功能:
1、集采通发布招募供应商，然后后台审核
2、集采通新建招募供应商
3、后台审核招募供应商活动模块
4、供应商在材巴巴平台报名集采招募
5、采购商新建一个集中采购招募单
6、cgcoms后台审核新建的集中采购单
7、采购商发布一个采购单并审核
8、供应商在材巴巴平台报价
9、采购商添加一个竞价单
10、cgcoms后台审核竞价的报名
'''


class CommonFunction:
            #1、集采通发布招募供应商，然后后台审核
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

            # 2、集采通新建招募供应商
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

            #3、后台审核招募供应商活动模块
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

            # 4、供应商在材巴巴平台报名集采招募
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

            # 5、采购商新建一个集中采购招募单
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

            # 6、cgcoms后台审核集中采购单
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

            #  7、采购商发布一个采购单并审核
            def purchaseOrder(self,driver):
                self.driver = driver
                commonLogin.CommonLogin.cjkLogin(commonLogin.CommonLogin.cjkLogin,self.driver)
                # 点击‘招标平台’
                self.driver.find_element_by_link_text('招标平台').click()
                # flag = common.isElementExistWithLinkText(self.driver, '采购报价') # 等待页面加载
                # self.assertEqual(True, flag)
                self.driver.find_element_by_link_text('采购报价').click()   # 点击‘采购报价’
                self.driver.find_element_by_link_text('添加采购单').click()  # 点击‘添加采购单’
                self.driver.find_element_by_name('xjd.title').send_keys('一个当前日期的采购单')   # 输入采购单名称
                self.driver.find_element_by_name('xjd.province').find_element_by_xpath('//option[@value="11"]').click()  # 选择省份,如北京
                self.driver.find_element_by_name('xjd.city').find_element_by_xpath('//option[@value="1101"]').click()   # 选择地区，如东城区
                self.driver.find_element_by_id('addr').send_keys('望京大厦')    # 输入所在地
                # 输入公示日期，比当前时间多1分
                self.driver.find_element_by_name('xjd.publicityDate').click()  # 查找公示日期输入框
                self.driver.find_element_by_name('xjd.publicityDate').clear()  # 清除公示日期输入框的内容
                now_time = datetime.datetime.now()
                print(datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M'))
                add_minute = now_time + datetime.timedelta(minutes=1)
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
                self.driver.find_element_by_xpath('//input[@vld="{required:true,number:true}"]').send_keys("1000")  # 输入工程用量
                sleep(3)
                self.driver.find_element_by_xpath('.//input[@value="提交"]').click()  # 提交采购单

                # 发布该采购单
                self.driver.find_element_by_link_text('招标平台').click()  # 点击‘招标平台’
                # flag = common.isElementExistWithLinkText(self.driver, '采购报价')  # 等待页面加载
                # self.assertEqual(True, flag)
                self.driver.find_element_by_link_text('采购报价').click()  # 点击‘采购报价’
                self.driver.find_element_by_link_text('发布').click()  # 点击‘发布’
                sleep(2)  # 等待弹框出现

                # 确认发布
                self.driver.switch_to.alert.accept()

                # 审核该采购单
                self.driver.find_element_by_link_text('招标平台').click()  # 点击‘招标平台’
                sleep(1)
                self.driver.find_element_by_xpath('//a[@href="/xjds/auditList"]').click()  # 点击‘采购审核’
                sleep(1)
                self.driver.find_element_by_xpath('//a[text()="审核"]').click()  # 点击‘审核’
                sleep(1)
                self.driver.find_element_by_xpath('//input[@value="通过"]').click()  # 点击‘通过’
                sleep(1)

            #  8、集采通新建竞价单
            def new_a_bidding_list(self, driver):
                self.driver = driver
                commonLogin.CommonLogin.cjkLogin(commonLogin.CommonLogin.cjkLogin, self.driver)
                self.driver.find_element_by_link_text('招标平台').click()  # 点击‘招标平台’
                sleep(2)
                # flag = common.isElementExistWithLinkText(self.driver, '采购报价') # 断言
                # self.assertEqual(True, flag)
                self.driver.find_element_by_link_text('采购报价').click()  # 点击‘采购报价’
                self.driver.find_element_by_xpath('//a[text()="竞价清单"]').click()  # 点击‘竞价清单’
                self.driver.find_element_by_xpath('//a[text()="添加竞价单"]').click()  # 点击‘添加竞价单’
                self.driver.find_element_by_name('xjd.title').send_keys('可以报名的竞价单')  # 输入‘竞价单名称’
                # 选择所属项目
                self.driver.find_element_by_xpath('//select[@name="xjd.project.id"]').find_element_by_xpath('//option[@value="4028827e64f82b8f0164f888963a0001"]').click()

                now_time = datetime.datetime.now()
                add_one_start = now_time + datetime.timedelta(minutes=2)  # 首轮竞价开始时间
                add_one_end = now_time + datetime.timedelta(minutes=3)  # 首轮竞价结束时间
                add_two_start = now_time + datetime.timedelta(minutes=4)  # 次轮竞价开始时间
                add_two_end = now_time + datetime.timedelta(minutes=5)  # 次轮竞价结束时间
                add_three_start = now_time + datetime.timedelta(minutes=6)  # 末轮竞价开始时间
                add_three_end = now_time + datetime.timedelta(minutes=7)  # 末轮竞价结束时间

                time_one_start = datetime.datetime.strftime(add_one_start, '%Y-%m-%d %H:%M')
                time_one_end = datetime.datetime.strftime(add_one_end, '%Y-%m-%d %H:%M')
                time_two_start = datetime.datetime.strftime(add_two_start, '%Y-%m-%d %H:%M')
                time_two_end = datetime.datetime.strftime(add_two_end, '%Y-%m-%d %H:%M')
                time_three_start = datetime.datetime.strftime(add_three_start, '%Y-%m-%d %H:%M')
                time_three_end = datetime.datetime.strftime(add_three_end, '%Y-%m-%d %H:%M')

                # 首轮竞价开始时间
                self.driver.find_element_by_xpath('//input[@name="bidNoStartDt0"]').send_keys(time_one_start)
                # 首轮竞价结束时间
                self.driver.find_element_by_xpath('//input[@name="bidNoEndDt0"]').send_keys(time_one_end)
                sleep(2)

                # 次轮竞价开始时间
                self.driver.find_element_by_xpath('//input[@name="bidNoStartDt1"]').send_keys(time_two_start)
                # 先写入 触发js自动写入时间 再清除写入时间
                self.driver.find_element_by_xpath('//input[@name="bidNoStartDt1"]').clear()
                self.driver.find_element_by_xpath('//input[@name="bidNoStartDt1"]').send_keys(time_two_start)
                sleep(2)

                # 次轮竞价结束时间
                self.driver.find_element_by_xpath('//input[@name="bidNoEndDt1"]').send_keys(time_two_end)
                sleep(2)

                # 末轮竞价开始时间
                self.driver.find_element_by_xpath('//input[@name="bidNoStartDt2"]').send_keys(time_three_start)
                # 先写入 触发js自动写入时间 再清除写入时间
                self.driver.find_element_by_xpath('//input[@name="bidNoStartDt2"]').clear()
                self.driver.find_element_by_xpath('//input[@name="bidNoStartDt2"]').send_keys(time_three_start)
                sleep(2)

                # 末轮竞价结束时间
                self.driver.find_element_by_xpath('//input[@name="bidNoEndDt2"]').send_keys(time_three_end)
                sleep(2)
                self.driver.find_element_by_xpath('//input[@value="添加材料"]').click()   # 点击‘添加材料’
                self.driver.find_element_by_xpath('//a[@id="mat_all"]').click()   # 点击‘全部’
                self.driver.find_elements_by_xpath('//input[@type="submit" and @value="添加"]')[0].click()   # 选择材料，点击‘添加’按钮
                self.driver.find_elements_by_class_name('ui-icon-closethick')[0].click()   # 关闭当前窗口
                num = '1000'
                self.driver.find_element_by_xpath('//*[@id="item_tb"]/tbody/tr[2]/td[5]/input').send_keys(num)   # 输入‘工程用量’
                self.driver.find_element_by_xpath('//input[@value="提交"]').click()    # 提交竞价单
                self.driver.find_element_by_xpath('//a[text()="发布"]').click()    # 发布
                a = self.driver.switch_to.alert   # 切换到弹窗，确认发布
                print(a.text)  # 打印弹出框文本
                a.accept()  # 确定

            #  9、后台审核竞价单
            def exam_a_bidding_list(self, driver):
                self.driver = driver
                commonLogin.CommonLogin.cgcomsLogin(commonLogin.CommonLogin.cgcomsLogin, self.driver)   # 登录
                # 点击采购管理之后点击采购审核
                self.driver.find_element_by_xpath('//span[text()="采购管理"]').click()  # 点击采购管理
                self.driver.find_element_by_xpath('//span[text()="采购审核"]').click()  # 点击采购审核
                # sleep(2)
                # self.driver.find_element_by_xpath('//*[@id="auditlist"]/span').click()   # 点击审核
                WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="auditlist"]/span')))
                self.driver.find_element_by_xpath('//*[@id="auditlist"]/span').click()
                # 进入iframe
                element2 = self.driver.find_element_by_xpath('//iframe[@src="/purchaserCompeteOrder/auditList?kitId=purchaser-competeOrder-auditlist"]')
                self.driver.switch_to.frame(element2)  
                self.driver.find_elements_by_xpath('//a[@data-title="竞价单审核"]')[0].click()   # 点击审核
                self.driver.find_element_by_xpath('//input[@value="通过"]').click()  # 审核通过

            #  10、cgcoms后台审核竞价的报名
            def exam_bidding_list_enroll(self, driver):
                self.driver = driver
                commonLogin.CommonLogin.cgcomsLogin(commonLogin.CommonLogin.cgcomsLogin, self.driver) # 登录
                # 点击采购管理之后点击采购审核
                self.driver.find_element_by_xpath('//span[text()="采购管理"]').click()  # 点击采购管理
                self.driver.find_element_by_xpath('//span[text()="采购审核"]').click()  # 点击采购审核
                #WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="auditApply"]/i')))
                self.driver.find_element_by_xpath('//*[@id="auditApply"]/i').click()  # 点击’竞价单报名审核‘
                #element3 = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[3]/iframe')  # 切换到iframe
                iframe = self.driver.find_element_by_xpath('//iframe[@src="/purchaserCompeteOrder/orderApplyList?kitId=purchaser-competeOrder-auditApply"]')
                self.driver.switch_to.frame(iframe)  # 切换到iframe
                sleep(0.5)
                self.driver.find_elements_by_xpath('//a[text()="通过"]')[0].click()  # 点击通过
                sleep(2)
                self.driver.find_element_by_xpath('//a[text()="确定"]').click()  # 确定
                sleep(1)
               





