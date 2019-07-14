import os
from removebg import RemoveBg

rmbg = RemoveBg("psCaKrA5rUMXJ6A12H8Kirup", "error.log")  # 引号内是你获取的API
rmbg.remove_background_from_img_file("/mnt/d/picture/图像/m/DSC_0040 - 副本.jpg")  # 图片地址

#path = "/mnt/d/picture/cqb/anan"
#for pic in os.listdir(path):
#    path_name = os.path.join(path, pic)
#    rmbg.remove_background_from_img_file(path_name)  # 图片地址
