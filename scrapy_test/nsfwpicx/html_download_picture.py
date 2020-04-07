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
        title = "_"
        # try:
        #    pass
        # except Exception as e:
        #    print("保存图片链接失败:", e.__doc__)

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
        # picture_text = soup.find_all(attrs={"itemprop": "articleBody"})
        # pprint.pprint("-------------picture_text",picture_text)

        # pprint.pprint(r.text)
        # p = re.compile("https://qpix.com/images/\d{4}/\d{2}/\d{2}/\w*\.jpg")
        p = re.compile(
            "(https://qpix.com/images/\d{4}/\d{2}/\d{2}/\w*\.jpg|http://85.117.234.129/images/\d{4}/\d{2}/\d{2}/\w*\.jpg)"
        )
        # tempList = re.findall(p, str(picture_text))
        tempList = re.findall(p, r.text)
        for addr in tempList:
            picList.append(addr)
            # print("-------------test each addr:", addr)
        if len(picList) > 0:
            print("保存图片链接成功", pageNumber)
        tempList = []
        pprint.pprint(list(set(picList)))

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
        # os.chdir(root2)
        for i, addr in enumerate(picList):
            # 解决 windows 不区分大小写的问题
            filename = "".join([str(i), "_", addr.split("/")[-1]])
            file_path = os.path.join(root2, filename)

            # 多进程下载图片
            subprocess.Popen(['curl', addr, '-o', file_path, '--silent'])
            print("图片下载中", pageNumber)

        # if not os.path.exists(file_path):
        #    pass
        #    # save file
        #    #r = requests.get(addr, headers=self.kv)
        #    #r.raise_for_status()
        #    #with open(file_path, "wb") as f:
        #    #    f.write(r.content)
        #    #urllib.request.urlretrieve(addr,filename=file_path)
        #    #print("图片已保存")

        # else:
        #    print("-------------------图片已存在")

    def download_one_html(self, pageNumber):
        titlelist = self.get_picure_addrs(pageNumber)
        self.download_picture(titlelist, pageNumber)

    def download_all_pictures(self, from_number, end_number):
        for i in range(from_number, end_number, -1):
            print("Deal with page index:", i)
            self.download_one_html(i)
            # 休息，防止被封, 等并行的下载完成
            sleep_second = 30
            print("---------Sleep {} second start--------- ...".format(sleep_second))
            time.sleep(sleep_second)
            print("---------Sleep {} second end---------\n".format(sleep_second))


if __name__ == "__main__":
    g = GetNsfwPicture()
    #pageNumber = 881
    #g.download_one_html(pageNumber)

    from_number = 1249
    end_number = 1229
    #end_number = 1200
    g.download_all_pictures(from_number, end_number)
