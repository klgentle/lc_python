import os
import py7zr


def decryptZipFile(filename):
    print("current dir is: ", os.getcwd())
    print(f"filename is: {filename}")

    a = 0
    with open('pwd_guss.txt', "r", encoding="utf8") as fpPwd:
        for pwd in fpPwd:
            pwd = pwd.rstrip()
            print(f'Try password {pwd} ...')
            try:
                qz = py7zr.SevenZipFile(filename, password=pwd)
                qz.extractall()
                print("破解成功，密码是" + pwd)
                a += 1
                break
            except:
                pass
        if a == 0:
            print("破解失败")


if __name__ == '__main__':
    os.chdir(r"D:\code_test\game_test\confidential_data")
    #decryptZipFile("girl_r15.7z")
    #decryptZipFile("pvideo.7z")
    decryptZipFile("personal.7z")

