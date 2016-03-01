#!/bin/python
import sys

def find_max_expected_sum(items, n, k):
    pchart = [ False for x in range(0, k+1) ]
    pchart[0] = True
    minv = 0
    for i in items:
        if minv == 0:
           minv = i
        elif i < minv:
           minv = i
        if i <= k:
           pchart[i] = True
    for m in range(1, k+1):
        if m < minv:
            continue
        for i in items:
            if m >= i and pchart[m - i]:
                pchart[m] = True
                break
    for j in range(k, -1, -1):
        if pchart[j]:
            print j
            break
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    t = map(lambda x: int(x), raw_input(input_fp).split())[0]
    while t:
        t = t - 1
        n,k = map(lambda x: int(x), raw_input(input_fp).split())
        items = map(lambda x: int(x), raw_input(input_fp).split())
        find_max_expected_sum(items, n, k)

if __name__ == '__main__':
    main()
