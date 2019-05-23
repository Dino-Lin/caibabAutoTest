#-*- coding:utf-8 -*-
import unittest

class Test(unittest.TestCase):
    u'''这是加法运算'''
    def testadd(self):
        result = 10+8
        hope = 18
        self.assertEqual(result,hope)