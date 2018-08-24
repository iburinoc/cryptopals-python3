import base64
from Crypto.Cipher import AES
from os import path

# 1.7
def aesecbdecrypt(c, k):
    cipher = AES.new(k, AES.MODE_ECB)
    return cipher.decrypt(c)

if __name__ == '__main__':
    data = base64.b64decode(
        open(path.join(path.dirname(path.abspath(__file__)), '7.txt')).read().strip()
    )
    print(aesecbdecrypt(data, b'YELLOW SUBMARINE').decode('ascii'))
