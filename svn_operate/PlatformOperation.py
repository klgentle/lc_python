import os


class PlatformOperation(object):
    @staticmethod
    def change_path_sep(path):
        if path.find("\\") > -1 and os.sep != "\\":
            path = path.replace("\\", os.sep)
        elif path.find("/") > -1 and os.sep != "/":
            path = path.replace("/", os.sep)
        return path



if __name__ == "__main__":
    obj = PlatformOperation()
    path = "lc_python\\svn_operate"
    #print(obj.change_path_sep(path))
    assert(obj.change_path_sep(path) == path.replace("\\",'/'))
