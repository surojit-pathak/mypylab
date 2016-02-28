#!/bin/python
import sys

def test_palindrome(s, i, j):
    if i > j:
        return False
    while i < j:
        if s[i] == s[j]:
           i = i + 1
           j = j - 1
        else:
           return False
    return True
       
def find_longest_palindromic_substring(s):
    max_len = 1
    max_s = max_e = 0
    n = len(s)
    for i in xrange(0, n):
        for j in xrange(n-1, i, -1):
            if j - i + 1 > max_len:
                if test_palindrome(s, i, j):
                     max_len = j - i + 1
                     max_s = i
                     max_e = j
                     break
            else:
                break
    if max_len:
        print s[max_s:max_e+1]
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    s = raw_input(input_fp)
    find_longest_palindromic_substring(s)

if __name__ == '__main__':
    main()
