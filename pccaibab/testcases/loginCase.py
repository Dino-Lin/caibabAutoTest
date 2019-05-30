import sys
sys.path.append('../')
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import common

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.caibab.com")
        self.driver.implicitly_wait(3)
        WebDriverWait(self.driver, 10).until(EC.title_contains("材巴巴"))
        self.driver.find_element_by_xpath("//a[@class='orange-color']").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("passport"))

    def login(self,username,password):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        if (common.isElementExist(self.driver, "//input[@id='j_captcha_response']")):
            print("需要输入验证码")
            self.driver.find_element_by_id("j_captcha_response").send_keys("qwer")
        else:
            pass
        self.driver.find_element_by_id("btnLogin").click()

    def tearDown(self):
        self.driver.quit()

    def test_empty_username(self):
        '''账号为空'''
        self.login("","")
        error_message = self.driver.find_element_by_class_name("errors").text
        self.assertEqual(error_message, '请输入用户名!')

    def test_empty_password(self):
        '''密码为空'''
        self.login("vv66", "")
        error_message = self.driver.find_element_by_class_name("errors").text
        self.assertEqual(error_message, '请输入密码!')

    def test_error_username(self):
        '''账号不存在'''
        self.login("asxsax", "12345678")
        error_message = self.driver.find_element_by_xpath("//div[@id='status']").text
        self.assertEqual(error_message,'登录帐号不存在')

    def test_login_success(self):
        '''账号密码正确'''
        self.login("vv66", "12345678")
        sleep(1)
        username = self.driver.find_element_by_xpath('//*[@id="masthead"]/div/div[1]/div/p/a').text
        self.assertEqual(username,'66供应商')

if __name__ == "__main__":
    unittest.main()