import requests
import os
import re
from urllib.parse import quote_plus, unquote_plus
 
def get_page(url,page_num):
    pageList =[]
    for i in range(1,page_num +1):
        formdata ={
                    'txtCorpName': None,
                    'txtName': None,
                    'txtIdCard':None,
                    'txtIdCard':'360723199104131212' ,
                    "__EVENTTARGET": None,
                    "__EVENTARGUMENT":None,
                    "__VIEWSTATE":"%2FwEPDwUKLTczMzAxMTI0MQ8WCB4HUGFnZU51bQIBHglQYWdlQ291bnQC4QEeCFNRTFF1ZXJ5BfkBc2VsZWN0IHRvcCAxMCAqIGZyb20gKCBzZWxlY3Qgcm93X251bWJlcigpIG92ZXIgKCBvcmRlciBieSBFbmRQdWJsaWNpdHlUaW1lIGRlc2MsQnVzSUQgZGVzYykgYXMgdGVtcGlkLCogZnJvbSBCdXNpbmVzc19QZXJzb25JbnRyb2R1Y2VQdWJsaWNpdHlWaWV3IHdoZXJlIFByb2NJRCA9ICcyJyBhbmQgRW5kUHVibGljaXR5VGltZT4nMjAxOS83LzE0IDk6MDY6MzUnICkgYXMgYSAgd2hlcmUgdGVtcGlkIGJldHdlZW4gezB9IGFuZCB7MX0gHglTUUxQYXJhbXMWABYCAgEPZBYIAgkPPCsACwEADxYIHghEYXRhS2V5cxYKBSBmNmMzNzE3NWU3ZTc0YmJhOGEwYjVjZmZlMDVlNTkxMAUgNzhkNGI0NTAxYzE3NDhlN2JlYmYxOTVjZTA3ZWQwN2IFIDczN2JjZTU0NTIyNTQ2MTM4YjQ4YmY1Mzg2ZGZlZmM4BSAwNWY2MDVkYzZiMTY0MDBhYjBmMTFlYzI1N2Y2ODkwMQUgMDQyZDVlMWU4ZjQ0NDA2N2JhZTkyZDA2NWE0OGFlNTQFIGY4OTVhZTUwNGM0MTRiNjZhZjY0NGE0MDcyOTliNDBjBSBjZmE2NThkZDEyNDQ0NDNhYTRkMmFiMWZmNjM5YTllNAUgMWRkOTA1YTkzMmQwNDk4NGIyODVkNjQ2M2QzNmVmY2MFIGUxMWU0MWVkZjAzYTQyYTVhMzc1ZmY5YjcyYzM0OTcxBSBkOGIxNGUyNTM4ZGQ0MWEwOTVkZmYwZTYxZmQ3NDY4NR4LXyFJdGVtQ291bnQCCh8BAgEeFV8hRGF0YVNvdXJjZUl0ZW1Db3VudAIKZBYCZg9kFhQCAQ9kFgxmDw8WAh4EVGV4dAUJ6ZmI6Imv5Z2kZGQCAQ8PFgIfBwUw5bm%2F5Lic5bm%2F54mp5Lqs5a6J5rG96L2m6ZSA5ZSu5pyN5Yqh5pyJ6ZmQ5YWs5Y%2B4ZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjA3ZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowN2RkAgIPZBYMZg8PFgIfBwUJ6LCi5a2f5Z2KZGQCAQ8PFgIfBwUt5bm%2F5bee5biC5aKe5Z%2BO546J6Iiq5pWZ6IKy5ZKo6K%2Bi5pyN5Yqh5Lit5b%2BDZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjAxZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowMWRkAgMPZBYMZg8PFgIfBwUJ6K6457Kf5YWwZGQCAQ8PFgIfBwUY5aKe5Z%2BO5biC5bm%2F576O6ZOd5p2Q5Y6CZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjAxZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowMWRkAgQPZBYMZg8PFgIfBwUJ5YiY5Y%2BR6L6JZGQCAQ8PFgIfBwUk5bm%2F5bee5LyX6LGq5pyN6KOF6K6%2B6K6h5pyJ6ZmQ5YWs5Y%2B4ZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjAxZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowMWRkAgUPZBYMZg8PFgIfBwUJ6buE5b2p6ZyeZGQCAQ8PFgIfBwUe5bm%2F5bee5biC5aKe5Z%2BO5Yy65pil5pmW5a2m5qChZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjAxZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowMWRkAgYPZBYMZg8PFgIfBwUJ5Y%2Bk5Y2r5by6ZGQCAQ8PFgIfBwUn5bm%2F5bee5biC6IuP5rqQ55S15Yqb6K6%2B5aSH5pyJ6ZmQ5YWs5Y%2B4ZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjAxZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowMWRkAgcPZBYMZg8PFgIfBwUJ6LCi5bCP5LqRZGQCAQ8PFgIfBwUk5bm%2F5bee6IW%2B5aiB56eR5oqA6IKh5Lu95pyJ6ZmQ5YWs5Y%2B4ZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjAxZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowMWRkAggPZBYMZg8PFgIfBwUJ6ZmI5rui5769ZGQCAQ8PFgIfBwUq5bm%2F5rG95pys55Sw5rG96L2m56CU56m25byA5Y%2BR5pyJ6ZmQ5YWs5Y%2B4ZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjAxZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowMWRkAgkPZBYMZg8PFgIfBwUJ5p2O5qKF6IqzZGQCAQ8PFgIfBwUq5aKe5Z%2BO5biC56Kn5qGC5Zut54mp5Lia5Y%2BR5bGV5pyJ6ZmQ5YWs5Y%2B4ZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjAwZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowMGRkAgoPZBYMZg8PFgIfBwUJ5L2V6L22576kZGQCAQ8PFgIfBwU56Zi%2F6YeM5be05be05Y2O5Y2X5oqA5pyv5pyJ6ZmQ5YWs5Y%2B45bm%2F5bee5aKe5Z%2BO5YiG5YWs5Y%2B4ZGQCAg8PFgIfBwUG5ZCM5oSPZGQCAw8PFgIfBwU%2B5bm%2F5bee5biC5aKe5Z%2BO5Yy65Lq65Yqb6LWE5rqQ5ZKM56S%2B5Lya5L%2Bd6Zqc5bGAKOWOn%2BS6uuS6i%2BWxgClkZAIEDw8WAh8HBRYyMDE55bm0N%2BaciDEy5pelIDE3OjAwZGQCBQ8PFgIfBwUWMjAxOeW5tDfmnIgxOeaXpSAxNzowMGRkAgsPDxYCHwcFAzIyNWRkAg0PDxYCHgdFbmFibGVkaGRkAg8PDxYCHwhoZGRk338O3BCbzuunXQrKJAGMtRBCIvsJ1MWC%2Bi2uctbodP0%3D"
                    'btnSearch':'%E6%9F%A5%E8%AF%A2'
                    'ToPage':'1'
                    }
        try:
            r = requests.post(url,data =formdata)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print('链接成功')
            print(r.text)
            #p = re.compile(r'href="(http://www.jdlingyu.net/\d{5}/)"')
            #tempList = re.findall(p,r.text)
            #for each in tempList:
            #    pageList.append(each)
            #    print('保存页面成功')
            #tempList = []
            #if r.text.find('文思') > -1:
            if r.text.find('广汽本田') > -1:
                print('=====================同意入户')
        except:
            print('链接失败')
    return 0 
 
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
 

if __name__ == '__main__':
    #url = 'http://www.jdlingyu.net/'
    #kv = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    #picList = get_picure(pageList)
    #down_picture(picList,root)
    url = 'http://gzrsj.hrssgz.gov.cn/vsgzpiapp01/GZPI/Gateway/PersonIntroducePublicity.aspx'
    kv = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    pageList = get_page(url,1)
