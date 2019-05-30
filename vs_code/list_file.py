import os
import time


def list_file(path: str, file_name: str):
    to_file = open(file_name, "w")
    date_str = time.strftime("%Y%m%d", time.localtime())
    to_path = f"D:\jdong\\beta\\{date_str}_beta"
    for f in os.listdir(path):
        s = f"@@{to_path}\{f};\n"
        to_file.write(s)

    to_file.close()
    #print("list file done!")


if __name__ == "__main__":
    path = "/mnt/e/walker/乌海银行/baowen"
    file_name = "list.sql"
    list_file(path, file_name)
