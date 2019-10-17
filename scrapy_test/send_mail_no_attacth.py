#!/usr/bin/python3

import traceback
import time
import os

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

# from pysnooper import snoop
# from getpass import getpass
from sys import argv


# password = ''  # 发件人邮箱密码
sender = "klgentle@sina.com"  # 收件人邮箱
addressed_eamil2 = ["jian.dong2@pactera.com", "1063237864@qq.com"]  # 收件人邮箱

# @snoop()
def mail():
    """
    作者：梦忆安凉 
    原文：https://blog.csdn.net/a54288447/article/details/81113934 
    """
    # home_path = "/home/kl"
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message["From"] = formataddr(["jdong", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # send to multi people, 1.message to should join by comma, 2.sending to should be list
        message["To"] = formataddr(
            ["Dear", ",".join(addressed_eamil2)]
        )  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message["Subject"] = "入户审批已公示!"  # 邮件的主题，也可以说是标题

        # 邮件正文内容
        message.attach(
            MIMEText(
                "入户审批已公示，请登陆网址查看\nhttp://gzrsj.hrssgz.gov.cn/vsgzpiapp01/GZPI/Gateway/PersonIntroducePublicity.aspx",
                "plain",
                "utf-8",
            )
        )

        server = smtplib.SMTP_SSL("smtp.sina.com", 465)  # 发件人邮箱中的SMTP服务器，一般端口是25
        server.starttls()
        # to get passwd
        #password = getpass(f"{sender}'s password: ")
        cmd = "awk 'FS=\"=\" {if ($0~/^sina_passwd/) print $2}' $HOME/.passwd.txt"
        password = ""
        with os.popen(cmd) as p:
            password = p.read().strip()
        #print(f"test [{password}]")
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # multi people shoud be list
        server.sendmail(
            sender, addressed_eamil2, message.as_string()
        )  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")

    except Exception as e:
        traceback.print_exc()
        print("邮件发送失败")


if __name__ == "__main__":
    mail()
