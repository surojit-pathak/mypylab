#!/bin/python
import sys

def find_minimum_candies_required(ranks, n):
    candies = [ 1 for i in range(0,n) ]
    for i in range(1, n):
        if ranks[i-1] < ranks[i] and candies[i-1] >= candies[i]:
            candies[i] = candies[i-1] + 1
    for i in range(n-2, -1, -1):
        if ranks[i] > ranks[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1
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
