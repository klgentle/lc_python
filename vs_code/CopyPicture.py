#! python3

import os
import shutil
import time


def CopyPicture():
    username = "klgentle"
    target_path = "D:\\picture\\win10_save\\tmp"

    path = f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
    # os.path.dirname(path)
    date_str = time.strftime("%Y%m%d", time.localtime())

    for filename in os.listdir(path):
        # 拼接路径与文件名
        path_file = os.path.join(path, filename)
        # print(str(os.path.getsize(path_file))+'\t', filename)
        # 判断文件大小
        if os.path.getsize(path_file) > 169 * 1024:
            # 复制并重新命名文件
            shutil.copy(
                path_file, target_path + date_str + "_" + str(filename)[:6] + ".jpg"
            )


if __name__ == "__main__":
    CopyPicture()
