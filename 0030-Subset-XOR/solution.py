#!/bin/python
import sys

def xor_all_contiguous_subarray(arr, n):
    val = 0
    for i in xrange(0, n):
        freq = (n - i) * (i + 1)
        if freq % 2 != 0:
            val = val ^ arr[i]
    print val

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    t = map(lambda x: int(x), raw_input(input_fp).split())[0]
    while t > 0:
        t = t -1
        n = map(lambda x: int(x), raw_input(input_fp).split())[0]
        arr = map(lambda x: int(x), raw_input(input_fp).split())
        xor_all_contiguous_subarray(arr, n)

if __name__ == '__main__':
    main()
