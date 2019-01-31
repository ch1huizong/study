#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# splitter模块中split函数的单元测试

import splitter
import unittest


class TestSplitFunction(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testsimplestring(self):
        r = splitter.split("GOOG 100 490.50")
        self.assertEqual(r, ["GOOG", "100", "490.50"])

    def testtypeconvert(self):
        r = splitter.split("GOOG 100 490.5", [str, int, float])
        self.assertEqual(r, ["GOOG", 100, 490.5])

    def testdelimiter(self):
        r = splitter.split("GOOG,100,490.50", delimiter=",")
        self.assertEqual(r, ["GOOG", "100", "490.50"])


if __name__ == "__main__":
    unittest.main()
