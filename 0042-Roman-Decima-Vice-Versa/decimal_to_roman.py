#!/bin/python
import sys

import math

abet = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

def find_maximum_inclusive_radix(n, radix):
    for k in radix:
        if k <= n:
           return k
    
def roman_representation(n):
    if n in abet:
       return abet[n]
    radix = sorted(abet.keys())
    radix.reverse()
    addl = []
    while n:
       k = find_maximum_inclusive_radix(n, radix)
       n = n - k
       addl.append(k)
    return ''.join(map(lambda x: abet[x], addl))

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    print roman_representation(n)

if __name__ == '__main__':
    main()
