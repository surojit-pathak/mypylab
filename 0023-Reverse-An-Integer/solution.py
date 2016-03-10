#!/bin/python
import sys

def find_reversed_int(n):
    d = [ x for x in str(n) ]
    d.reverse()
    return int(''.join(d))
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    print find_reversed_int(n)


if __name__ == '__main__':
    main()
