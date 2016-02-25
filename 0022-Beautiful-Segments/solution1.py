#!/bin/python
import sys

bs_cache = {}
def print_number_of_beautiful_segments(A, L, R, X, memo):
    if (L, R, X) in bs_cache:
        print bs_cache[(L, R, X)]
        return
    count = 0
    for i in xrange(L, R+1):
        for j in xrange(i, R+1):
            if memo[i][j] == -1:
                prod = A[i]
                for k in xrange(i+1, j+1):
                    prod = prod & A[k]
                    if prod == 0:
                       break
                memo[i][j] = prod
            else:
                prod = memo[i][j]
            if prod <= X:
                count = count + 1
    print count
    bs_cache[(L, R, X)] = count
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin

    n, q = map(lambda x: int(x), raw_input(input_fp).split())
    memo = [ [ -1 for j in range(0, n) ] for i in range(0, n) ]
    A = map(lambda x: int(x), raw_input(input_fp).split())
    for i in xrange(0, q):
        L, R, X = map(lambda x: int(x), raw_input(input_fp).split())
        print_number_of_beautiful_segments(A, L - 1, R - 1, X, memo)

if __name__ == '__main__':
    main()
