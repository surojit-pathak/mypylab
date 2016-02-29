#!/bin/python
import sys

class LNode(object):
    def __init__(self, data=data, next=next, prev=prev):
        self.data = data
        self.next = next
        self.prev = prev

class TNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST(object):
    def __init__(self):
        self.root = None

    @staticmethod
    def _convert_bst_to_dll(n):
        if n is None:
            return (None, None)
        h1,t1 = BST._convert_bst_to_dll(n.left)
        h2,t2 = BST._convert_bst_to_dll(n.right)
        ln = LNode(data=n.data)
        if t1:
           t1.next = ln
        if h2:
           h2.prev = ln
        ln.next = h2
        ln.prev = t1
        if h1 is None:
            h1 = ln
        if t2 is None:
            t2 = ln
        return (h1, t2)

    def convert_bst_to_dll(self):
        h,t = BST._convert_bst_to_dll(self.root)
        return h

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin

if __name__ == '__main__':
    main()
