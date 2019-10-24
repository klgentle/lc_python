import os 

def test_change_path_sep(path):
    if path.find("\\") > -1 and os.sep != "\\":
        path = path.replace("\\", os.sep)
    elif path.find("/") > -1 and os.sep != "/":
        path = path.replace("/", os.sep)
    return path


if __name__== "__main__":
    path1 = "1000_编辑区/1300_编码/1301_ODSDB/RPTUSER/05Procedures"
    print(test_change_path_sep(path1))
    path2 = r"1000_编辑区\1300_编码\1370_水晶报表\CIF"
    print(test_change_path_sep(path2))

