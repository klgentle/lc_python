#coding=utf-8
from PIL import Image #需要pillow库
import os
#import cv2

class SplitPicture(object):
    """
    剪切手机图片，主要是剪掉图片头部跟图片下方的答案
    """

    def __init__(self):
        self.path = "/mnt/f/for_wife"

    def splitPicture(self):
        #for filename in os.listdir(self.path):
        for folderName, subfolders, filenames in os.walk(self.path):
            for filename in filenames:
                if isinstance(filename,list):
                    #print(f"filename:{filename} list ")
                    continue
                if not filename.endswith('png'):
                    continue

                #if filename != '2019-05-13 163927.png':
                #    continue
                #print(f"filename:{filename}")

                file_whole_name = os.path.join(self.path,folderName,filename)
                img = Image.open(file_whole_name)
                w,h = img.size
                h = 850
                print(f"w,h:{w},{h}")
                box1 = (0,120,w,h)
                image1 = img.crop(box1)
                percent = 2.2
                image1 = image1.resize((int(w/percent), int((h-60)/percent)))
                image1.save(file_whole_name)


if __name__ == "__main__":
    a = SplitPicture()
    a.splitPicture()
