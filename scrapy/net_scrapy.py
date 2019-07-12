import requests
import os
import re
 
def get_page(url,page_num):
    pageList =[]
    for i in range(1,page_num +1):
        formdata ={'type':'index' ,
                   'paged': i}
        try:
            r = requests.post(url,data =formdata)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print('链接成功')
            p = re.compile(r'href="(http://www.jdlingyu.net/\d{5}/)"')
            tempList = re.findall(p,r.text)
            for each in tempList:
                pageList.append(each)
                print('保存页面成功')
            tempList = []
        except:
            print('链接失败')
    print(pageList)
    return pageList
 
def get_picure(pageList):
    """
    --------------------- 
    作者：c350577169 
    来源：CSDN 
    原文：https://blog.csdn.net/c350577169/article/details/80410133 
    """
    picList = []
    for each in pageList:
        try:
            r = requests.get(each,headers = kv)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            p = re.compile('http://img.jdlingyu.mobi/[^"]+\.jpg|http://w[wx][23].sinaimg.cn/[^"]+\.jpg')
            tempList = re.findall(p,r.text)
            for each in tempList:
                picList.append(each)
                print('保存图片链接成功')
            tempList = []
        except:
            print('保存图片链接失败')
    return picList
def down_picture(picList,root):
    picList = list(set(picList))
    if not os.path.exists(root):
        os.mkdir(root)
    for each in picList:
        path = root + each.split('/')[-1]
        if not os.path.exists(path):
            r = requests.get(each,headers = kv)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                print('动图已保存')
        else:
            print('动图已存在')
 
url = 'http://www.jdlingyu.net/'
kv = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
root = 'D://绝对领域//'
pageList = get_page(url,2)
picList = get_picure(pageList)
down_picture(picList,root)
