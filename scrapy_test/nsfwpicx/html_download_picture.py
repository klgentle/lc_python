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
        pageNumber = url.replace(".html", "").split("/")[-1]
        print(f"test pageNumber: {pageNumber}")

        picList = []
        title = "_"

        r = requests.get(url, headers=self.kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.text.replace(" - Nsfwpicx", "")

        # 精确定位地址集
        imgs = soup.select("img[data-src]")

        try:
            tempList = []
            for img in imgs:
                # p = re.compile("http.*#vwid")
                imgAddrs = str(img).split('data-src="')[1]
                tempList.append(imgAddrs.split("#vwid")[0])

        except Exception as e:
            print(e.__doc__)

        for addr in tempList:
            picList.append(addr)
        if len(picList) > 0:
            print("保存图片链接成功", pageNumber)
        else:
            print("保存图片链接失败", pageNumber)
            pprint.pprint(r.text)

        uniqueList = sorted(list(set(picList)))
        for i, v in enumerate(uniqueList):
            print(i, v)
        #pprint.pprint(uniqueList)
        print("Picture number is:", len(uniqueList))

        return (title, pageNumber, uniqueList)

    def GetFolderRoot(self, title, pageNumber):
        # root 保存目录
        root2 = os.path.join(self.root, str(pageNumber) + "_" + title.replace(" ", "_"))
        return root2

    def download_picture(self, title_picList):
        title, pageNumber, picList = title_picList
        root2 = self.GetFolderRoot(title, pageNumber)
        if not os.path.exists(root2):
            os.mkdir(root2)
        print("保存目录为：", root2)

        for i, addr in enumerate(picList):
            filename = self.createFilename(pageNumber, i, addr)
            file_path = os.path.join(root2, filename)

            # 多进程下载图片
            self.callCurlThroughSubprocess(file_path, addr)

        time.sleep(10)
        self.checkAndRedownload(root2, pageNumber, picList)

    @staticmethod
    def createFilename(pageNumber, index, addr):
        # 解决 windows 不区分大小写的问题
        return "".join([pageNumber, "_", str(index), "_", addr.split("/")[-1]])

    @staticmethod
    def callCurlThroughSubprocess(file_path: str, addr: str):
        # 感觉curl,比wget快一点
        process = subprocess.Popen(
            ["curl", "-C", "-", "-S", "-s", "-o", file_path, addr]
        )
        return process

    @staticmethod
    def callWgetThroughSubprocess(file_path: str, addr: str):
        process = subprocess.Popen(
            ["wget", "-O", file_path, "-q", "-o", "/tmp/wget-log",  addr]
        )
        return process

    def checkAndRedownload(self, root2, pageNumber, picList):
        for i, addr in enumerate(picList):
            filename = self.createFilename(pageNumber, i, addr)
            file_path = os.path.join(root2, filename)

            # 如果下载不成功，需要换方法
            if not os.path.exists(file_path):
                print("file to check:", filename)
                #self.callWgetThroughSubprocess(file_path, addr)
                self.SaveOnePictureFrom(addr, file_path)

    def SaveOnePictureFrom(self, url:str, file_path:str):
        response = requests.get(url,headers=self.kv)
        with open(file_path,"wb") as f:
            f.write(response.content)

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
