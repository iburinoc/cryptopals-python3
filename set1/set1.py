import base64

fromhex = bytes.fromhex

# 1.1
def hextob64(s):
    return base64.b64encode(fromhex(s))

def xorbytes(a, b):
    return bytes(ca ^ cb for ca, cb in zip(a, b))

# 1.2
def xorhex(a, b):
    return xorbytes(fromhex(a), fromhex(b)).hex()

def xorrepeatingkey(p, k):
    return xorbytes(p,
        (k[i % len(k)] for i in range(len(p)))
    )

# 1.5
def encryptrepeatingkeyxor(p, k):
    p = p.encode('ascii')
    k = k.encode('ascii')
    return xorrepeatingkey(p, k).hex()
