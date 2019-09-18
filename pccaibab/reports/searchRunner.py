import sys
sys.path.append('../')
import unittest
from testcases import searchCase
from utils import HTMLTestReportCN
import datetime


if __name__ == "__main__":
    suite = unittest.TestSuite()
    test_cases = [
                searchCase.searchTestCase("test_001"),searchCase.searchTestCase("test_002"),searchCase.searchTestCase("test_003"),searchCase.searchTestCase("test_004")
                  ,searchCase.searchTestCase("test_005"),searchCase.searchTestCase("test_006"),searchCase.searchTestCase("test_007"),searchCase.searchTestCase("test_008")
                  ,searchCase.searchTestCase("test_009"),searchCase.searchTestCase("test_010")
    ]
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