from os import path

def detectecb(blocks):
    for j, block in enumerate(blocks):
        if len(set(block[i:i+16] for i in range(0, len(block), 16))) != len(block)/16:
            return j, block

if __name__ == '__main__':

    res = detectecb(
        bytes.fromhex(s.strip()) for s in 
            open(path.join(path.dirname(path.abspath(__file__)), '8.txt')).readlines()
        )
    print(res[0], res[1].hex())
