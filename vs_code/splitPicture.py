from PIL import Image
import os
import cv2


class SplitPicture(object):
    def __init__(self):
        self.path = "/mnt/c/Users/klgentle/Desktop/老婆专用"

    def splitPicture(self):
        # for filename in os.listdir(self.path):
        for folderName, subfolders, filenames in os.walk(self.path):
            for filename in filenames:
                if isinstance(filename, list):
                    print(f"filename:{filename} list ")
                    continue
                if not filename.endswith("png"):
                    continue

                #if filename not in ("2019-05-13 163920.png"):
                #    continue
                print(f"filename:{filename}")
                file_whole_name = os.path.join(self.path, folderName, filename)

                img = cv2.imread(file_whole_name)
                #cropped = img[85:660, :] # cut half
                cropped = img[120:-120, :] # cut head tail
                x, y = cropped.shape[0:2]
                img_test1 = cv2.resize(cropped, (int(y / 2.2), int(x / 2.2)))
                cv2.imwrite(file_whole_name, img_test1)


if __name__ == "__main__":
    a = SplitPicture()
    a.splitPicture()
