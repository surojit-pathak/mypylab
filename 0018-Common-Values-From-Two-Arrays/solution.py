#!/bin/python
import sys
import Queue

def find_arr_intersect(a, b):
    a = sorted(a)
    b = sorted(b)
    n = len(a)
    m = len(b)
    
    alow = a[0]
    ahigh = a[n - 1]
    blow = b[0]
    bhigh = b[m - 1]
    
    if ahigh < blow or alow > bhigh:
       return []
       
    ul = []   
    for x in a:
        for y in b:
            if x == y:
               ul.append(x)
               break
            if y > x:
               break
    
    return ul 

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    
    a = map(lambda x: int(x), raw_input(input_fp).split())
    b = map(lambda x: int(x), raw_input(input_fp).split())
    for x in find_arr_intersect(a, b):
        print x,
    print

if __name__ == '__main__':
    main()
