#!/bin/python
import sys

def calculate_modified_fibonacci(a, b, n):
    c = 0
    for x in xrange(3, n + 1):
        c = (b * b) + a
        a = b
        b = c
    return c
        

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    
    a, b, n = map(lambda x: int(x), raw_input(input_fp).split())
    c = calculate_modified_fibonacci(a, b, n)
    print c
    return c

if __name__ == '__main__':
    main()
