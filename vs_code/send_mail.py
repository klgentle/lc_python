import smtplib
from pysnooper import snoop


#@snoop()
def send_mail():
    from_email = "jian.dong2@pactera.com"

    smtpObj = smtplib.SMTP('smtp.office365.com',587)
    ret = smtpObj.ehlo()
    if ret[0] != 250: 
        print("Smtp say hello failed!")
        return -1
    ret = smtpObj.starttls()
    if ret[0] != 220: 
        print("smtp tsl encode failed!")
        return -1
    password = input(f"Please input your passwd of {from_email}: ")
    ret = smtpObj.login(from_email, password) 
    if ret[0] != 235: 
        print("Smtp login failed!")
        return -1
    # 电子邮件正文字符串必须以'Subject: \n'开头，作为电子邮件的主题 行。'\n'换行符将主题行与电子邮件的正文分开。
    ret = smtpObj.sendmail('jian.dong2@pactera.com','klgentle@sina.com',
        'Subject: SMTP mail test, long time no see.\nThanks for all your help, sincerely, klgentle')
    if ret != {}: 
        print("Smtp send mail failed!")
        return -1
    smtpObj.quit()
    print("mail send success!")
    return 0


if __name__ == '__main__':
    send_mail()
