import os
import sys
from os.path import dirname

# 项目根目录
BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
from vs_code.SvnOperate import SvnOperate

SVN_DIR = r"E:\svn\1300_编码"


def test_svn_add():
    SvnOperate().svn_add(SVN_DIR)


if __name__ == "__main__":
    test_svn_add()
