from __future__ import absolute_import, division, print_function, unicode_literals
from os.path import dirname
import os
import sys

# 项目根目录
BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
print(BASE_DIR)
sys.path.append('../')
# 导入模块
from 02_string.StringFunctions import StringFunctions
import unittest


class TestString(unittest.TestCase):
    def test_find_the_second_position(self):
        a = StringFunctions("AND a =b AND c=d")
        except_out = 9
        self.assertEqual(except_out, a.find_the_second_position("AND"))


if __name__ == "__main__":
    unittest.main()
