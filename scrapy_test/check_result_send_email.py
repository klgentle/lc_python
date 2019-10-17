#!/usr/bin/python3
from crawler01 import check_result
from send_mail_no_attacth import mail


if __name__ == "__main__":
    if check_result():
        mail()
    else:
        print("No result, please wait!")
