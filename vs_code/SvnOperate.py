import os
import platform


class SvnOperate(object):
    def __init__(self):
        pass

    @staticmethod
    def update_svn(path):
        try:
            print("Call svn up ......")
            os.chdir(path)
            os.system("svn up")
        except Exception as e:
            print("SVN UP ERROR: ", e.__doc__)

    def update_windows_svn(self, path):
        if self.is_system_windows():
            # BE CAREFUL HERE ###############
            self.update_svn(path)

    @staticmethod
    def is_system_windows():
        is_system_windows = False
        if platform.uname().system == "Windows":
            is_system_windows = True
        return is_system_windows

    @staticmethod
    def svn_add(path):
        try:
            os.chdir(path)
            # 检查是否需要add
            if os.popen("svn st").read()[0] == "?":
                # TODO add * not good
                os.system("svn add *")
        except Exception as e:
            print("SVN ADD ERROR: ", e.__doc__)

    @staticmethod
    def svn_commit(path, message="update by dongjian", redirect=None):
        try:
            os.chdir(path)
            os.system(f"svn commit -m '{message}' * >{redirect}")
        except Exception as e:
            print("SVN COMMIT ERROR: ", e.__doc__)

    def svn_commit_code(
        self, path, message="update by dongjian", redirect="../commit.log"
    ):
        return self.svn_commit(path, message, redirect)
