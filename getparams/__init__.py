from Crypto.Cipher import AES
import base64

# 获取参数


def get_params(text):
    first_key = "0CoJUm6Qyw8W8jud"
    second_key = "FFFFFFFFFFFFFFFF"
    h_encText = AES_encrypt(text, first_key)
    h_encText = AES_encrypt(h_encText, second_key)
    return h_encText

# 获取 encSecKey


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7\
            a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d\
            512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b\
            54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey

# 加密过程


def AES_encrypt(text, key):
    iv = "0102030405060708"
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    encrypt_text = str(encrypt_text, encoding="utf-8")
    # 注意一定要加上这一句，没有这一句则出现错误
    return encrypt_text
