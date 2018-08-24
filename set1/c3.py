from collections import defaultdict
from os import path

from .set1 import *

def countinversions(a, b):
    idx = {}
    for i, c in enumerate(b):
        idx[c] = i
    total = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if idx[a[i]] > idx[a[j]]:
                total += 1
    return total

def score1(eng):
    counts = defaultdict(int)
    for c in eng:
        counts[c] += 1

    order = sorted(list(range(97, 123)), key=lambda x: -counts[x])
    total = sum(counts[x] for x in range(97, 123))
    if total == 0:
        return float('-inf')
    return -countinversions(order, b'etaoinshrdlcumwfgypbvkjxqz') / total

freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}

def score(eng):
    return sum(freqs[chr(c).lower()] for c in eng if chr(c).lower() in freqs)

def process(b, x):
    res = xorbytes(b, bytes(x for _ in range(len(b))))
    return (score(res), res, x)

def candidate(b):
    return max(
        process(b, x) for x in range(256)
    )

# 1.3
def decrypt(s):
    return candidate(fromhex(s))[1].decode('ascii')

# 1.4
def decryptbest(ss):
    return max(
        candidate(fromhex(s)) for s in ss
    )[1].decode('ascii')

if __name__ == '__main__':
    print(decrypt('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
    print(decryptbest(
        s.strip() for s in 
            open(path.join(path.dirname(path.abspath(__file__)), '4.txt')).readlines()
        ))
