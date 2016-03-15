#!/bin/python
import sys

def maximum_possible_gain(sprice, n):
    prof = 0
    min = sprice[0]
    for i in range(1, n):
        if sprice[i] < min:
            min = sprice[i]
        elif sprice[i] - min > prof:
            prof = sprice[i] - min

    return prof
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    sprice = map(lambda x: int(x), raw_input(input_fp).split())
    print maximum_possible_gain(sprice, n)

if __name__ == '__main__':
    main()
