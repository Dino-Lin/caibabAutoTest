import sys
sys.path.append('../')
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from commons import commonLogin
from commons import commonFunction
from utils import common
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import random
import string


'''
备注：这是搜索的脚本
用例：
1、未登录状态下搜索采购单
2、未登录状态下搜索材料
3、未登录状态下搜索采购商
4、未登录状态下搜索供应商
5、未登录状态下搜索不存在的采购单、材料、采购商、供应商
6、gys登录状态下搜索采购单
7、gys登录状态下搜索材料
8、cgs登录状态下搜索采购商
9、cgs登录状态下搜索供应商
10、cgs登录状态下搜索不存在的采购单、材料、采购商、供应商
'''

class searchTestCase(unittest.TestCase):
      def setUp(self):
          self.driver = webdriver.Chrome()
          self.driver.maximize_window()
          self.driver.get("http://www.caibab.com")
          self.driver.implicitly_wait(3)
          WebDriverWait(self.driver, 10).until(EC.title_contains("材巴巴"))

      def tearDown(self):
          self.driver.quit()

      '''1、未登录状态下搜索采购单'''
      def test_001(self):
                  self.driver.find_element_by_xpath('//input[@placeholder="输入采购单名称、规格等"]').send_keys('报名')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()
                  sleep(2)
                  js = "var q=document.documentElement.scrollTop=10000"
                  self.driver.execute_script(js)
                  sleep(3)
                  element_1 = self.driver.find_element_by_xpath('//a[@class="red-color"]').text
                  self.assertEqual(element_1,'登录后查看更多')

      '''2、未登录状态下搜索材料'''
      def test_002(self):
                  self.driver.find_element_by_xpath('//li[text()="材料"]').click()  # 点击‘材料’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入材料名称、规格等"]').send_keys('开关')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()  # 搜索
                  sleep(1)
                  self.driver.find_elements_by_xpath('//a[text()="立即购买"]')[3].click()  # 加入购物车
                  js = "var q=document.documentElement.scrollTop=100"
                  self.driver.execute_script(js)
                  self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()  # 立即购买
                  element = self.driver.find_element_by_xpath('//h1[text()="材巴巴会员"]').text
                  self.assertEqual(element, "材巴巴会员")




      '''3、未登录状态下搜索采购商'''
      def test_003(self):
                  self.driver.find_element_by_xpath('//li[text()="采购商"]').click()  # 点击‘采购商’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入采购商名称"]').send_keys('采购商')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()   # 搜索
                  sleep(1)
                  js = "var q=document.documentElement.scrollTop=10000"
                  self.driver.execute_script(js)
                  sleep(3)
                  element_1 = self.driver.find_element_by_xpath('//a[@class="red-color"]').text
                  self.assertEqual(element_1, '登录后查看更多')

      '''4、未登录状态下搜索供应商'''
      def test_004(self):
                  self.driver.find_element_by_xpath('//li[text()="供应商"]').click()  # 点击‘采购商’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入供应商名称"]').send_keys('供应商')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()   # 搜索
                  sleep(1)
                  self.driver.execute_script("""
                     (function () {
                     var y = 0;
                     var step = 100;
                     window.scroll(0, 0);
                     function f() {
                     if (y < document.body.scrollHeight) {
                     y += step;
                     window.scroll(0, y);
                     setTimeout(f, 100);
                     } else {
                     window.scroll(0, 0);
                     document.title += "scroll-done";
                     }
                     }
                     setTimeout(f, 1000);
                     })();
                     """)
                  print("下拉中...")
                  while True:
                              if "scroll-done" in self.driver.title:
                                          break
                  else:
                              print("还没有拉到最底端...")
                              time.sleep(3)
                  sleep(3)
                  element_1 = self.driver.find_element_by_xpath('//*[text()="更多信息敬请期待"]').text
                  self.assertEqual(element_1, '更多信息敬请期待')

      '''5、未登录状态下搜索不存在的采购单、材料、采购商、供应商'''
      def test_005(self):
                  '''输入不存在的采购单'''
                  self.driver.find_element_by_xpath('//input[@placeholder="输入采购单名称、规格等"]').send_keys('good')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()
                  ele = self.driver.find_element_by_xpath('//*[text()="抱歉,暂无信息"]').text
                  self.assertEqual(ele,"抱歉,暂无信息")
                  self.driver.find_element_by_xpath('//*[text()="材巴巴首页"]').click()
                  sleep(1)

                  '''输入不存在的材料'''
                  self.driver.find_element_by_xpath('//li[text()="材料"]').click()  # 点击‘材料’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入材料名称、规格等"]').send_keys('earings')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()   # 搜索
                  ele = self.driver.find_element_by_xpath('//*[text()="抱歉,暂无数据"]').text
                  self.assertEqual(ele, "抱歉,暂无数据")
                  self.driver.find_element_by_xpath('//*[text()="材巴巴首页"]').click()
                  sleep(1)

                  # '''输入不存在的采购商，定位不到元素'''
                  # self.driver.find_element_by_xpath('//li[text()="采购商"]').click()  # 点击‘采购商’按钮
                  # self.driver.find_element_by_xpath('//input[@placeholder="输入采购商名称"]').send_keys('你好吗')  # 输入搜索的文字
                  # self.driver.find_element_by_xpath('//button[text()="搜索"]').click()  # 搜索
                  # ele = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/p/text()[1]').text
                  # self.assertEqual(ele, "抱歉，暂无")
                  # # ele = self.driver.find_element_by_xpath('//*[text()="抱歉，暂无信息"]').text
                  # # self.assertEqual(ele, "抱歉,暂无信息")
                  # sleep(1)

                  '''输入不存在的供应商'''
                  self.driver.find_element_by_xpath('//li[text()="供应商"]').click()  # 点击‘供应商’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入供应商名称"]').send_keys('不存在的供应商')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()   # 搜索
                  ele = self.driver.find_element_by_xpath('//p[text()="抱歉，暂无信息"]').text
                  self.assertEqual(ele, "抱歉，暂无信息")
                  sleep(1)

      '''6、gys登录状态下搜索采购单'''
      def test_006(self):
                  commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin,self.driver)
                  self.driver.find_element_by_xpath('//input[@placeholder="输入采购单名称、规格等"]').send_keys('lzceshihongdian1')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()
                  sleep(2)
                  js = "var q=document.documentElement.scrollTop=10000"
                  self.driver.execute_script(js)
                  sleep(3)
                  element_1 = self.driver.find_element_by_xpath('//*[text()="更多信息敬请期待"]').text
                  self.assertEqual(element_1, '更多信息敬请期待')

      '''7、gys登录状态下搜索材料'''
      def test_007(self):
                  commonLogin.CommonLogin.gysLogin(commonLogin.CommonLogin,self.driver)
                  self.driver.find_element_by_xpath('//li[text()="材料"]').click()  # 点击‘材料’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入材料名称、规格等"]').send_keys('开关')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()   # 搜索
                  sleep(1)
                  self.driver.find_elements_by_xpath('//a[text()="立即购买"]')[3].click()  # 加入购物车
                  js = "var q=document.documentElement.scrollTop=100"
                  self.driver.execute_script(js)
                  self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()   # 立即购买
                  sleep(3)
                  self.driver.switch_to.alert.accept()

      '''8、cgs登录状态下搜索采购商'''
      def test_008(self):
                  commonLogin.CommonLogin.cgsLogin(commonLogin.CommonLogin,self.driver)
                  self.driver.find_element_by_xpath('//li[text()="采购商"]').click()  # 点击‘采购商’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入采购商名称"]').send_keys('采购商')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()   # 搜索
                  sleep(1)
                  self.driver.execute_script("""
                                       (function () {
                                       var y = 0;
                                       var step = 100;
                                       window.scroll(0, 0);
                                       function f() {
                                       if (y < document.body.scrollHeight) {
                                       y += step;
                                       window.scroll(0, y);
                                       setTimeout(f, 100);
                                       } else {
                                       window.scroll(0, 0);
                                       document.title += "scroll-done";
                                       }
                                       }
                                       setTimeout(f, 1000);
                                       })();
                                       """)
                  print("下拉中...")
                  while True:
                              if "scroll-done" in self.driver.title:
                                          break
                  else:
                              print("还没有拉到最底端...")
                              time.sleep(3)
                  element_1 = self.driver.find_element_by_xpath('//*[text()="更多信息敬请期待"]').text
                  self.assertEqual(element_1, '更多信息敬请期待')

      '''9、cgs登录状态下搜索供应商'''
      def test_009(self):
                  commonLogin.CommonLogin.cgsLogin(commonLogin.CommonLogin,self.driver)
                  self.driver.find_element_by_xpath('//li[text()="供应商"]').click()  # 点击‘采购商’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入供应商名称"]').send_keys('供应商')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()  # 搜索
                  sleep(1)
                  self.driver.execute_script("""
                                      (function () {
                                      var y = 0;
                                      var step = 100;
                                      window.scroll(0, 0);
                                      function f() {
                                      if (y < document.body.scrollHeight) {
                                      y += step;
                                      window.scroll(0, y);
                                      setTimeout(f, 100);
                                      } else {
                                      window.scroll(0, 0);
                                      document.title += "scroll-done";
                                      }
                                      }
                                      setTimeout(f, 1000);
                                      })();
                                      """)
                  print("下拉中...")
                  while True:
                              if "scroll-done" in self.driver.title:
                                          break
                  else:
                              print("还没有拉到最底端...")
                              time.sleep(3)
                  sleep(3)
                  element_1 = self.driver.find_element_by_xpath('//*[text()="更多信息敬请期待"]').text
                  self.assertEqual(element_1, '更多信息敬请期待')


      '''10、cgs登录状态下搜索不存在的采购单、材料、采购商、供应商'''
      def test_010(self):
                  commonLogin.CommonLogin.cgsLogin(commonLogin.CommonLogin,self.driver)
                  '''输入不存在的采购单'''
                  self.driver.find_element_by_xpath('//input[@placeholder="输入采购单名称、规格等"]').send_keys('good')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()
                  ele = self.driver.find_element_by_xpath('//*[text()="抱歉,暂无信息"]').text
                  self.assertEqual(ele, "抱歉,暂无信息")
                  self.driver.find_element_by_xpath('//a[text()="材巴巴"]').click()
                  sleep(1)

                  '''输入不存在的材料'''
                  self.driver.find_element_by_xpath('//li[text()="材料"]').click()  # 点击‘材料’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入材料名称、规格等"]').send_keys(
                              'earings')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()  # 搜索
                  ele = self.driver.find_element_by_xpath('//*[text()="抱歉,暂无数据"]').text
                  self.assertEqual(ele, "抱歉,暂无数据")
                  self.driver.find_element_by_xpath('//a[text()="材巴巴"]').click()
                  sleep(1)

                  # '''输入不存在的采购商，定位不到元素'''
                  # self.driver.find_element_by_xpath('//li[text()="采购商"]').click()  # 点击‘采购商’按钮
                  # self.driver.find_element_by_xpath('//input[@placeholder="输入采购商名称"]').send_keys('你好吗')  # 输入搜索的文字
                  # self.driver.find_element_by_xpath('//button[text()="搜索"]').click()  # 搜索
                  # ele = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/p/text()[1]').text
                  # self.assertEqual(ele, "抱歉，暂无")
                  # # ele = self.driver.find_element_by_xpath('//*[text()="抱歉，暂无信息"]').text
                  # # self.assertEqual(ele, "抱歉,暂无信息")
                  # sleep(1)

                  '''输入不存在的供应商'''
                  self.driver.find_element_by_xpath('//li[text()="供应商"]').click()  # 点击‘供应商’按钮
                  self.driver.find_element_by_xpath('//input[@placeholder="输入供应商名称"]').send_keys('不存在的供应商')  # 输入搜索的文字
                  self.driver.find_element_by_xpath('//button[text()="搜索"]').click()  # 搜索
                  ele = self.driver.find_element_by_xpath('//p[text()="抱歉，暂无信息"]').text
                  self.assertEqual(ele, "抱歉，暂无信息")
                  sleep(1)


















