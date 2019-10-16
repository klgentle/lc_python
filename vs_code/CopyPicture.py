#! python3

import os
import shutil
import time
from pathlib import Path


# def readHistory(file_name:str)->list:
#    l = []
#    with open(file_name) as f:
#        for i in f.readlines():
#            l.append(i.strip('\n'))
#    return l


def CopyPicture():
    username = "klgentle"
    target_path = r"D:\picture\win10_save\tmp"
    hist_file = Path(target_path) / "list.txt"
    path = r"C:\Users\{}\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets".format(
        username
    )
    # os.path.dirname(path)
    # hist_list = readHistory(hist_file)
    date_str = time.strftime("%Y%m%d", time.localtime())  # 20180610
    modle = "a"
    if date_str[6:8] == "15":
        modle = "w"
        # delete all file
        shutil.rmtree(target_path)
        os.makedirs(target_path)

    f = open(hist_file, modle)

    for filename in os.listdir(path):
        # 拼接路径与文件名
        path_file = os.path.join(path, filename)

        # short_name = str(filename)[:12]
        short_name = str(filename)
        # if short_name in hist_list:
        #    continue

        # 判断文件大小
        if os.path.getsize(path_file) > 169 * 1024:
            # 复制并重新命名文件
            print(f"copy file {short_name}")
            shutil.copy(path_file, os.path.join(target_path, short_name + ".jpg"))
            f.write(short_name + "\t" + date_str + "\n")
    f.close()


if __name__ == "__main__":
    CopyPicture()
