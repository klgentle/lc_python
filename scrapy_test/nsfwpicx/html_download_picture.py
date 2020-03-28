import requests
import os
import re
from urllib.parse import quote_plus, unquote_plus
import random
from bs4 import BeautifulSoup
import urllib.request
import time


class GetNsfwPicture(object):
    def __init__(self):
        self.kv = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        self.root = "/mnt/d/code_test/game_test/nsf"
    
    @staticmethod
    def find_read_number(input_str)-> int:
        # 删除非数字(-)的字符串
        return int(re.sub(r'\D', "", input_str))

    def get_picure_addrs(self, pageNumber):
        """
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
            # tempList = re.findall(p, r.text)

            # 查找阅读人数
            read_num = soup.find_all(attrs={"class": "post-meta"})
            read_number = self.find_read_number(str(read_num))
            print("read_number", read_number)

            if read_number < 2000:
                print("read_number to small")
                return (" ", None)

            # 精确定位地址集
            picture_text = soup.find_all(attrs={"itemprop": "articleBody"})
            tempList = re.findall(p, str(picture_text))
            for each in tempList:
                picList.append(each)
                # print("-------------test each addr:", each)
            print("保存图片链接成功")
            tempList = []
        except Exception as e:
            print("保存图片链接失败:", e.__doc__)

        return (title, picList)

    def download_picture(self, title_picList, pageNumber):
        # root 保存目录
        title, picList = title_picList[0], list(set(title_picList[1]))
        root2 = os.path.join(self.root, str(pageNumber) + "_" + title.replace(" ", "_"))
        if not os.path.exists(root2):
            os.mkdir(root2)
        print("folder:", root2)
        for each in picList:
            # 过滤异常的文件
            if each.find("/") == -1:
                print("no / address", each)
                continue
            filename = each.split("/")[-1]
            path = os.path.join(root2, filename)
            if not os.path.exists(path):
                # save file
                r = requests.get(each, headers=self.kv)
                r.raise_for_status()
                with open(path, "wb") as f:
                    f.write(r.content)
                # 休息，防止被封
                time.sleep(1)
                #urllib.request.urlretrieve(each,filename=path)
                print("动图已保存", pageNumber)
            else:
                print("动图已存在")

    
    def download_one_html(self, pageNumber):
        titlelist = self.get_picure_addrs(pageNumber)
        self.download_picture(titlelist, pageNumber)

    def download_all_pictures(self, from_number, end_number):
        for i in range(from_number, end_number, -1):
            print("deal with page index:", i)
            # 休息，防止被封
            time.sleep(20)
            self.download_one_html(i)


if __name__ == "__main__":
    g = GetNsfwPicture()
    #pageNumber = 1162
    #g.download_one_html(pageNumber)

    from_number = 1023
    end_number = 500 
    g.download_all_pictures(from_number, end_number)
