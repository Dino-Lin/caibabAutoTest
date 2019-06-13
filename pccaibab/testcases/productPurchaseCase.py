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
        self.driver.find_element_by_class_name('head-search-input').send_keys('公牛开关插座86型面板')
        self.driver.find_element_by_class_name('head-search-btn').click()
        #找到第二个产品，点击立即购买
        self.driver.find_element_by_css_selector('#root > div > div.wrap._3rs-yFi0AAN5C3Y7mcc3ky > div.clearfix._1h2BiFdwId1XXqeGre9ACE > div > div.clearfix > div:nth-child(2) > div.clearfix > div._3qbv4KHiA-oqQU6b1BExEJ > a').click()
        #点击减少产品数量
        self.driver.find_element_by_link_text('-').click()
        #切换到alert
        alert = self.driver.switch_to.alert
        self.assertEqual('不能低于最少购买量',alert.text)
        alert.accept()
        self.driver.switch_to.default_content()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    def test_maxBuy(self):
        '''高于最大购买量'''
        self.driver.find_element_by_xpath('//*[@id="headMenu"]/div/ul/li[2]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_class_name('head-search-input').send_keys('公牛开关插座86型面板')
        self.driver.find_element_by_class_name('head-search-btn').click()
        # 找到第二个产品，点击立即购买
        self.driver.find_element_by_css_selector('#root > div > div.wrap._3rs-yFi0AAN5C3Y7mcc3ky > div.clearfix._1h2BiFdwId1XXqeGre9ACE > div > div.clearfix > div:nth-child(2) > div.clearfix > div._3qbv4KHiA-oqQU6b1BExEJ > a').click()
        # 输入超高数值
        self.driver.find_element_by_css_selector('#root > div > div.clearfix.Pyq7vjwVNHGxQv6-9MfL_ > div:nth-child(2) > div > div.clearfix.P7yHmpc0Ncw6XfyLQSuSA > div.left.TSaKdC0n0iGBusWXCWsbR > input[type=text]').send_keys(99999)
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
        self.driver.find_element_by_class_name('head-search-input').send_keys('公牛开关插座86型面板')
        self.driver.find_element_by_class_name('head-search-btn').click()
        # 找到第二个产品，点击立即购买
        self.driver.find_element_by_css_selector('#root > div > div.wrap._3rs-yFi0AAN5C3Y7mcc3ky > div.clearfix._1h2BiFdwId1XXqeGre9ACE > div > div.clearfix > div:nth-child(2) > div.clearfix > div._3qbv4KHiA-oqQU6b1BExEJ > a').click()
        num = self.driver.find_element_by_css_selector('#root > div > div.clearfix.Pyq7vjwVNHGxQv6-9MfL_ > div:nth-child(2) > div > div.clearfix.P7yHmpc0Ncw6XfyLQSuSA > div.left.TSaKdC0n0iGBusWXCWsbR > input[type=text]')
        num.click()
        num.clear()
        # 输入产品数量
        num.send_keys(6)
        # 点击立即购买
        self.driver.find_element_by_link_text('立即购买').click()
        if (common.isElementExistWithLinkText(self.driver,'设置默认地址')):
            print('存在送货地址，不需要新增')
        else:
            print('没有送货地址，新增一个送货地址')
            #点击使用新地址
            self.driver.find_element_by_link_text('使用新地址').click()
            button = self.driver.find_element_by_class_name('_2iW2bM0CmH_wBkhkF3kG1d')
            ActionChains(self.driver).move_to_element(button).perform()
            province = self.driver.find_element_by_link_text("广东省")
            ActionChains(self.driver).move_to_element(province).perform()
            city = self.driver.find_element_by_link_text("广州市")
            ActionChains(self.driver).move_to_element(city).perform()
            city.click()
            self.driver.find_element_by_name('contacter').send_keys("材巴巴")
            self.driver.find_element_by_name('addr').send_keys("盘福路888号7楼")
            self.driver.find_element_by_name('phone').send_keys("18888888888")
            self.driver.find_element_by_css_selector('#root > div > div.wrap.clearfix > div > div.cbb-modal-component > div.cbb-modal-wrap > div > div > div.cbb-modal-body > div > div._3I7KMBRllnatofzyOdupE6 > a.btn.btn-orange').click()
        #记录提交订单价格
        sleep(1)
        price1 = self.driver.find_element_by_class_name('kVghzsx9F7vxFasMLuuu7').text
        payType = self.driver.find_element_by_name('payType')
        #选择付款方式
        payType.find_element_by_xpath("//option[@value='A']").click()
        #选择送货日期
        self.driver.find_element_by_class_name('ant-calendar-picker-input').click()
        #选择今天
        self.driver.find_element_by_class_name('ant-calendar-today-btn').click()
        self.driver.find_element_by_name('remark').send_keys('123123123213123213123213')
        # 提交产品购买
        self.driver.find_element_by_css_selector('#root > div > div.wrap.clearfix > div > div:nth-child(9) > div._3CQoR6V6nspzW2VH1pMYba > button').click()
        frame1 = self.driver.find_element_by_css_selector('#container > div > div.layui-tab-content > div > iframe')
        # 切换进去iframe
        self.driver.switch_to.frame(frame1)
        # 等待1s
        sleep(1)
        # 关闭自动提示弹框
        if(common.isElementExistWithCssName(self.driver,'layui-layer-btn0')):
            self.driver.find_element_by_class_name('layui-layer-btn0').click()
        # 点击新增付款单
        self.driver.find_element_by_class_name('add-pay').click()
        # 输入付款账号
        self.driver.find_element_by_name('purchaserBankno').send_keys('123')
        # 点击付款日期
        self.driver.find_element_by_name('payTime').click()
        # 切换默认driver
        self.driver.switch_to.default_content()
        sleep(0.2)
        # 获取日期控件对应iframe
        frame2 = self.driver.find_element_by_css_selector('body > div:nth-child(5) > iframe')
        # 切换进入日期控件iframe
        self.driver.switch_to.frame(frame2)
        sleep(0.2)
        # 点击今天
        self.driver.find_element_by_id('dpTodayInput').click()
        # 切换默认主页面
        self.driver.switch_to.default_content()
        sleep(0.2)
        # 切入iframe
        self.driver.switch_to.frame(frame1)
        sleep(0.2)
        # 输入收款账号
        self.driver.find_element_by_name('supplierBankno').send_keys('321')
        # 新增付款单，提交
        self.driver.find_element_by_css_selector('#form1 > div > button.btn.btn-sm.btn-radius.btn-green').click()
        # 获取详情页对应金额
        sleep(1)
        price2 = self.driver.find_element_by_css_selector('body > div.basic-content > div > div > div:nth-child(9) > div.shopdetail-msg.clearfix > div > p.favorable > span').text
        # 对比前后金额是否一致
        self.assertEqual(price1, price2)
        # 切回主页面
        self.driver.switch_to.default_content()
        # 关闭窗口
        self.driver.close()
        # 切回上一个窗口
        self.driver.switch_to.window(self.driver.window_handles[0])
    def test_addAndBuy(self):
        '''添加进货单后购买'''
        self.driver.find_element_by_xpath('//*[@id="headMenu"]/div/ul/li[2]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_class_name('head-search-input').send_keys('公牛开关插座86型面板')
        self.driver.find_element_by_class_name('head-search-btn').click()
        # 找到第二个产品，点击立即购买
        self.driver.find_element_by_css_selector('#root > div > div.wrap._3rs-yFi0AAN5C3Y7mcc3ky > div.clearfix._1h2BiFdwId1XXqeGre9ACE > div > div.clearfix > div:nth-child(2) > div.clearfix > div._3qbv4KHiA-oqQU6b1BExEJ > a').click()
        num = self.driver.find_element_by_css_selector('#root > div > div.clearfix.Pyq7vjwVNHGxQv6-9MfL_ > div:nth-child(2) > div > div.clearfix.P7yHmpc0Ncw6XfyLQSuSA > div.left.TSaKdC0n0iGBusWXCWsbR > input[type=text]')
        num.click()
        num.clear()
        num.send_keys(6)
        # 点击加入进货单
        self.driver.find_element_by_css_selector('#root > div > div.clearfix.Pyq7vjwVNHGxQv6-9MfL_ > div:nth-child(2) > div > div.clearfix.P7yHmpc0Ncw6XfyLQSuSA > div.left._1c7SGERAW1ZNlx0rmHjpp7 > a.btn.btn-radius.btn-orange.p9M0tjB6kWw00eW4e8Iqo').click()
        self.driver.find_element_by_link_text('去结算').click()
        # 等待1秒，等产品加载成功后全选
        sleep(1)
        self.driver.find_element_by_css_selector('#root > div > div.wrap.clearfix > div > div._1SZYpqKc8QPPTJqsnQdzCX > div > div._2A7RiH2WmTjQEC2KF6ajdE._2qC2zgthWAljQGrwusw33g > label > input[type=checkbox]').click()
        # 提交
        self.driver.find_element_by_link_text('提交').click()
        if (common.isElementExistWithLinkText(self.driver, '设置默认地址')):
            print('存在送货地址，不需要新增')
        else:
            print('没有送货地址，新增一个送货地址')
            # 点击使用新地址
            self.driver.find_element_by_link_text('使用新地址').click()
            button = self.driver.find_element_by_class_name('_2iW2bM0CmH_wBkhkF3kG1d')
            ActionChains(self.driver).move_to_element(button).perform()
            province = self.driver.find_element_by_link_text("广东省")
            ActionChains(self.driver).move_to_element(province).perform()
            city = self.driver.find_element_by_link_text("广州市")
            ActionChains(self.driver).move_to_element(city).perform()
            city.click()
            self.driver.find_element_by_name('contacter').send_keys("材巴巴")
            self.driver.find_element_by_name('addr').send_keys("盘福路888号7楼")
            self.driver.find_element_by_name('phone').send_keys("18888888888")
            self.driver.find_element_by_css_selector(
                '#root > div > div.wrap.clearfix > div > div.cbb-modal-component > div.cbb-modal-wrap > div > div > div.cbb-modal-body > div > div._3I7KMBRllnatofzyOdupE6 > a.btn.btn-orange').click()
        # 记录提交订单价格
        sleep(1)
        price1 = self.driver.find_element_by_class_name('kVghzsx9F7vxFasMLuuu7').text
        payType = self.driver.find_element_by_name('payType')
        # 选择付款方式
        payType.find_element_by_xpath("//option[@value='A']").click()
        # 选择送货日期
        self.driver.find_element_by_class_name('ant-calendar-picker-input').click()
        # 选择今天
        self.driver.find_element_by_class_name('ant-calendar-today-btn').click()
        self.driver.find_element_by_name('remark').send_keys('123123123213123213123213')
        # 提交产品购买
        self.driver.find_element_by_css_selector('#root > div > div.wrap.clearfix > div > div._3CQoR6V6nspzW2VH1pMYba > button').click()
        frame1 = self.driver.find_element_by_css_selector('#container > div > div.layui-tab-content > div > iframe')
        # 切换进去iframe
        self.driver.switch_to.frame(frame1)
        # 等待1s
        sleep(1)
        # 关闭自动提示弹框
        if (common.isElementExistWithCssName(self.driver,'layui-layer-btn0')):
            self.driver.find_element_by_class_name('layui-layer-btn0').click()
        # 点击新增付款单
        self.driver.find_element_by_class_name('add-pay').click()
        # 输入付款账号
        self.driver.find_element_by_name('purchaserBankno').send_keys('123')
        # 点击付款日期
        self.driver.find_element_by_name('payTime').click()
        # 切换默认driver
        self.driver.switch_to.default_content()
        sleep(0.2)
        # 获取日期控件对应iframe
        frame2 = self.driver.find_element_by_css_selector('body > div:nth-child(5) > iframe')
        # 切换进入日期控件iframe
        self.driver.switch_to.frame(frame2)
        sleep(0.2)
        # 点击今天
        self.driver.find_element_by_id('dpTodayInput').click()
        # 切换默认主页面
        self.driver.switch_to.default_content()
        sleep(0.2)
        # 切入iframe
        self.driver.switch_to.frame(frame1)
        sleep(0.2)
        # 输入收款账号
        self.driver.find_element_by_name('supplierBankno').send_keys('321')
        # 新增付款单，提交
        self.driver.find_element_by_css_selector('#form1 > div > button.btn.btn-sm.btn-radius.btn-green').click()
        # 获取详情页对应金额
        sleep(1)
        price2 = self.driver.find_element_by_css_selector(
            'body > div.basic-content > div > div > div:nth-child(9) > div.shopdetail-msg.clearfix > div > p.favorable > span').text
        # 对比前后金额是否一致
        self.assertEqual(price1, price2)
        # 切回主页面
        self.driver.switch_to.default_content()
        # 关闭窗口
        self.driver.close()
        # 切回上一个窗口
        self.driver.switch_to.window(self.driver.window_handles[0])
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main(unittest.TestCase)