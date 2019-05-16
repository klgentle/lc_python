#! python3

import os
import shutil
import time
from pathlib import Path


def readHistory(file_name:str)->list:
    l = []
    with open(file_name) as f:
        for i in f.readlines():
            l.append(i.strip('\n'))
    return l

def CopyPicture():
    username = "pactera"
    target_path = "D:\\win_screen\\tmp\\"
    
    hist_file = Path(target_path) / 'list.txt'
    path = f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
    # os.path.dirname(path)
    date_str = time.strftime("%Y%m%d", time.localtime())
    #hist_list = readHistory(hist_file)
    f = open(hist_file,"a")
    #print(f'enter here!27,path:{path}')
        
    for filename in os.listdir(path):
        # 拼接路径与文件名
        path_file = os.path.join(path, filename)
        
        short_name = str(filename)[:12] # 6 is too short
        #if short_name in hist_list:
        #    continue
        
        # 判断文件大小
        if os.path.getsize(path_file) > 169 * 1024:
            # 复制并重新命名文件
            print(f"copy file {short_name}")
            shutil.copy(
                path_file, target_path + short_name + ".jpg"
            )
            f.write(short_name+"\t"+date_str+'\n')
    f.close()


if __name__ == "__main__":
    CopyPicture()
