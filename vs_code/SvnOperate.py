import os
import platform


class SvnOperate(object):
    def __init__(self):
        pass


    @staticmethod
    def update_svn_path(path):
        try:
            print("Call svn up ......")
            os.chdir(path)
            os.system("svn up")
        except Exception as e:
            print("SVN UP ERROR: ", e.__doc__)

    def update_windows_svn_path(self, path):
        if self.is_system_windows():
            # BE CAREFUL HERE ###############
            self.update_svn_path(path)

    @staticmethod
    def is_system_windows():
        is_system_windows = False
        if platform.uname().system == "Windows":
            is_system_windows = True
        return is_system_windows
