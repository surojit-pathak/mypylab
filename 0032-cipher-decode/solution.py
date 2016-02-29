#!/bin/python
import sys

def cipher_decode(outp, n, k):
    inp = [ 0 for x in range(0, n) ]
    for i in range(0, n):
        if i == 0:
           inp[i] = outp[i]
        else:
           if i < k:
              inp[i] = outp[i] ^ outp[i-1]
           else:
              prod = inp[i-k+1]
              for j in range(i-k+2, i):
                  prod = prod ^ inp[j]
              inp[i] = outp[i] ^ prod
    inp = map(lambda x: str(x), inp)
    print ''.join(inp)

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n, k = map(lambda x: int(x), raw_input(input_fp).split())
    outp = [ int(x) for x in raw_input(input_fp) ]
    cipher_decode(outp, n, k)

if __name__ == '__main__':
    main()
