import urllib

def get_result(url):
    page = urllib.urlopen('http://gzrsj.hrssgz.gov.cn/vsgzpiapp01/GZPI/Gateway/PersonIntroducePublicity.aspx')
    htmlcode = page.read().decode('utf-8') # 读取页面源码

