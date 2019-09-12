import sys
sys.path.append('../')
import unittest
from testcases import loginCase
from utils import HTMLTestReportCN
import datetime


if __name__ == "__main__":
    suite = unittest.TestSuite()
    test_cases = [loginCase.LoginTestCase("test_right_message"),loginCase.LoginTestCase("test_wrong_password"),loginCase.LoginTestCase("test_not_regist"),loginCase.LoginTestCase("test_not_used")
                  ,loginCase.LoginTestCase("test_empty_message"),loginCase.LoginTestCase("test_empty_username"),loginCase.LoginTestCase("test_empty_password")]
    suite.addTests(test_cases)
    fileEnd = datetime.datetime.now().strftime('%Y%m%d%H%M')
    filePath = 'F:\\HTMLTestReportCN'+fileEnd+'.html'
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告'+fileEnd,
        # description='详细测试用例结果',
        tester='Findyou'
    )
    runner.run(suite)
    fp.close()
    print('执行完毕')
    exit()



