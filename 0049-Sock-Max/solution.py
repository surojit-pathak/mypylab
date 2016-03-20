#!/bin/python
import sys

def find_index_of_maximum(sprice, start, end):
    m = sprice[start]
    maxi = start
    for i in range(start+1, end+1):
        if sprice[i] > m:
            m = sprice[i]
            maxi = i
    return maxi

def calc_profit(sprice, start, end):
    inv = count = 0
    for i in range(start, end):
        inv += sprice[i]
        count += 1
    return (count * sprice[end]) - inv

def calculate_maximum_gain(sprice, start, end):
    if start >= end:
        return 0
    maxi = find_index_of_maximum(sprice, start, end)
    return calc_profit(sprice, start, maxi) + calculate_maximum_gain(sprice, maxi+1, end)
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    t = map(lambda x: int(x), raw_input(input_fp).split())[0]
    while t:
        t -= 1
        n = map(lambda x: int(x), raw_input(input_fp).split())[0]
        sprice = map(lambda x: int(x), raw_input(input_fp).split())
        print calculate_maximum_gain(sprice, 0, n-1)

if __name__ == '__main__':
    main()
