#!/bin/python
import sys

def find_if_possible_to_buy(items, n, k):
    pchart = [ False for x in range(0, k+1) ]
    pchart[0] = True
    for i in range(0,n):
        v = items[i]
        if v <= k:
           pchart[v] = True
    if pchart[k]:
        return True

    for l in range(1,k+1):
        result = False
        for i in items:
            if l >= i and pchart[l - i]:
                result = True
                break
        pchart[l] = result
    return pchart[k]
      
def find_if_possible_to_buy_memo(items, n, k, memo=None):
    if memo is None:
        memo = {}
        memo[0] = True
        for i in items:
            memo[i] = True
    if k in memo:
        return memo[k] 
    
    if n == 0:
       return False
    if items[n-1] == k:
       memo[k] = True
       return True
    if items[n-1] > k:
       return find_if_possible_to_buy(items, n-1, k)
    return (find_if_possible_to_buy(items, n, k - items[n-1]) or find_if_possible_to_buy(items, n-1, k))

def find_if_possible_to_buy_recursion(items, n, k):
    if k == 0: 
       return True
    if n == 0:
       return False
    if items[n-1] == k:
       return True
    if items[n-1] > k:
       return find_if_possible_to_buy(items, n-1, k)
    return (find_if_possible_to_buy(items, n, k - items[n-1]) or find_if_possible_to_buy(items, n-1, k))

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n,k = map(lambda x: int(x), raw_input(input_fp).split())
    items = map(lambda x: int(x), raw_input(input_fp).split())

    print find_if_possible_to_buy(items, n, k)

if __name__ == '__main__':
    main()
