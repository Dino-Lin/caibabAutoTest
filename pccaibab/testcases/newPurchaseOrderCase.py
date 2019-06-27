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

class NewPurchaseOrderTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonLogin.CommonLogin.cjkLogin(commonLogin.CommonLogin,cls.driver)

    def tearDown(self):
        self.driver.get('http://cjk.caibab.com')

    # 用例：已登录集采通，新建一个公示日期为当日期的采购单
    def test_newCurrentDatePurchaseOrder(self):
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

        # 公示日期自行填写，建议填写当前日期过几分的时间,如显示器的时间为2010-06-26 15：40，则输入2019-06-26 16:00
        self.driver.find_element_by_name('xjd.publicityDate').click()
        self.driver.find_element_by_name('xjd.publicityDate').clear()
        self.driver.find_element_by_name('xjd.publicityDate').send_keys('2019-06-27 16:50')

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
        a = self.driver.switch_to_alert()
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

    def tearDown(self):
        self.driver.get('http://www.caibab.com/purchase_orders')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()



