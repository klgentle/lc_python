from Crypto.Cipher import DES
key = b'abcdefgh'  # 密钥 8位或16位,必须为bytes

def get_passwd():
    des = DES.new(key, DES.MODE_ECB)  # 创建一个DES实例
    #f = open("pactera_passwd_encrpt.txt","r")
    # str 转二进制通过encode()
    #encrypted_text = f.read().encode()
    encrypted_text = "" 
    # rstrip(' ')返回从字符串末尾删除所有字符串的字符串(默认空白字符)的副本
    return des.decrypt(encrypted_text).decode().rstrip(' ')  # 解密
