from PIL import Image
import pytesseract
#上面都是导包，只需要下面这一行就能实现图片文字识别
file_name ="/mnt/c/Users/klgentle/Desktop/老婆专用/2019版药学（初级西药师）考前押题［专业代码：201］/押题密卷一/专业知识/2019-05-13 223410.png"
text = pytesseract.image_to_string(Image.open(file_name),lang='chi_sim')
print(text)
