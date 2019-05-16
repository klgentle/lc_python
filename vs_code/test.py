from PIL import Image
import os
import cv2

class SplitPicture(object):

    def __init__(self):
        self.path = "/mnt/c/Users/klgentle/Desktop/老婆专用/押题密卷二/基础知识"

    def splitPicture(self):
        for filename in os.listdir(self.path):
            if filename !='2019-05-13 165604.png':
                continue

            file_whole_name = os.path.join(self.path,filename)
            #img = Image.open(file_whole_name)
            #box1 = (0,0,665,750)
            #image1 = img.crop(box1)
            #image1.save(file_whole_name)
            
            
            img = cv2.imread(file_whole_name)
            #print(f"img:{img.shape}") #(1334, 750, 3)
            
            cropped = img[0:660,:]
            x, y = cropped.shape[0:2]
            img_test1 = cv2.resize(cropped, (int(y / 2), int(x / 2)))
            cv2.imwrite(file_whole_name,img_test1)




if __name__ == "__main__":
    a = SplitPicture()
    a.splitPicture()
