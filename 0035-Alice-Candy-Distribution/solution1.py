#!/bin/python
import sys

def fix_left_subarr(ranks, candies, k):
    for i in range(k, 0, -1):
        if ranks[i-1] > ranks[i] and candies[i-1] <= candies[i]:
           candies[i-1] = candies[i-1] + 1
        else:
           break
    
def find_minimum_candies_required(ranks, n):
    candies = [ 1 for i in range(0,n) ]
    for i in range(1, n):
        if ranks[i-1] > ranks[i]:
            fix_left_subarr(ranks, candies, i)
        elif ranks[i-1] < ranks[i]:
            candies[i] = candies[i-1] + 1
        else:
            candies[i] = 1
    sum = 0
    for i in candies:
       sum = sum + i    
    print sum

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    t = n
    ranks = []
    while t:
        t = t - 1
        ranks.append(map(lambda x: int(x), raw_input(input_fp).split())[0])
    find_minimum_candies_required(ranks, n)

if __name__ == '__main__':
    main()
