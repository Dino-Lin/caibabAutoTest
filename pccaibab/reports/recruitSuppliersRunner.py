import sys
sys.path.append('../')
import unittest
from testcases import recruitSuppliersCase
from utils import HTMLTestReportCN
import datetime


if __name__ == "__main__":
    suite = unittest.TestSuite()
    #test_cases = [demoCase.DemoTestCase("test_clickSomething"),demoCase.DemoTestCase("test_clickOneMorething")]
    test_cases = [recruitSuppliersCase.RecruitSuppliersTestCase("test_001"),recruitSuppliersCase.RecruitSuppliersTestCase("test_002"),recruitSuppliersCase.RecruitSuppliersTestCase("test_003"),recruitSuppliersCase.RecruitSuppliersTestCase("test_004")]
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