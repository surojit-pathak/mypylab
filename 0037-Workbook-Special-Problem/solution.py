#!/bin/python
import sys

def find_special_problems(chaps, n, k):
    count = 0
    curp = 1
    for t in chaps:
        p = t / k
        if t % k != 0:
            p = p + 1
        endp = curp + p - 1
        c = 1
        for p in range(curp, endp + 1):
            if p in range(c, min(t+1, (c + k))):
                count = count + 1
            c = c + k
        curp = endp + 1
    print count

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n,k = map(lambda x: int(x), raw_input(input_fp).split())
    chaps = map(lambda x: int(x), raw_input(input_fp).split())
    find_special_problems(chaps, n, k)

if __name__ == '__main__':
    main()
