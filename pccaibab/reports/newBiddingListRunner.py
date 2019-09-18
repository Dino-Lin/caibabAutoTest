import sys
sys.path.append('../')
import unittest
from testcases import purchaseOrdersCase
from testcases import newBiddingListCase
from utils import HTMLTestReportCN
import datetime

# 备注：新建竞价单然后竞价经过单三轮报价的用例（报价之后还包含易材通‘选择中标’、‘中标采购’，‘货款管理’）
# 对应的脚本名称为 testcases——newBiddingListCase.py
if __name__ == "__main__":
    suite = unittest.TestSuite()
    test_cases = [newBiddingListCase.NewBiddingListTestCase("test_NewBiddingListOrder")]
    suite.addTests(test_cases)
    fileEnd = datetime.datetime.now().strftime('%Y%m%d%H%M')
    filePath = 'C:\\HTMLTestReportCN'+fileEnd+'.html'
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