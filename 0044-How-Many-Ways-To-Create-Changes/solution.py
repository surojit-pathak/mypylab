#!/bin/python
import sys

def calculate_ways_to_change(k, coins, n):
    ways = [ [ 0 for j in range(0, n) ] for i in range(0, k+1)]
    ways[0] = [ 1 for j in range(0, n) ]
    for i in range(1, k+1):
        if i % coins[0] == 0:
            ways[i][0] = 1
     
    for j in range(1, n):
        for i in range(1, k+1):
            ways[i][j] = ways[i][j-1]
        m = 1
        while True:
            v = m * coins[j]
            m = m + 1
            loop = False
            for i in range(v, k+1):
               ways[i][j] += ways[i-v][j-1]
               loop = True
            if loop is False:
               break

    return ways[k][n-1]
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n,m = map(lambda x: int(x), raw_input(input_fp).split())
    coins = map(lambda x: int(x), raw_input(input_fp).split())
    print calculate_ways_to_change(n, coins, m)

if __name__ == '__main__':
    main()
