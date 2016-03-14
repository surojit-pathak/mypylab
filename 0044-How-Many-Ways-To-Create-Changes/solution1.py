#!/bin/python
import sys

def fn(n, coins, m):
    if m == 0:
       return 0
    if m == 1:
       if n % coins[0] == 0:
          return 1
       else:
          return 0
    if n == 0:
       return 1

    v = coins[m-1]
    ways = 0
    i = 0
    while True:
       t = n - (i * v)
       if t >= 0:
           ways += fn(t, coins, m - 1)
       else:
           break
       i += 1
    return ways

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n,m = map(lambda x: int(x), raw_input(input_fp).split())
    coins = map(lambda x: int(x), raw_input(input_fp).split())
    print fn(n, coins, m)

if __name__ == '__main__':
    main()
