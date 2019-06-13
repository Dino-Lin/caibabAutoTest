import sys
sys.path.append("../")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import common
class CommonLogin:
    def login(self,username,password):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        if (common.isElementExist(self.driver, "//input[@id='j_captcha_response']")):
            print("需要输入验证码")
            self.driver.find_element_by_id("j_captcha_response").send_keys("qwer")
        else:
            pass
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

    def gysLogin(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("http://www.caibab.com")
        self.driver.implicitly_wait(2)
        WebDriverWait(self.driver, 10).until(EC.title_contains("材巴巴"))
        self.driver.find_element_by_xpath("//a[@class='orange-color']").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("passport"))
        self.login(self,"vv66", "12345678")

    def yysLogin(self):
        pass