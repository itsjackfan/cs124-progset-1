import sys
from complete_graph import CompleteGraph
from hypercube_graph import HCubeGraph
from complete_graph_2d import CompleteGraph2D
from complete_graph_3d import CompleteGraph3D
from complete_graph_4d import CompleteGraph4D
import time

numpoints = int(sys.argv[2])
numtrials = int(sys.argv[3])
dimension = int(sys.argv[4])

class TreeNode:
    def __init__(self, x):
        self.x = x
        self.parent = self
        self.rank = 0

class UnionFind:
    def __init__(self): # makeset
        self.nodes = {}

    def makeset(self, x):
        self.nodes[x] = TreeNode(x)

    def union(self, x, y):
        return self.link(self.find(x), self.find(y))

    def find(self, x):
        if self.nodes[x] != self.nodes[x].parent:
            self.nodes[x].parent = self.find(self.nodes[x].parent.x)
        return self.nodes[x].parent
     
    def link(self, x, y):
        if x.rank > y.rank:
            return self.link(y, x)
        else:
            y.rank += 1
        x.parent = y
        return y

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
        self.in_set = set()

    def min_heapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        smallest = i

        if left < self.size and self.heap[left][1] < self.heap[smallest][1]:
            smallest = left
        if right < self.size and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def extract_min(self):
        if self.size == 0:
            return None
        
        min_node = self.heap[0]
        last = self.heap.pop()
        self.size -= 1
        self.in_set.remove(min_node[0])
        
        if self.size > 0:
            self.heap[0] = last
            self.min_heapify(0)
            
        return min_node

    def insert(self, v, weight):
        if v in self.in_set:
            for i in range(self.size):
                if self.heap[i][0] == v and self.heap[i][1] > weight:
                    self.heap[i] = (v, weight)
                    self.heapify_up(i)
                    return
        else:
            self.heap.append((v, weight))
            self.size += 1
            self.in_set.add(v)
            self.heapify_up(self.size - 1)

    def heapify_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[parent][1] > self.heap[i][1]:
            self.swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]



def prim(vertices, edges):
   #""""""
    #vertices: list of the vertices (not just the total number of vertices)
    #edges: adjacency list in form of dictionary {u: [(v_1,w_1), (v_2,w_2),...],...}
    #"""

    # Initialize
    num_points=len(vertices)
    d = {v: float('inf') for v in vertices}
    prev = {v: None for v in vertices}

    S = set()
    H = MinHeap()

    # Start at source
    source = vertices[0]
    d[source] = 0
    prev[source] = None
    H.insert(source, 0)

    mst = []
    mst_weight = 0

    while H.size > 0:
        u, weight = H.extract_min()
        if u in S:
            continue

        S.add(u)

        if prev[u] is not None:
            mst.append((prev[u], u))
            mst_weight += weight

        for (v,w) in edges[u]:
            if v not in S and d[v] > w:
                d[v] = w
                prev[v] = u
                H.insert(v, w)

    return mst, mst_weight


def kruskal(v, e):
    uf = UnionFind()
    sorted_edges = dict(sorted(e.items(), key = lambda x:x[1]))

    X = {}

    for i in range(v):
        uf.makeset(i)
    
    for edge in sorted_edges:
        if uf.find(edge[0]) != uf.find(edge[1]):
            X[edge] = e[edge]
            uf.union(edge[0], edge[1])

    return X, max(X.values())

kruskal_weight_sum = 0
prim_weight_sum = 0

#numtrials=60


if dimension == 0:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        #adj_list = Complete(numpoints).getAdjList()
        graph = CompleteGraph(numpoints)
        adj_list = graph.getAdjList()
        vertices = graph.getVertices()

        # run MST on graph
        #print("Adj_list: ", adj_list)
        #print("Vertices: ", vertices)
        #MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)
        MST_prim, prim_weight = prim(vertices, adj_list)
        
        #print("Kruskal:", MST_kruskal)
        #print("Prim:", MST_prim)

        # calculate averages of weights
        #kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)
        prim_weight_sum += prim_weight

    #kruskal_avg = kruskal_weight_sum / numtrials
    prim_avg = prim_weight_sum / numtrials
    #print(kruskal_avg, numpoints, numtrials, dimension)
    print(prim_avg, numpoints, numtrials, dimension)

elif dimension == 1:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        #adj_list = HCubeGraph(numpoints).getAdjList()
        graph = HCubeGraph(numpoints)
        adj_list = graph.getAdjList()
        vertices = graph.getVertices()

        # run MST on graph
        #print("Adj_list: ", adj_list)
        #print("Vertices: ", vertices)
        #MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)
        MST_prim, prim_weight = prim(vertices, adj_list)
        
        #print("Kruskal:", MST_kruskal)
        #print("Prim:", MST_prim)

        # calculate averages of weights
        #kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)
        prim_weight_sum += prim_weight

    #kruskal_avg = kruskal_weight_sum / numtrials
    prim_avg = prim_weight_sum / numtrials
    #print(kruskal_avg, numpoints, numtrials, dimension)
    print(prim_avg, numpoints, numtrials, dimension)

elif dimension == 2:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        #adj_list = CompleteGraph2D(numpoints).getAdjList()
        graph = CompleteGraph2D(numpoints)
        adj_list = graph.getAdjList()
        vertices = graph.getVertices()

        # run MST on graph
        #print("Adj_list: ", adj_list)
        #print("Vertices: ", vertices)
        #MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)
        MST_prim, prim_weight = prim(vertices, adj_list)
        
        #print("Kruskal:", MST_kruskal)
        #print("Prim:", MST_prim)

        # calculate averages of weights
        #kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)
        prim_weight_sum += prim_weight

    #kruskal_avg = kruskal_weight_sum / numtrials
    prim_avg = prim_weight_sum / numtrials
    #print(kruskal_avg, numpoints, numtrials, dimension)
    print(prim_avg, numpoints, numtrials, dimension)

elif dimension == 3:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        #adj_list = CompleteGraph3D(numpoints).getAdjList()
        graph = CompleteGraph3D(numpoints)
        adj_list = graph.getAdjList()
        vertices = graph.getVertices()

       # run MST on graph
        #print("Adj_list: ", adj_list)
        #print("Vertices: ", vertices)
        #MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)
        MST_prim, prim_weight = prim(vertices, adj_list)
        
        #print("Kruskal:", MST_kruskal)
        #print("Prim:", MST_prim)

        # calculate averages of weights
        #kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)
        prim_weight_sum += prim_weight

    #kruskal_avg = kruskal_weight_sum / numtrials
    prim_avg = prim_weight_sum / numtrials
    #print(kruskal_avg, numpoints, numtrials, dimension)
    print(prim_avg, numpoints, numtrials, dimension)

elif dimension == 4:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        #adj_list = CompleteGraph4D(numpoints).getAdjList()
        graph = CompleteGraph4D(numpoints)
        adj_list = graph.getAdjList()
        vertices = graph.getVertices()

        # run MST on graph
        #print("Adj_list: ", adj_list)
        #print("Vertices: ", vertices)
        #MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)
        MST_prim, prim_weight = prim(vertices, adj_list)
        
        #print("Kruskal:", MST_kruskal)
        #print("Prim:", MST_prim)

        # calculate averages of weights
        #kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)
        prim_weight_sum += prim_weight

    #kruskal_avg = kruskal_weight_sum / numtrials
    prim_avg = prim_weight_sum / numtrials
    #print(kruskal_avg, numpoints, numtrials, dimension)
    print(prim_avg, numpoints, numtrials, dimension)

else:
    pass
