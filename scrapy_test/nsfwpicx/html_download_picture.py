import requests
import os
import re
import random
import sys

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

    def get_picure_addrs(self, url):
        """
        获取单个页面中的全部图片地址
        """
        # url = "http://nsfwpicx.com/{}.html#".format(pageNumber)
        # url = "http://nsfwpicx.com/2020/04/11/{}.html".format(pageNumber)
        pageNumber = url.replace(".html", "").split("/")[-1]
        print(f"test pageNumber: {pageNumber}")

        picList = []
        title = "_"

        r = requests.get(url, headers=self.kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.text.replace(" - Nsfwpicx", "")

        # 查找阅读人数
        # read_num = soup.find_all(attrs={"class": "post-meta"})
        # read_number = self.get_read_number(str(read_num))
        # print("read_number", read_number)

        ## 可能有坑，尤其是新页面阅读量少
        # if read_number < 2000:
        #    print("Read_number to small", pageNumber)
        #    return (" ", None)

        # 精确定位地址集
        # http://45.147.200.153/images/2020/04/20/PG8T.jpg#vwid=860&vhei=1530
        p = re.compile(
            "(https://qpix.com/images/\d{4}/\d{2}/\d{2}/\w*\.jpg|http://\d*.\d*.\d*.\d*/images/\d{4}/\d{2}/\d{2}/\w*\.jpg)"
        )
        tempList = re.findall(p, r.text)
        for addr in tempList:
            picList.append(addr)
        if len(picList) > 0:
            print("保存图片链接成功", pageNumber)
        else:
            print("保存图片链接失败", pageNumber)
            pprint.pprint(r.text)

        #pprint.pprint(list(set(picList)))
        print("Picture number is:", len(set(picList)))

        return (title, pageNumber, list(set(picList)))

    def download_picture(self, title_picList):
        # root 保存目录
        start = time.time()
        title, pageNumber, picList = title_picList
        root2 = os.path.join(self.root, str(pageNumber) + "_" + title.replace(" ", "_"))
        if not os.path.exists(root2):
            os.mkdir(root2)
        print("保存目录为：", root2)

        for i, addr in enumerate(picList):
            # 解决 windows 不区分大小写的问题
            filename = "".join([str(i), "_", addr.split("/")[-1]])
            file_path = os.path.join(root2, filename)

            # 多进程下载图片
            subprocess.Popen(["curl", addr, "-o", file_path, "--silent"])
            #print("图片下载中", i, sep=" ")


    def download_one_html(self, url):
        pic_list = self.get_picure_addrs(url)
        self.download_picture(pic_list)

    def download_all_pictures(self, from_number, end_number):
        for i in range(from_number, end_number - 1, -1):
            print("Deal with page index:", i)
            self.download_one_html(i)
            # 休息，防止被封, 等并行的下载完成
            sleep_second = 20
            print("---------Sleep {} second start--------- ...".format(sleep_second))
            time.sleep(sleep_second)
            print("---------Sleep {} second end---------\n".format(sleep_second))

    def download_list_pictures(self, index_list):
        for i in index_list:
            print("Deal with page index:", i)
            self.download_one_html(i)
            # 休息，防止被封, 等并行的下载完成
            sleep_second = 20
            print("---------Sleep {} second start--------- ...".format(sleep_second))
            time.sleep(sleep_second)
            print("---------Sleep {} second end---------\n".format(sleep_second))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please input Url!")
    g = GetNsfwPicture()
    # url = "http://nsfwpicx.com/2020/05/01/1435.html"
    g.download_one_html(sys.argv[1])
