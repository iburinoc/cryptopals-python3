import base64
import itertools
from os import path

from .set1 import *
from .c3 import candidate

def popcnt(v):
    return bin(v).count('1')

def hamdist(a, b):
    return sum(popcnt(ca ^ cb) for ca, cb in zip(a, b))

def score(b, ks):
    blocks = [b[i*ks:i*ks+ks] for i in range(4)]
    scores = list(hamdist(a, b) / ks for a, b in itertools.combinations(blocks, 2))
    return sum(scores) / len(scores)



# 1.6
def breakvigenere(b, kss):
    kss = list(kss)
    cands = list((score(b, ks), ks) for ks in kss)
    cands = sorted(cands)

    bestscore = float('-inf')
    bestres = b
    bestkey = b'\0'

    for _, ks in cands[:5]:
        sc = 0
        res = [''] * len(b)
        key = [''] * ks
        for i in range(ks):
            val = candidate(b[i::ks])
            sc += val[0]
            res[i::ks] = val[1]
            key[i] = val[2]
        if sc > bestscore:
            bestscore = sc
            bestres = bytes(res)
            bestkey = bytes(key)
    return bestkey

if __name__ == '__main__':
    text = base64.b64decode(
        open(path.join(path.dirname(path.abspath(__file__)), '6.txt')).read().strip()
    )
    key = breakvigenere(text, range(2, 41))

    print(key)
    print(xorrepeatingkey(text, key).decode('ascii'))
