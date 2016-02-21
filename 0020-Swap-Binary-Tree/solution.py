#!/bin/python
import sys

sys.setrecursionlimit(15000)

def inorder_traversal(nodes, i):
    l, r = nodes[i]
    if l != -1:
       inorder_traversal(nodes, l)
    #print str(i) + ' ',
    print str(i),
    if r != -1:
       inorder_traversal(nodes, r)

def swap(nodes, i):
    l,r = nodes[i]
    nodes[i] = (r, l)

def swap_at_level(nodes, i, k, h):
    if k == h:
       swap(nodes, i)
       return
    l, r = nodes[i]
    if l != -1:
       swap_at_level(nodes, l, k, h+1)
    if r != -1:
       swap_at_level(nodes, r, k, h+1)
    

def max(a, b):
    if (a > b):
        return a
    else:
        return b

def depth_of_tree(nodes, i):
    l, r = nodes[i]
    h1 = h2 = 0
    if l != -1:
       h1 = depth_of_tree(nodes, l)
    if r != -1:
       h2 = depth_of_tree(nodes, r)
    return max(h1, h2) + 1
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    nodes = [(-1, -1) for x in range(0, n+1)]
    for i in xrange(1, n+1):
        l, r = map(lambda x: int(x), raw_input(input_fp).split())
        nodes[i] = (l, r)
    h = depth_of_tree(nodes, 1)
    t = map(lambda x: int(x), raw_input(input_fp).split())[0]
    for i in xrange(0, t):
        k = map(lambda x: int(x), raw_input(input_fp).split())[0]
        while k < h:
            swap_at_level(nodes, 1, k, 1)
            k = k + k
 
        inorder_traversal(nodes, 1)
        print
     


if __name__ == '__main__':
    main()
