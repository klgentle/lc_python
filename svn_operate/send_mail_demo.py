#!/usr/bin/python3
import traceback
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from sys import argv


sender = "klgentle4@outlook.com"
mail_to = [sender]


def mail(date_str=None):
    time_str = time.strftime("%H:%M:%S", time.localtime())
    try:
        message = MIMEMultipart()
        message["From"] = formataddr(["Florian", sender])
        message["To"] = formataddr(["Dear", ",".join(mail_to)])
        message["Subject"] = f"UAT {date_str}beta update {time_str}"

        message.attach(
            MIMEText(
                f"Dear all,\n\n\tSIT, UAT program update {date_str}.\n\nBest Regards\nDong Jian",
                "plain",
                "utf-8",
            )
        )

        server = smtplib.SMTP("outlook.office365.com", 587)  # 发件人邮箱中的SMTP服务器，一般端口是25
        server.starttls()
        password = input("Passwd: ")
        server.login(sender, password)
        server.sendmail(sender, mail_to, message.as_string())
        server.quit()  # 关闭连接
        print("邮件发送成功")

    except Exception as e:
        traceback.print_exc()
        print("邮件发送失败")


if __name__ == "__main__":
    date_str = time.strftime("%Y%m%d", time.localtime())
    mail(date_str)
