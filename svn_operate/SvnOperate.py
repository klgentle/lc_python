import os
import platform
import sys
import requests


class SvnOperate(object):
    def __init__(self, path):
        os.chdir(path)
        if not self.is_system_windows():
            raise TypeError("not windows OS svn operate is not safe")
        self.checkSvnConnect()

    @staticmethod
    def checkSvnConnect():
        # SSLError(SSLCertVerif
        svn_url = "https://10.120.107.200/svn/HK-ODS"
        r = requests.get(svn_url, verify=False)

    @staticmethod
    def update_svn():
        try:
            print("Call svn up ......")
            os.system("svn up")
        except Exception as e:
            print("SVN UP ERROR: ", e.__doc__)

    def update_windows_svn(self):
        if self.is_system_windows():
            # BE CAREFUL HERE ###############
            self.update_svn()

    @staticmethod
    def is_system_windows():
        is_system_windows = False
        if platform.uname().system == "Windows":
            is_system_windows = True
        return is_system_windows

    @staticmethod
    def svn_add():
        try:
            # 检查是否是新增的文件
            # TODO svn how to add file with blank?
            if os.popen("svn st").read().find("?") > -1:
                svn_st_list = os.popen("svn st").read().strip("\n").split("\n")
                svn_st_filter = filter(lambda x: x.startswith("? "), svn_st_list)
                svn_st_list = list(map(lambda x: x.strip("?       "), svn_st_filter))
                # print(list(svn_st_list))
                for filename in svn_st_list:
                    print("call svn add {}".format(filename))
                    os.system("svn add {}".format(filename))
        except Exception as e:
            print("SVN ADD ERROR: ", e.__doc__)

    @staticmethod
    def svn_commit(message="", redirect=None):
        try:
            # TODO 解决重复提交的问题
            if len(os.popen("svn st").read()) < 2:
                # print("no need to commit")
                return
            if redirect:
                print(f'call svn commit -m "{message}" * >{redirect}')
                os.system(f'svn commit -m "{message}" * >{redirect}')
            else:
                print(f'call svn commit -m "{message}" *')
                os.system(f'svn commit -m "{message}" *')

        except Exception as e:
            print("SVN COMMIT ERROR: ", e.__doc__)

    def svn_commit_code(self, message="", redirect="../commit.log"):
        return self.svn_commit(message, redirect)

    @staticmethod
    def svn_delete():
        try:
            if os.popen("svn st").read().find("!") > -1:
                svn_st_list = os.popen("svn st").read().strip("\n").split("\n")
                svn_st_filter = filter(lambda x: x.startswith("! "), svn_st_list)
                svn_st_list = list(map(lambda x: x.strip("!       "), svn_st_filter))
                # print(list(svn_st_list))
                for filename in svn_st_list:
                    print("call svn delete {}".format(filename))
                    os.system("svn delete {}".format(filename))
        except Exception as e:
            print("SVN DELETE ERROR: ", e.__doc__)
