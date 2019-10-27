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
    SvnOperate(SVN_DIR).svn_add()


def test_svn_commit():
    SvnOperate(SVN_DIR).svn_commit()


def test_svn_commit_code():
    SvnOperate(SVN_DIR).svn_commit_code()


if __name__ == "__main__":
    test_svn_commit()

