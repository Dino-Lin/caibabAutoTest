import sys
sys.path.append('../')
import unittest
from testcases import findPasswordCase
from utils import HTMLTestReportCN
import datetime


if __name__ == "__main__":
    suite = unittest.TestSuite()
    test_cases = [findPasswordCase.FindPasswordTestCase("test_001"),findPasswordCase.FindPasswordTestCase("test_002"),findPasswordCase.FindPasswordTestCase("test_003"),findPasswordCase.FindPasswordTestCase("test_004")]
    suite.addTests(test_cases)
    fileEnd = datetime.datetime.now().strftime('%Y%m%d%H%M')
    filePath = 'C:\\HTMLTestReportCN'+fileEnd+'.html'
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告'+fileEnd,
        # description='详细测试用例结果',
        tester='Finyou'
    )
    runner.run(suite)
    fp.close()
    print('执行完毕')
    exit()