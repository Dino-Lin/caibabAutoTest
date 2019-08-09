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
from selenium.webdriver.common.keys import Keys
import datetime

# 备注：这是一个新建竞价单，供应商报价竞价单的用例

class NewBiddingListTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonLogin.CommonLogin.cjkLogin(commonLogin.CommonLogin,cls.driver)


    # 用例1：已登录集采通，新建一个竞价单
    def test_NewBiddingListOrder(self):
        # 点击‘招标平台’
        self.driver.find_element_by_link_text('招标平台').click()

        # 断言
        flag = common.isElementExistWithLinkText(self.driver,'采购报价')
        self.assertEqual(True,flag)

        # 点击‘采购报价’
        self.driver.find_element_by_link_text('采购报价').click()

        # 点击‘竞价清单’
        self.driver.find_element_by_xpath('//a[text()="竞价清单"]').click()

        # 点击‘添加竞价单’
        self.driver.find_element_by_xpath('//a[text()="添加竞价单"]').click()

        # 输入‘竞价单名称’
        self.driver.find_element_by_name('xjd.title').send_keys('可以报名的竞价单')

        # 选择所属项目
        self.driver.find_element_by_xpath('//select[@name="xjd.project.id"]').find_element_by_xpath('//option[@value="4028827e64f82b8f0164f888963a0001"]').click()


        now_time = datetime.datetime.now()

        add_one_start = now_time + datetime.timedelta(minutes=2)  # 首轮竞价开始时间
        add_one_end = now_time + datetime.timedelta(minutes=3)    # 首轮竞价结束时间
        add_two_start = now_time + datetime.timedelta(minutes=4)  # 次轮竞价开始时间
        add_two_end = now_time + datetime.timedelta(minutes=5)    # 次轮竞价结束时间
        add_three_start = now_time + datetime.timedelta(minutes=6)  # 末轮竞价开始时间
        add_three_end = now_time + datetime.timedelta(minutes=7)    # 末轮竞价结束时间

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
        #先写入 触发js自动写入时间 再清除写入时间
        self.driver.find_element_by_xpath('//input[@name="bidNoStartDt1"]').clear()
        self.driver.find_element_by_xpath('//input[@name="bidNoStartDt1"]').send_keys(time_two_start)
        sleep(2)

        # 次轮竞价结束时间
        self.driver.find_element_by_xpath('//input[@name="bidNoEndDt1"]').send_keys(time_two_end)
        sleep(2)

        # 末轮竞价开始时间
        self.driver.find_element_by_xpath('//input[@name="bidNoStartDt2"]').send_keys(time_three_start)
        #先写入 触发js自动写入时间 再清除写入时间
        self.driver.find_element_by_xpath('//input[@name="bidNoStartDt2"]').clear()
        self.driver.find_element_by_xpath('//input[@name="bidNoStartDt2"]').send_keys(time_three_start)
        sleep(2)

        # 末轮竞价结束时间
        self.driver.find_element_by_xpath('//input[@name="bidNoEndDt2"]').send_keys(time_three_end)
        sleep(2)


        # 点击‘添加材料’
        self.driver.find_element_by_xpath('//input[@value="添加材料"]').click()

        # 点击‘全部’
        self.driver.find_element_by_xpath('//a[@id="mat_all"]').click()

        # 选择材料，点击‘添加’按钮
        self.driver.find_elements_by_xpath('//input[@type="submit" and @value="添加"]')[0].click()

        # 关闭当前窗口
        self.driver.find_elements_by_class_name('ui-icon-closethick')[0].click()

        # 输入‘工程用量’
        num = '1000'
        self.driver.find_element_by_xpath('//*[@id="item_tb"]/tbody/tr[2]/td[5]/input').send_keys(num)

        # 提交竞价单
        self.driver.find_element_by_xpath('//input[@value="提交"]').click()

        # 发布
        self.driver.find_element_by_xpath('//a[text()="发布"]').click()

        # 确认发布
        a = self.driver.switch_to.alert
        print(a.text)   # 打印弹出框文本
        a.accept()    # 确定
        print('*****************显示分割线********************')

        # 获得易材通窗口句柄
        cjk_window = self.driver.current_window_handle
        print('窗口1  易材通窗口：'+cjk_window)

        # ******断言*******

        # **************************后台审核竞价单*********************************

        # 新建一个选项卡，打开cgcoms后台
        self.driver.execute_script("window.open('http://cgcoms.caibab.com/login.do')")
        current_handle = self.driver.current_window_handle

        # 切换到最新打开的窗口（cgcoms）
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # 获得后台窗口句柄
        cgcoms_window = self.driver.current_window_handle
        print('窗口2  cgcoms后台窗口：' + cgcoms_window)
        self.driver.implicitly_wait(2)

        # 输入账号密码
        self.driver.find_element_by_xpath('//input[@name="loginName"]').send_keys('admin')
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('111111')

        # 输入校验码qwer
        # self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')

        # 点击登录
        self.driver.find_element_by_xpath('//a[text()="登录"]').click()

        # 点击采购管理之后点击采购审核
        self.driver.find_element_by_xpath('//span[text()="采购管理"]').click()  # 点击采购管理
        self.driver.find_element_by_xpath('//span[text()="采购审核"]').click()   # 点击采购审核
        # sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="auditlist"]/span').click()   # 点击审核
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="auditlist"]/span')))
        self.driver.find_element_by_xpath('//*[@id="auditlist"]/span').click()
        #进入iframe
        element2 = self.driver.find_element_by_xpath('//iframe[@src="/purchaserCompeteOrder/auditList?kitId=purchaser-competeOrder-auditlist"]')
        self.driver.switch_to.frame(element2)

        # 点击审核
        self.driver.find_elements_by_xpath('//a[@data-title="竞价单审核"]')[0].click()

        # 审核通过
        self.driver.find_element_by_xpath('//input[@value="通过"]').click()

        #   ***********************后台审核竞价单完毕*************************

        # 切换到前一个窗口（cjk）
        self.driver.switch_to.window(self.driver.window_handles[0])
        current_handle = self.driver.current_window_handle

        # 点击材巴巴采购平台
        self.driver.find_element_by_xpath('//a[text()="材巴巴采购平台"]').click()

        # 自动新建了窗口，页面跳转至材巴巴平台，切换到才巴巴平台
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 获得材巴巴平台窗口句柄
        caibab_window = self.driver.current_window_handle
        print('窗口3  材巴巴平台窗口：' + caibab_window)
        sleep(0.5)

        # 登录材巴巴平台
        self.driver.find_element_by_xpath('//a[text()="登录"]').click()  # 登录材巴巴平台
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(1)
        self.driver.find_element_by_name('username').send_keys('huahua123456')  # 账号
        self.driver.find_element_by_name('password').send_keys('huahua123456')  # 密码
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()  # 登录

        # 点击采购清单
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div/div/div/div/ul/li[2]/div/div/ul/li[1]/a').click()

        # 获取采购清单列表窗口句柄
        self.driver.switch_to.window(self.driver.window_handles[-1])
        oders_window = self.driver.current_window_handle
        print('窗口4  采购清单列表窗口：' + oders_window)

        # 点击参与竞价
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//a[text()="参与竞价"]').click()

        # 获得竞价单详情页窗口句柄
        self.driver.switch_to.window(self.driver.window_handles[-1])   # 切换到竞价单详情页
        biding_window = self.driver.current_window_handle
        print('窗口5  竞价单详情页窗口:' + biding_window)

        # 点击立即报名
        self.driver.find_element_by_css_selector('#root > div > div > div.wrap > div.clearfix.row > div.right._3wabwNSbYm9Vib0y4vqTw8 > div._1jipg0fO-gmd-AP4EX2eNy > div:nth-child(4) > div > div > a').click()

        # 报名然后确定
        self.driver.find_element_by_xpath('//button[text()="报名"]').click()
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()

        # 打印窗口
        handle_list = self.driver.window_handles
        print(handle_list)

        # cgcoms后台审核竞价报名
        self.driver.switch_to.window(self.driver.window_handles[1])    # 转换到后台
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="auditApply"]/i').click()  # 点击’竞价单审核‘
        element3 = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[3]/iframe')  # 切换到iframe
        self.driver.switch_to.frame(element3)  # 切换到iframe
        sleep(0.5)
        self.driver.find_elements_by_xpath('//a[text()="通过"]')[0].click()  # 点击通过
        sleep(2)
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()         # 确定
        sleep(1)

        # 切换到竞价单详情页
        self.driver.switch_to.window(self.driver.window_handles[4])
        # 点击查看竞价大厅
        self.driver.find_element_by_xpath('//a[text()="查看竞价大厅"]').click()

        # 点击’正式竞价‘-----首轮竞价
        sleep(80)   # 等待页面到点刷新
        self.driver.refresh()  # 刷新竞价单详情窗口
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[text()="正式竞价"]')))  # 等待元素出现
        self.driver.find_element_by_xpath('//*[text()="正式竞价"]').click()
        self.driver.find_element_by_xpath('// input[ @ placeholder = "请输入单价"]').send_keys('2000')   # 输入报价
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
        self.driver.find_elements_by_xpath('//a[text()="编辑"]')[0].click()    # 点击’编辑‘
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="竞价信息"]').click()     # 点击’竞价信息‘
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="中标"]').click()        # 选择第一个供应商，中标
        sleep(0.5)
        self.driver.find_element_by_xpath('//a[text()="确定"]').click()           # 确定
        sleep(0.5)

        # 中标采购
        self.driver.find_element_by_xpath('//a[@href="/cgd/list"]').click()     # 点击功能栏的’中标采购
        self.driver.find_elements_by_xpath('//a[text()="操作"]')[0].click()      # 点击第一个竞价单的操作按钮
        self.driver.find_element_by_xpath('//input[@value="提交"]').click()       # 点击‘提交’按钮
        self.driver.switch_to.alert.accept()        # 确认弹框

        #  货款管理
        self.driver.find_element_by_xpath('//a[@href="/payment/list"]')           # 点击左边功能栏的‘货款管理’
        self.driver.find_element_by_xpath('//*[@id="pageForm"]/div[2]/div[1]/table/tbody/tr[2]/td[8]/a').click()    # 点击‘收’,跑不过
        self.driver.find_element_by_xpath('//input[@name="shdItems[0].num"]').send_keys(num)
        self.driver.find_element_by_xpath('//input[@value="提交"]').click()    # 提交

        # 在中标采购中，完成竞价单
        self.driver.find_element_by_xpath('//a[@href="/cgd/list"]').click()  # 点击功能栏的’中标采购
        self.driver.find_elements_by_xpath('//a[text()="操作"]')[0].click()  # 点击第一个竞价单的操作按钮
        self.driver.find_element_by_xpath('//input[@value="提交"]').click()   # 点击‘采购完成’
        sleep(0.5)

        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()














