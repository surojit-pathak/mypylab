#!/bin/python
import sys

import math
abet = {0:'', 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
abet = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def roman_to_decimal(r):
    max = total = 0
    rl = [ x for x in r.upper() ]
    rl.reverse()
    for l in rl:
        v = abet[l]
        if v < max:
           v = -v
        else:
           max = v
        total = total + v
    return total

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    while n:
        n = n - 1
        r = raw_input(input_fp)
        print roman_to_decimal(r)
      

if __name__ == '__main__':
    main()
