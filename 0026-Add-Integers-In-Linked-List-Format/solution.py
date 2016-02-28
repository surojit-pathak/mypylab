#!/bin/python
import copy
import sys

class LLInt(object):
    class LLNode(object):
        def __init__(self, data=0, next=None):
            self.data = data
            self.next = next

    def __init__(self, num):
        if num == 0:
            self.start = LLInt.LLNode()
            return
        
        prev = None
        while num > 0:
            r = num % 10 
            n = LLInt.LLNode(data=r, next=prev)
            self.start = prev = n
            num = num / 10

    def _get_numbers_in_stack(self):
        nl = []
        n = self.start
        while n:
            nl.append(n.data)
            n = n.next
        return nl

    @staticmethod
    def add(m, n):
        ml = m._get_numbers_in_stack()
        nl = n._get_numbers_in_stack()
        p = LLInt(0)
        p.start.data = ml.pop() + nl.pop()
        c = p.start.data / 10
        p.start.data = p.start.data % 10
        prev = p.start
        while len(ml) or len(nl):
            if len(ml):
                c = c + ml.pop()
            if len(nl):
                c = c + nl.pop()
            n = LLInt.LLNode(data=c%10, next=prev)
            p.start = prev = n
            c = c /10
        if c:
            p.start = LLInt.LLNode(data=c, next=prev)
        return p

    def display(self):
        n = self.start
        while n != None:
            print str(n.data) + ' -> ',
            n = n.next
        print

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    m, n = map(lambda x: int(x), raw_input(input_fp).split())
    #print m, n
    m = LLInt(m)
    n = LLInt(n)
    m.display()
    n.display()
    p = LLInt.add(m,n)
    p.display()


if __name__ == '__main__':
    main()
