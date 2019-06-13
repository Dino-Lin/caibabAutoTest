import sys
sys.path.append('../')
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils import common
from commons import commonLogin
'''产品购买用例'''
class ProductPurchaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonLogin.CommonLogin.cgsLogin(commonLogin.CommonLogin, cls.driver)
    def test_minBuy(self):
        '''低于最小购买量'''
        self.driver.find_element_by_xpath('//*[@id="headMenu"]/div/ul/li[2]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div/div/ul/li[1]/div/a[1]/span').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/a').click() #点击购买
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[4]/div[1]/a[2]').click()
        alert = self.driver.switch_to.alert
        self.assertEqual('不能低于最少购买量',alert.text)
        alert.accept()
        self.driver.switch_to.default_content()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(10)
    def test_maxBuy(self):
        '''高于最大购买量'''
        self.driver.find_element_by_xpath('//*[@id="headMenu"]/div/ul/li[2]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div/div/ul/li[1]/div/a[1]/span').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/a').click() #点击购买
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[4]/div[1]/input').send_keys(99999)
        alert = self.driver.switch_to.alert
        self.assertEqual('不能大于供货总量',alert.text)
        alert.accept()
        self.driver.switch_to.default_content()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    def test_normalBuy(self):
        '''正常购买步骤'''
        self.driver.find_element_by_xpath('//*[@id="headMenu"]/div/ul/li[2]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div/div/ul/li[1]/div/a[1]/span').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[2]/a').click() #点击购买
        num = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[3]/div[1]/input')
        num.click()
        num.clear()
        num.send_keys(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[3]/div[2]/a[2]').click()
        if (common.isElementExist(self.driver,'//*[@id="root"]/div/div[2]/div/div[2]/div[2]/ul/li/span[4]/a[1]')):
            print('存在送货地址，不需要新增')
        else:
            print('没有送货地址，新增一个送货地址')
            self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[1]/a[1]').click()
            button = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[10]/div[2]/div/div/div[2]/div/div[1]/div/div[1]')
            ActionChains(self.driver).move_to_element(button).perform()
            province = self.driver.find_element_by_link_text("广东省")
            ActionChains(self.driver).move_to_element(province).perform()
            city = self.driver.find_element_by_link_text("广州市")
            ActionChains(self.driver).move_to_element(city).perform()
            city.click()
            self.driver.find_element_by_name('contacter').send_keys("材巴巴")
            self.driver.find_element_by_name('addr').send_keys("盘福路888号7楼")
            self.driver.find_element_by_name('phone').send_keys("18888888888")
            self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[10]/div[2]/div/div/div[2]/div/div[6]/a[1]').click()
        price1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[9]/div[1]/div[4]/span').text
        payType = self.driver.find_element_by_name('payType')
        payType.find_element_by_xpath("//option[@value='A']").click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[3]/div[3]/span/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[3]/span/a').click()
        self.driver.find_element_by_name('remark').send_keys('123123123213123213123213')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[9]/div[2]/button').click() #提交产品购买
        frame1 = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/iframe')
        self.driver.switch_to.frame(frame1)
        sleep(1)
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[1]/div[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="form1"]/dl/dd[1]/input').send_keys('123')
        self.driver.find_element_by_xpath('//*[@id="form1"]/dl/dd[2]/input').click()
        self.driver.switch_to.default_content()
        sleep(1)
        frame2 = self.driver.find_element_by_xpath('/html/body/div[4]/iframe')
        self.driver.switch_to.frame(frame2)
        sleep(1)
        self.driver.find_element_by_id('dpTodayInput').click()
        self.driver.switch_to.default_content()
        sleep(1)
        self.driver.switch_to.frame(frame1)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="form1"]/dl/dd[4]/input').send_keys('321')
        self.driver.find_element_by_xpath('//*[@id="form1"]/div/button[1]').click()
        price2 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[9]/div[3]/div/p[2]/span').text #新增付款单，提交
        self.assertEqual(price1, price2)
        self.driver.switch_to.default_content()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    def test_addAndBuy(self):
        '''添加进货单后购买'''
        self.driver.find_element_by_xpath('//*[@id="headMenu"]/div/ul/li[2]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div/div/ul/li[1]/div/a[1]/span').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[2]/a').click()  # 点击购买
        num = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[3]/div[1]/input')
        num.click()
        num.clear()
        num.send_keys(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[3]/div[2]/a[1]').click() #点击加入进货单
        self.driver.find_element_by_link_text('去结算').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[3]/div/div[1]/label/input').click()
        sleep(1)
        self.driver.find_element_by_link_text('提交').click()
        if (common.isElementExist(self.driver, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/ul/li/span[4]/a[1]')):
            print('存在送货地址，不需要新增')
        else:
            print('没有送货地址，新增一个送货地址')
            self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[1]/a[1]').click()
            button = self.driver.find_element_by_xpath( '//*[@id="root"]/div/div[2]/div/div[10]/div[2]/div/div/div[2]/div/div[1]/div/div[1]')
            ActionChains(self.driver).move_to_element(button).perform()
            province = self.driver.find_element_by_link_text("广东省")
            ActionChains(self.driver).move_to_element(province).perform()
            city = self.driver.find_element_by_link_text("广州市")
            ActionChains(self.driver).move_to_element(city).perform()
            city.click()
            self.driver.find_element_by_name('contacter').send_keys("材巴巴")
            self.driver.find_element_by_name('addr').send_keys("盘福路888号7楼")
            self.driver.find_element_by_name('phone').send_keys("18888888888")
            self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[10]/div[2]/div/div/div[2]/div/div[6]/a[1]').click()
        price1 = self.driver.find_element_by_class_name("kVghzsx9F7vxFasMLuuu7").text
        payType = self.driver.find_element_by_name('payType')
        payType.find_element_by_xpath("//option[@value='A']").click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[3]/div[3]/span/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[3]/span/a').click()
        self.driver.find_element_by_name('remark').send_keys('123123123213123213123213')
        self.driver.find_element_by_css_selector('#root > div > div.wrap.clearfix > div > div._3CQoR6V6nspzW2VH1pMYba > button').click()  # 提交产品购买
        sleep(2)
        frame1 = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/iframe')
        self.driver.switch_to.frame(frame1)
        sleep(1)
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[1]/div[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="form1"]/dl/dd[1]/input').send_keys('123')
        self.driver.find_element_by_xpath('//*[@id="form1"]/dl/dd[2]/input').click()
        self.driver.switch_to.default_content()
        sleep(1)
        frame2 = self.driver.find_element_by_xpath('/html/body/div[4]/iframe')
        self.driver.switch_to.frame(frame2)
        sleep(1)
        self.driver.find_element_by_id('dpTodayInput').click()
        self.driver.switch_to.default_content()
        sleep(1)
        self.driver.switch_to.frame(frame1)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="form1"]/dl/dd[4]/input').send_keys('321')
        self.driver.find_element_by_xpath('//*[@id="form1"]/div/button[1]').click()
        price2 = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[9]/div[3]/div/p[2]/span').text  # 新增付款单，提交
        self.assertEqual(price1, price2)
        self.driver.switch_to.default_content()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main(unittest.TestCase)