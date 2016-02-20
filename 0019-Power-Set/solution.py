#!/bin/python
import sys
import math
import itertools

def generate_values(coins, i):
    values = [0.0]
    tv = []
    j = 0
    while (i >> j) != 0:
        if ((i >> j) & 0x1) == 0x1:
           c, v = coins[j]
           tvl = []
           for k in xrange(1, c + 1):
               values.append(k * v)
               tvl.append(k * v)
           tv.append(tvl)
        j = j + 1
    for elem in itertools.product(*tv):
        sum = 0
        for x in elem:
            sum = sum + x
        values.append(sum)
               
    return values
           
def find_all_possible_values(coins):
    types = len(coins)
    n = int(math.pow(2, types))
    values = set()
    for i in xrange(0, n):
        vals = generate_values(coins, i)
        for v in vals:
            values.add(v)
    return values

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    #coins = {}
    coins = []
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    for i in xrange(0, n):
        type, count, value = raw_input(input_fp).split()
        coins.append((int(count), float(value)))
 
    values = list(find_all_possible_values(coins))
    for v in sorted(values):
        print v,
    print

if __name__ == '__main__':
    main()
