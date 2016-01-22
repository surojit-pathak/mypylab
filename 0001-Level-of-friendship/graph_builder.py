import sys
import sets
import Queue

class graph(object):
    nodes = sets.Set()
    edges = {}
    def _add_edge(self, v1, v2):
        if v1 in self.edges:
            self.edges[v1].add(v2)
        else:
            self.edges[v1] = sets.Set(v2)

    def process_edge(self, v1, v2):
        self.nodes.add(v1)
        self.nodes.add(v2)

        self._add_edge(v1, v2)
        self._add_edge(v2, v1)

    def walk_graph_by_level(self, start, tfunc):
        visited = {}
        for x in self.nodes:
            visited[x] = False
      
        process_q = Queue.Queue(maxsize=len(self.nodes))
        process_q.put((start, 0))
        visited[start] = True
        while not process_q.empty():
            node, dist = process_q.get()
            for adj in self.edges[node]:
                if visited[adj] == False:
                    process_q.put((adj, dist + 1))
                    visited[adj] = True
            tfunc(node, dist)
        
def build_graph():
    fp = open(sys.argv[1], 'r')
    G = graph()
    for line in fp.readlines():
        line = line.rstrip('\n')
        info = line.split(':')
        v1 = info[0]
        for v in info[1].lstrip().split(','):
            G.process_edge(v1, v)
    return G

if __name__ == '__main__':
    graph = build_graph()
    start = raw_input('Enter the node in question: ')
    last_visited_depth = 0

    def traversal_func(node, dist):
        global last_visited_depth
        if dist == 0: 
           return
        if last_visited_depth != dist:
           print "\nLevel %s - %s" %(dist, node),
        else:
           print ", %s" %node,
        last_visited_depth = dist
        

    if start in graph.nodes:
        last_visited_depth = 0
        graph.walk_graph_by_level(start, traversal_func)
        print "\n"
    #print graph.nodes
    #print graph.edges
