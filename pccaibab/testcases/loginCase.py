import sys
sys.path.append('../')
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import common
'''
登录的测试用例

1、输入已注册的用户名和正确的密码，验证是否成功登录
2、输入已注册的用户名和不正确的密码，验证是否成功失败，且提示信息正确
3、输入未注册的用户名和任意密码，验证是否登录失败，且提示信息正确
4、使用被禁用用户登录，验证是否登录失败
5、用户名和密码两者都为空，验证是否登录失败，且提示信息正确
6、用户名为空，验证是否登录失败，并且提示信息正确
7、密码为空，验证是否登录失败，提示信息正确

'''
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

    '''1、正确的用户名，正确的密码'''
    def test_right_message(self):
        self.login("huahua123456","huahua123456")
        right_message = self.driver.find_element_by_xpath('//*[text()="花都山卡拉公司"]').text
        self.assertEqual(right_message,"花都山卡拉公司")

    '''2、正确的用户名，不正确的密码'''
    def test_wrong_password(self):
        self.login("huahua123456", "huahua1234567")
        right_message = self.driver.find_element_by_xpath('//*[text()="您输入的密码和账户名不匹配，请重新输入。"]').text
        self.assertEqual(right_message, "您输入的密码和账户名不匹配，请重新输入。")

    '''3、输入未注册的用户名和任意密码'''
    def test_not_regist(self):
        self.login("jdjajasj123456", "fjdjjd999")
        message = self.driver.find_element_by_xpath('//*[text()="登录帐号不存在"]').text
        self.assertEqual(message,'登录帐号不存在')

    '''4、使用被禁用用户登录'''
    def test_not_used(self):
        self.login("hua123", "88888888")
        message = self.driver.find_element_by_xpath('//*[text()="用户名或密码错误"]').text
        self.assertEqual('用户名或密码错误')

    '''5、用户名密码都为空'''
    def test_empty_message(self):
        self.login("","")
        error_message = self.driver.find_element_by_class_name("errors").text
        self.assertEqual(error_message, '请输入用户名!')

    '''6、用户名为空 '''
    def test_empty_username(self):
        self.login("", "88888888")
        error_message = self.driver.find_element_by_class_name("errors").text
        self.assertEqual(error_message, '请输入用户名!')

    '''7、密码为空'''
    def test_empty_password(self):
        self.login("vv66", "")
        error_message = self.driver.find_element_by_class_name("errors").text
        self.assertEqual(error_message, '请输入密码!')

if __name__ == "__main__":
    unittest.main()