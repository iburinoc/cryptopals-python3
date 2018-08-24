from os import path

from .set1 import *
from .c3 import decrypt as c3decrypt
from .c3 import decryptbest as c4decrypt

def test():
    assert b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t' == hextob64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

    assert '746865206b696420646f6e277420706c6179' == xorhex('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')

    assert 'Cooking MC\'s like a pound of bacon' == c3decrypt('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    assert 'Now that the party is jumping\n' == c4decrypt(
        s.strip() for s in 
            open(path.join(path.dirname(path.abspath(__file__)), '4.txt')).readlines()
        )

    assert '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f' == \
        encryptrepeatingkeyxor("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", "ICE")

if __name__ == '__main__':
    test()
    print('set1 passed')
