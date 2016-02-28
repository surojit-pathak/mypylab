#!/bin/python
import sys

import Queue
import string
import time

debug = False
def debug_print(*args, **kwargs):
    if debug:
        print(args, kwargs)
    
class MyGraph(object):
    def __init__(self):
        self.vertices = set()
        self.edges = {}
   
    def add_vertex(self, data):
        self.vertices.add(data);
        if data not in self.edges:
            self.edges[data] = set()

    def add_edge(self, v1, v2):
        self.edges[v1].add(v2)
        self.edges[v2].add(v1)

class WordDictionary(object):
    def __init__(self):
        start = time.time()
        self.wg = MyGraph()
        dp = open('/usr/share/dict/words', 'r')
        for w in dp.readlines():
            w = w.rstrip('\n').strip().lower()
            self.wg.add_vertex(w)
        dp.close()
        end = time.time()
        debug_print('All vertices are added to the dictionary in {}'.format(end-start))
        start = time.time()
        alphabet = string.lowercase
        for w in self.wg.vertices:
            n = len(w)
            for i in xrange(0, n):
                c = w[i]
                for a in alphabet:
                    if a != c:
                        rs = w[:i] + a + w[i+1:]
                        if rs in self.wg.vertices:
                            self.wg.add_edge(w, rs)
        end = time.time()
        debug_print('All edges are added to the dictionary in {}'.format(end-start))
 
    def find_path(self, ws, we):
        if len(ws) != len(we):
            print 'This algorithm works for same length string'
            return
        if ws not in self.wg.vertices or we not in self.wg.vertices:
            print 'This algorithm works for words in dictionary'
            return
        visited = []
        q = Queue.Queue()
        q.put((ws, None))
        while q.empty() is False:
            n, path = q.get()
            if n == we:
               print path + we
               return
            if path is None: 
               path = n + '->'
            else:
               path = path + n + '->'

            for adj in self.wg.edges[n]:
                if adj not in visited:
                    q.put((adj, path))
            visited.append(n)
        print "There is no valid transition"

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    WD = WordDictionary()
    while True:
	s, e = raw_input(input_fp).split()
	start = time.time()
	WD.find_path(s,e)
	end = time.time()
	debug_print('Find took {}'.format(end-start))
    

if __name__ == '__main__':
    main()
