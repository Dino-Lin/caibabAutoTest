import sys
sys.path.append("../")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils import common

# 公共登录模块

class CommonLogin:
    def login(self,username,password):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        if (common.isElementExist(self.driver, "//input[@id='j_captcha_response']")):
            print("需要输入验证码")
        else:
            pass
            #self.driver.find_element_by_id("j_captcha_response").send_keys("qwer")

        self.driver.find_element_by_id("btnLogin").click()


    def cgsLogin(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("http://www.caibab.com")
        self.driver.implicitly_wait(2)
        WebDriverWait(self.driver, 10).until(EC.title_contains("材巴巴"))
        self.driver.find_element_by_xpath("//a[@class='orange-color']").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("passport"))
        self.login(self, "cc55", "12345678")

    def gysLogin(self,driver):    # 已认证
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("http://www.caibab.com")
        self.driver.implicitly_wait(2)
        WebDriverWait(self.driver, 10).until(EC.title_contains("材巴巴"))
        self.driver.find_element_by_xpath("//a[@class='orange-color']").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("passport"))
        self.login(self,"huahua123456", "huahua123456")

    def cjkLogin(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("http://cjk.caibab.com")  # 打开网站
        self.driver.implicitly_wait(2)
        WebDriverWait(self.driver, 10).until(EC.title_contains("易材通"))# 输入账号密码
        self.driver.find_element_by_xpath('//*[@name="loginName"]').send_keys('whwh')
        self.driver.find_element_by_xpath('//input[@id="password"]').send_keys('888888')
        # 输入校验码qwer
        #self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')
        # 点击登录
        self.driver.find_element_by_class_name('btn-orange').click()
        # 如出现弹窗，忽略alert弹窗
        # driver.switch_to.alert.accept()

    def cgcomsLogin(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("http://cgcoms.caibab.com/login.do") # 打开网站
        self.driver.implicitly_wait(2)
        # 输入账号密码
        self.driver.find_element_by_xpath('//input[@name="loginName"]').clear()
        self.driver.find_element_by_xpath('//input[@name="password"]').clear()
        self.driver.find_element_by_xpath('//input[@name="loginName"]').send_keys('admin')
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('111111')
        # 输入校验码qwer
        # self.driver.find_element_by_xpath('//input[@name="checkCode"]').send_keys('qwer')
        # 点击登录
        self.driver.find_element_by_xpath('//a[text()="登录"]').click()


        pass