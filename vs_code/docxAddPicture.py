from PIL import Image
import os
import cv2
from docx import Document


class SplitPicture(object):
    def __init__(self):
        self.path = "/mnt/c/Users/klgentle/Desktop/老婆专用"
        os.chdir(self.path)

    def splitPicture(self):
        # for filename in os.listdir(self.path):
        for folderName, subfolders, filenames in os.walk(self.path):
            document = Document()
            for filename in filenames:
                if isinstance(filename, list):
                    print(f"filename:{filename} list ")
                    continue
                if not filename.endswith("png"):
                    continue

                # if filename in ('2019-05-13 163910.png','2019-05-13 163915.png'):
                #    continue
                print(f"filename:{filename}")
                file_whole_name = os.path.join(self.path, folderName, filename)

                #img = cv2.imread(file_whole_name)
                #cropped = img[85:660, :]
                #x, y = cropped.shape[0:2]
                #img_test1 = cv2.resize(cropped, (int(y / 2.2), int(x / 2.2)))
                #cv2.imwrite(file_whole_name, img_test1)
                
                # doc add picture
                document.add_picture(file_whole_name)
            document.save(folderName+'.docx')

    #def docxAddPicture(self):

        


if __name__ == "__main__":
    a = SplitPicture()
    a.splitPicture()
