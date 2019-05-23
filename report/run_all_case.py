#-*- coding:utf-8 -*-
import unittest
import HTMLTestReportCN

#执行测试用例的目录
case_dir = r"D:\pyWorkspace\caibabAutoTest\case"  #这里填写你刚刚创建的case文件夹的目录
testcase = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
#discover方法筛选出来的用例，循环添加到测试套件中
for test_suit in discover:
    for test_case in test_suit:
        #添加用例到testcase
        testcase.addTest(test_case)

reportTitle = "自动化测试报告"
filePath ='F:\\HTMLTestReportCN.html'
fp = open(filePath,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title=reportTitle,
        #description='详细测试用例结果',
        tester='Findyou')
runner.run(testcase)
