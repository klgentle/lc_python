#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from pysnooper import snoop
import traceback
import time
from getpass import getpass
import os
sender = 'jian.dong2@pactera.com'  # 发件人邮箱
#password = ''  # 发件人邮箱密码
addressed_eamil = 'klgentle@sina.com'  # 收件人邮箱
addressed_eamil2 = ['klgentle@163.com','klgentle@sina.com']  # 收件人邮箱
 
#@snoop()
def mail(date_str=None):
    """
    作者：梦忆安凉 
    原文：https://blog.csdn.net/a54288447/article/details/81113934 
    """
    if not date_str:
        date_str = time.strftime("%Y%m%d", time.localtime())
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr(['jdong', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # send to multi people, 1.message to should join by comma, 2.sending to should be list
        message['To'] = formataddr(['Dear', ','.join(addressed_eamil2)])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = f"测试发送邮件{date_str}"  # 邮件的主题，也可以说是标题
 
        # 邮件正文内容
        message.attach(MIMEText('Python3邮件发送测试。。。', 'plain', 'utf-8'))
 
        # 构造附件1
        #att1 = MIMEText(open('D:/PycharmProjects/Vuiki/Common/测试.txt', 'rb').read(), 'base64', 'utf-8')
        #att1["Content-Type"] = 'application/octet-stream'
        ## filename是附件名，附件名称为中文时的写法
        #att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "测试.txt"))
        #message.attach(att1)
 
        # 构造附件2
        att2 = MIMEText(open(f'/mnt/e/yx_walk/report_develop/sky/{date_str}beta.zip', 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        #附件名称非中文时的写法
        att2["Content-Disposition"] = 'attachment; filename="20190620beta.zip")'
        message.attach(att2)
 
        #server = smtplib.SMTP_SSL("smtp.office365.com", 847)  # 发件人邮箱中的SMTP服务器，一般端口是25
        server = smtplib.SMTP("smtp.office365.com", 587)  # 发件人邮箱中的SMTP服务器，一般端口是25
        server.starttls()
        # to get passwd
        #password = getpass(f"{sender}'s password: ")
        password = os.popen('awk \'FS="=" {if ($0~/^pactera_passwd/) print $2}\' $HOME/passwd.txt').read()
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # multi people shoud be list
        server.sendmail(sender, addressed_eamil2, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")

    except Exception as e:
        traceback.print_exc()
        print("邮件发送失败")
 
if __name__ == "__main__":
    mail()
