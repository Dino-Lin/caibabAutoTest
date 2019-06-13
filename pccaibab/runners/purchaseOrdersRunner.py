import sys
sys.path.append('../')
import unittest
from testcases import purchaseOrdersCase
from utils import HTMLTestReportCN
import datetime


if __name__ == "__main__":
    suite = unittest.TestSuite()
    #test_cases = [demoCase.DemoTestCase("test_clickSomething"),demoCase.DemoTestCase("test_clickOneMorething")]
    test_cases = [purchaseOrdersCase.PurchaseOrdersTestCase("test_notStarted"),purchaseOrdersCase.PurchaseOrdersTestCase("test_notShow")]
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