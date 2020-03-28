import requests
import os
import re
from urllib.parse import quote_plus, unquote_plus
import random
from bs4 import BeautifulSoup
#import urllib.request
import time
import pprint


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

    @staticmethod
    def change_char_to_number(filename)-> str:
        # xxx.jpg to ord(x)ord(x)ord(x).jpg
        name_list = filename.split(".")
        pre_name = name_list[0]
        for i in pre_name:
            if not i.isdigit():
                name_list[0] = pre_name.replace(i, str(ord(i)))
        return ".".join(name_list)

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
            # tempList = re.findall(p, r.text)

            # 查找阅读人数
            read_num = soup.find_all(attrs={"class": "post-meta"})
            read_number = self.find_read_number(str(read_num))
            print("read_number", read_number)

            # 可能有坑，尤其是新页面阅读量少
            #if read_number < 2000:
            #    print("Read_number to small", pageNumber)
            #    return (" ", None)

            # 精确定位地址集
            picture_text = soup.find_all(attrs={"itemprop": "articleBody"})
            tempList = re.findall(p, str(picture_text))
            for addr in tempList:
                picList.append(addr)
                # print("-------------test each addr:", addr)
            print("保存图片链接成功")
            tempList = []
        except Exception as e:
            print("保存图片链接失败:", e.__doc__)
        picList = sorted(list(set(picList)))
        #pprint.pprint(picList)

        return (title, picList)

    def download_picture(self, title_picList, pageNumber):
        # root 保存目录
        title, picList = title_picList
        root2 = os.path.join(self.root, str(pageNumber) + "_" + title.replace(" ", "_"))
        if not os.path.exists(root2):
            os.mkdir(root2)

        print("folder:", root2)
        for addr in picList:
            filename = addr.split("/")[-1]
            # 解决 windows 不区分大小写的问题
            filename = self.change_char_to_number(filename)
            file_path = os.path.join(root2, filename)
            if not os.path.exists(file_path):
                # save file
                r = requests.get(addr, headers=self.kv)
                r.raise_for_status()
                with open(file_path, "wb") as f:
                    f.write(r.content)
                #urllib.request.urlretrieve(addr,filename=file_path)
                print("动图已保存", pageNumber)
            #else:
            #    print("动图已存在")

    
    def download_one_html(self, pageNumber):
        titlelist = self.get_picure_addrs(pageNumber)
        self.download_picture(titlelist, pageNumber)

    def download_all_pictures(self, from_number, end_number):
        for i in range(from_number, end_number, -1):
            print("Deal with page index:", i)
            self.download_one_html(i)
            # 休息，防止被封
            time.sleep(12)
            print("Sleep 12 second")


if __name__ == "__main__":
    g = GetNsfwPicture()
    #pageNumber = 1162
    #g.download_one_html(pageNumber)

    from_number = 1014
    end_number = 500 
    g.download_all_pictures(from_number, end_number)

    #print("s57I.jpg")
    #print(g.change_char_to_number("s57I.jpg"))
    #print("s57i.jpg")
    #print(g.change_char_to_number("s57i.jpg"))
