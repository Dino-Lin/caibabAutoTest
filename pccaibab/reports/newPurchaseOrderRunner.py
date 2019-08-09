import sys
sys.path.append('../')
import unittest
from testcases import purchaseOrdersCase
from testcases import newPurchaseOrderCase
from utils import HTMLTestReportCN
import datetime

# 备注：新建采购单和采购单报价一起使用，先新建后报价

if __name__ == "__main__":
    suite = unittest.TestSuite()
    #test_cases = [newPurchaseOrderCase.NewPurchaseOrderTestCase("test_newSignupStartedPurchaseOrder"),purchaseOrdersCase.PurchaseOrdersTestCase("test_signupStarted")]
    test_cases = [newPurchaseOrderCase.NewPurchaseOrderTestCase("test_SignupNotStartPurchaseOrder"),purchaseOrdersCase.PurchaseOrdersTestCase("test_SignupNotStart"),newPurchaseOrderCase.NewPurchaseOrderTestCase("test_NewSignupStartedPurchaseOrder"),purchaseOrdersCase.PurchaseOrdersTestCase("test_signupStarted"),newPurchaseOrderCase.NewPurchaseOrderTestCase("test_SignupEndPurchaseOrder"),purchaseOrdersCase.PurchaseOrdersTestCase("test_signupEnd")]

    #test_cases = [productPurchaseCase.ProductPurchaseTestCase("test_normalBuy"),productPurchaseCase.ProductPurchaseTestCase("test_addAndBuy")]
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