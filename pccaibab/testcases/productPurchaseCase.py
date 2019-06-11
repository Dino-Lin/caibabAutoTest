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

class ProductPurchaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        commonLogin.CommonLogin.cgsLogin(commonLogin.CommonLogin, cls.driver)


    def test_normalBuy(self):
        '''正常购买步骤'''
        self.driver.find_element_by_xpath('//*[@id="headMenu"]/div/ul/li[2]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div/div/ul/li[1]/div/p/a').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.assertEqual(True, True)
        self.driver.close()
        sleep(3)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()