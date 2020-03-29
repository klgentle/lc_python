import requests
import os
import re
import random

import urllib.request
import time
import pprint
import subprocess

from bs4 import BeautifulSoup
from urllib.parse import quote_plus, unquote_plus


class GetNsfwPicture(object):
    def __init__(self):
        self.kv = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        self.root = "/mnt/d/code_test/game_test/nsf"

    @staticmethod
    def get_read_number(input_str) -> int:
        # 删除非数字(-)的字符串
        return int(re.sub(r"\D", "", input_str))

    def get_picure_addrs(self, pageNumber):
        """
        获取单个页面中的全部图片地址
        """
        url = "http://nsfwpicx.com/{}.html#".format(pageNumber)
        picList = []
        try:
            r = requests.get(url, headers=self.kv)
            r.raise_for_status()
            r.encoding = r.apparent_encoding

            soup = BeautifulSoup(r.text, "html.parser")
            title = soup.title.text.replace(" - Nsfwpicx", "")
            p = re.compile("https://qpix.com/images/\d{4}/\d{2}/\d{2}/\w*\.jpg")

            # 查找阅读人数
            #read_num = soup.find_all(attrs={"class": "post-meta"})
            #read_number = self.get_read_number(str(read_num))
            #print("read_number", read_number)

            # 可能有坑，尤其是新页面阅读量少
            # if read_number < 2000:
            #    print("Read_number to small", pageNumber)
            #    return (" ", None)

            # 精确定位地址集
            picture_text = soup.find_all(attrs={"itemprop": "articleBody"})
            # tempList = re.findall(p, r.text)
            tempList = re.findall(p, str(picture_text))
            for addr in tempList:
                picList.append(addr)
                # print("-------------test each addr:", addr)
            print("保存图片链接成功", pageNumber)
            tempList = []
        except Exception as e:
            print("保存图片链接失败:", e.__doc__)
        # pprint.pprint(list(set(picList)))

        return (title, list(set(picList)))

    def download_picture(self, title_picList, pageNumber):
        # root 保存目录
        start = time.time()
        title, picList = title_picList
        root2 = os.path.join(self.root, str(pageNumber) + "_" + title.replace(" ", "_"))
        if not os.path.exists(root2):
            os.mkdir(root2)

        print("folder:", root2)
        # 切换目录
        #os.chdir(root2)
        for i, addr in enumerate(picList):
            # 解决 windows 不区分大小写的问题
            filename = "".join([str(i), "_", addr.split("/")[-1]])
            file_path = os.path.join(root2, filename)

            # 多进程下载图片
            subprocess.Popen(['curl', addr, '-o', file_path, '--silent'])

        print("图片下载中")
        #print("Page {} finished in {:.3f} seconds".format(pageNumber,time.time()-start))

            #if not os.path.exists(file_path):
            #    pass
            #    # save file
            #    #r = requests.get(addr, headers=self.kv)
            #    #r.raise_for_status()
            #    #with open(file_path, "wb") as f:
            #    #    f.write(r.content)
            #    #urllib.request.urlretrieve(addr,filename=file_path)
            #    #print("图片已保存")


            #else:
            #    print("-------------------图片已存在")

    def download_one_html(self, pageNumber):
        titlelist = self.get_picure_addrs(pageNumber)
        self.download_picture(titlelist, pageNumber)

    def download_all_pictures(self, from_number, end_number):
        for i in range(from_number, end_number, -1):
            print("Deal with page index:", i)
            self.download_one_html(i)
            # 休息，防止被封
            time.sleep(20)
            print("---------Sleep 20 second--------- ...\n")


if __name__ == "__main__":
    g = GetNsfwPicture()
    # pageNumber = 1162
    # g.download_one_html(pageNumber)

    from_number = 986
    end_number = 500
    g.download_all_pictures(from_number, end_number)
