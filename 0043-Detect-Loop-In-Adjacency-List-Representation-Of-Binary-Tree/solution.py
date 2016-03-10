#!/bin/python
import sys

def detect_loop(adj):
    vertices = set()
    for x in adj:
        u,v = x
        vertices.add(u)
        if v in vertices:
            return True 
        vertices.add(v)
    
def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    n = map(lambda x: int(x), raw_input(input_fp).split())[0]
    adj = []
    for i in range(0, n):
       u,v = raw_input(input_fp).split(',')
       adj.append((u,v))

    if detect_loop(adj):
        print 'Loop Detected'
    else:
        print 'No Loop!'

if __name__ == '__main__':
    main()
