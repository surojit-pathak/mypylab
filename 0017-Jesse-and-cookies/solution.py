#!/bin/python
import sys
import Queue

def find_sweet_cookie_for_jesse(cookies, k):
    success = -1
    steps = 0
    pq = Queue.PriorityQueue()
    for x in cookies:
        pq.put(x)
    
    while pq.empty() is False:
        a = pq.get()
        if a >= k:
           success = steps
           break
        if pq.empty(): 
           break
        b = pq.get()
        if b >= k:
           success = steps
           break
        steps = steps + 1
        c = a + (2 * b)
        if c >= k:
           success = steps
           break
        pq.put(c)
    print success

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    
    n, k = map(lambda x: int(x), raw_input(input_fp).split())
    cookies = map(lambda x: int(x), raw_input(input_fp).split()) 
    find_sweet_cookie_for_jesse(cookies, k)

if __name__ == '__main__':
    main()
