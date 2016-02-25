#!/bin/python
import sys

class BeautifulStringFinder(object):
    def __init__(self):
        self.memo = {}

    def find_beautiful_strings(self, s, k=2):
        if s in self.memo:
           return self.memo[s]
        soln = set()
        for i in range(0, len(s)):
            if k == 1:
               soln.add(s[:i] + s[i+1:])
            else: 
               soln = soln.union(self.find_beautiful_strings(s[:i] + s[i+1:], k - 1))
        self.memo[s] = soln
        return soln
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    s = raw_input(input_fp).split()[0]
    fbs = BeautifulStringFinder()
    print len(fbs.find_beautiful_strings(s))


if __name__ == '__main__':
    main()
