import sys
sys.path.append('../')
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import common
from commons import commonLogin

class DemoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin,cls.driver)

    def test_clickSomething(self):
        '''输入123搜索'''
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div[1]/div/form/input').send_keys("123")
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div[1]/div/form/button').click()
        flag = common.isElementExist(self.driver,'//*[@id="root"]/div/div/div[2]/div[1]')
        self.assertEqual(True,flag)

    def test_clickOneMorething(self):
        '''输出4423123搜索'''
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div[1]/div/form/input').send_keys("4423123")
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div[1]/div/form/button').click()
        flag = common.isElementExist(self.driver, '//*[@id="root"]/div/div/div[2]/div[1]')
        self.assertEqual(True, flag)

    def tearDown(self):
        self.driver.get('http://www.caibab.com/index')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

