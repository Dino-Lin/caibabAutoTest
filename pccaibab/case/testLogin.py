import unittest
import common
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    u'''登录测试'''
    def testLogin(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("http://www.caibab.com")
        WebDriverWait(driver, 10).until(EC.title_contains("材巴巴"))

        loginButton = driver.find_element_by_xpath("//a[@class='orange-color']")
        loginButton.click()

        WebDriverWait(driver, 10).until(EC.url_contains("passport"))

        driver.find_element_by_id("username").send_keys("vv66")
        driver.find_element_by_id("password").send_keys("12345678")

        if (common.isElementExist(driver, "//input[@id='j_captcha_response']")):
            print("需要输入验证码")
            driver.find_element_by_id("j_captcha_response").send_keys("qwer")
        else:
            print("无需输入验证码")
        driver.find_element_by_id("btnLogin").click()

        driver.find_element_by_xpath("//p[@class='company-name company-54nameNew']")

        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    unittest.main()
