#!/bin/python
import copy
import sys

def find_list_of_strings_dropping_single_char(s):
    soln = set()
    for i in range(0, len(s)):
        sc = copy.copy(s)
        sc = [ x for x in sc ]
        sc.remove(sc[i])
        sc = ''.join(sc)
        soln.add(sc)
    return soln
    
def find_beautiful_strings(s):
    msoln = set()
    for i in range(0, len(s)):
        sol = find_list_of_strings_dropping_single_char(s[:i] + s[i+1:])
        for x in sol:
            msoln.add(x)
    return len(msoln)
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    s = raw_input(input_fp).split()[0]
    print find_beautiful_strings(s)


if __name__ == '__main__':
    main()
