#-*- coding:utf-8 -*-
import unittest
class Test(unittest.TestCase):
    u'''这是减法运算'''
    def testjianfa(self):
        result = 10-8
        hope = 2
        self.assertEqual(result,hope)