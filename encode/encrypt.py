from Crypto.Cipher import DES

key = b'abcdefgh'  # 密钥 8位或16位,必须为bytes


def pad(text):
    """
    # 加密函数，如果text不是8的倍数【加密文本text必须为8的倍数！】，那就补足为8的倍数
    :param text: 
    :return: 
    """
    while len(text) % 8 != 0:
        text += ' '
    return text


des = DES.new(key, DES.MODE_ECB)  # 创建一个DES实例
#text = 'Python rocks!'
text = input('Please input pactera password: ')
padded_text = pad(text)
encrypted_text = des.encrypt(padded_text.encode('utf-8'))  # 加密

print(encrypted_text)

with open("pactera_passwd_encrpt.txt","wb") as f:
    #f.write(str(encrypted_text))
    f.write(encrypted_text)
