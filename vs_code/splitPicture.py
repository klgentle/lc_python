from PIL import Image
import os
import cv2

class SplitPicture(object):

    def __init__(self):
        self.path = "/mnt/c/Users/klgentle/Desktop/老婆专用"

    def splitPicture(self):
        #for filename in os.listdir(self.path):
        for folderName, subfolders, filenames in os.walk(self.path):
            for filename in filenames:
                if isinstance(filename,list):
                    print(f"filename:{filename} list ")
                    continue
                if not filename.endswith('png'):
                    continue

                print(f"filename:{filename}")

                file_whole_name = os.path.join(self.path,folderName,filename)
                img = Image.open(file_whole_name)
                box1 = (0,0,665,750)
                image1 = img.crop(box1)
                image1.save(file_whole_name)
                
                
                img = cv2.imread(file_whole_name)
                #print(f"img:{img.shape}") #(1334, 750, 3)
                
                x, y = img.shape[0:2]
                img_test1 = cv2.resize(img, (int(y / 2), int(x / 2)))




if __name__ == "__main__":
    a = SplitPicture()
    a.splitPicture()
