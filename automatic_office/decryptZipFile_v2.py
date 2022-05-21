import os
# import py7zr
from itertools import product
import subprocess

filepath = r"D:\code_test\game_test\confidential_data"
namepath = r"D:\code_test\game_test\confidential_data\pvideo.7z"


def verify_password(pwd):
    cmd = f'7z t -p{pwd} {namepath}'
    #print(f"test cmd: {cmd}")
    status = subprocess.call(cmd)
    return status


def unzip_file_other_folder(pwd):
    print(f'___________________________________ 正确的密码是：{pwd}')
    with open(r"D:\code_test\game_test\confidential_data\pvideo_pwd.txt", "w") as f:
        f.write(pwd)

    cmd = f'7z x -p{pwd} {namepath} -y -aos -o "{filepath}\girl"'
    subprocess.call(cmd)


def decryptZipFile(length):
    chars = "pvideoklgirl0123456789"
    passwords = product(chars, repeat=length)
    for pwd in passwords:
        pwd = "".join(pwd)
        print(f'Try password {pwd} ...')
        status = verify_password(pwd)
        if status == 0:
            unzip_file_other_folder(pwd)
            return "Success"

    return "Failed"


def bruteforce():
    for length in range(1, 13):
        status = decryptZipFile(length)
        if status == "Success":
            return "Success"

    print("破解失败")
    return "Failed"


if __name__ == '__main__':
    os.chdir(r"D:\code_test\game_test\confidential_data")
    # decryptZipFile("girl_r15.7z")
    # decryptZipFile()

    bruteforce()

    ### important call from cmd
