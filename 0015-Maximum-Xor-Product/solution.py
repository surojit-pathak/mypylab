#!/bin/python

def find_max_xor(a, b):
    max = 0
    while a != b:
       a = a >> 1
       b = b >> 1
       max = (max << 1) + 1
 
    print max
    return max

def main():
    s = int(raw_input())
    t = int(raw_input())
    find_max_xor(s, t)

if __name__ == '__main__':
    main()
