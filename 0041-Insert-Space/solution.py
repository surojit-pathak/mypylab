#!/bin/python
import sys

class MyDictionary():
    def __init__(self, dfile='/usr/share/dict/words'): 
        self.wordbook = {}
        dp = open(dfile, 'r')
        for w in dp.readlines():
            w = w.rstrip('\n').strip().lower()
            if len(w) > 1:
                self.wordbook[w] = 1
        dp.close()

    def contains(self, w):
        return w in self.wordbook

def insert_space(input, n, d):
    n = len(input)
    if n == 0:
       return ''
    for i in range(0, n):
        if d.contains(input[0:i+1]):
           r = insert_space(input[i+1:n+1], n - i + 1, d)
           if r is not None:
               return input[0:i+1] + ' ' + r
    return None

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    dfile = raw_input(input_fp)
    d = MyDictionary(dfile)
    input = raw_input(input_fp)
    print insert_space(input, len(input), d)
      

if __name__ == '__main__':
    main()
