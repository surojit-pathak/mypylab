#!/bin/python
import sets
import copy
import sys

class Graph(object):
    def __init__(self):
        self.vertices = sets.Set()
        self.edges = []
    def add_vertex(self, v):
        self.vertices.add(v)
    def add_edge(self, u, v, c):
        self.add_vertex(u)
        self.add_vertex(v)
        self.edges.append((c, (u, v)))
    def compare_edges(self, a, b):
        c1, (u1,v1) = a
        c2, (u2,v2) = b
        if c1 < c2:
           return -1
        if c1 > c2:
           return 1
        return 0

    def sort_edges_by_cost(self):
        self.edges = sorted(self.edges, cmp=self.compare_edges)

    # Prim's method
    def find_minimum_spanning_tree(self, n):
        self.sort_edges_by_cost()
        E = copy.copy(self.edges)
        g = Graph()
        e = E[0]
        c, (u, v) = e
        g.add_edge(u, v, c)
        E.remove(e)
          
        while len(g.edges) != len(self.vertices) - 1:
            for e in E:
                c, (u, v) = e
                if u in g.vertices and v in g.vertices:
                   continue
                if u in g.vertices or v in g.vertices:
                   g.add_edge(u, v, c)
                   E.remove(e)
                   break
 
        return g
        
    def find_cost(self):
        cost = 0
        for e in self.edges:
            c, (u, v) = e
            cost = cost + c
        return cost
    
    def find_minimum_weight_subgraph(self):
        mst = []
        for v in self.vertices:
            g = self.find_minimum_spanning_tree(v)
            c = g.find_cost()
            mst.append((c,g))
        c,g = sorted(mst)[0]
        print c
        print g
        return c
 
    def display(self):
        print self.vertices
        print self.edges

def raw_input(input_fp):
    return input_fp.readline().rstrip('\n').strip()

def main(input_fp=None):
    if input_fp is None:
       input_fp = sys.stdin
    
    n, m = map(lambda x: int(x), raw_input(input_fp).split())
    G = Graph()
    for i in xrange(0, m):
        u,v,c = map(lambda x: int(x), raw_input(input_fp).split())
        G.add_edge(u, v, c)
    #G.display()
    u = map(lambda x: int(x), raw_input(input_fp).split())
    g = G.find_minimum_spanning_tree(u[0])
    #g.display()
    c = g.find_cost()
    print c
    return c

if __name__ == '__main__':
    main()
