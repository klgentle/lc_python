#!/usr/bin/python3
 
import traceback
import time
import os

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from pysnooper import snoop
from getpass import getpass
from sys import argv


sender = 'jian.dong2@pactera.com'  # 发件人邮箱
#password = ''  # 发件人邮箱密码
addressed_eamil = 'klgentle@sina.com'  # 收件人邮箱
addressed_eamil2 = ['jiarui.qiu@pactera.com','klgentle@sina.com']  # 收件人邮箱
#addressed_eamil2 = ['jian.dong2@pactera.com','klgentle@sina.com']  # 收件人邮箱
 
#@snoop()
def mail(date_str=None, file_path=""):
    """
    作者：梦忆安凉 
    原文：https://blog.csdn.net/a54288447/article/details/81113934 
    """
    home_path = "/home/klgentle"
    time_str = time.strftime("%H:%M:%S", time.localtime())
    if not os.path.exists(home_path):
        home_path = "/mnt/e"
    if not date_str:
        date_str = time.strftime("%Y%m%d", time.localtime())
    if not file_path:
        file_path = f'{home_path}/yx_walk/beta/{date_str}beta.zip'
    #print(file_path)
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr(['jdong', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # send to multi people, 1.message to should join by comma, 2.sending to should be list
        message['To'] = formataddr(['Dear', ','.join(addressed_eamil2)])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = f"UAT {date_str}beta update {time_str}"  # 邮件的主题，也可以说是标题
 
        # 邮件正文内容
        message.attach(MIMEText(f'SIT, UAT program update {date_str}.', 'plain', 'utf-8'))
 
        # 构造附件1
        #att1 = MIMEText(open('D:/PycharmProjects/Vuiki/Common/测试.txt', 'rb').read(), 'base64', 'utf-8')
        #att1["Content-Type"] = 'application/octet-stream'
        ## filename是附件名，附件名称为中文时的写法
        #att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "测试.txt"))
        #message.attach(att1)
 
        # 构造附件2
        att2 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        #附件名称非中文时的写法
        att2["Content-Disposition"] = f'attachment; filename="{date_str}beta.zip")'
        message.attach(att2)
 
        #server = smtplib.SMTP_SSL("smtp.office365.com", 847)  # 发件人邮箱中的SMTP服务器，一般端口是25
        server = smtplib.SMTP("smtp.office365.com", 587)  # 发件人邮箱中的SMTP服务器，一般端口是25
        server.starttls()
        # to get passwd
        #password = getpass(f"{sender}'s password: ")
        password = os.popen('awk \'FS="=" {if ($0~/^pactera_passwd/) print $2}\' $HOME/.passwd.txt').read()
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # multi people shoud be list
        server.sendmail(sender, addressed_eamil2, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")

    except Exception as e:
        traceback.print_exc()
        print("邮件发送失败")
 
if __name__ == "__main__":
    date_str = time.strftime("%Y%m%d", time.localtime())
    if len(argv) > 1 and len(argv[1]) == 8:
        date_str = argv[1]

    mail(date_str)
