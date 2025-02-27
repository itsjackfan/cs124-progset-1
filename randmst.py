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
    
"""
class FibonaciNode:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.degree = 0
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0
    
    def create(self):
        self.min_node = None
        self.num_nodes = 0

    def insert(self, x):
        node = FibonaciNode(x)
        if self.min_node is None:
            self.min_node = node
        else:
            self._add_node_to_root_list(node, self.min_node)
            if node.key < self.min_node.key:
                self.min_node = node
        self.num_nodes += 1
        return node
    
    def find_min(self):
        return self.min_node
    
    def delete_min(self):
        x = self.min_node
        if x is not None:
            if x.child is not None:
                children=[]
                child = x.child
                while True:
                    children.append(child)
                    child=child.right
                    if child == x.child:
                        break
                for child in children:
                    self._add_node_to_root_list(child, x)
                    child.parent = None

            self._remove_node_from_root_list(x)
            if x == x.right:
                self.min_node = None
            else:
                self.min_node = x.right
                self._consolidate()
            self.num_nodes -= 1
        return x

    # Helper functions
    def _add_node_to_root_list(self, node, root):
        node.left = root
        node.right = root.right
        root.right.left = node
        root.right = node

    def _remove_node_from_root_list(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def _consolidate(self):
        A = [None] * self.num_nodes
        nodes = []

    """
        

class MinHeap:
    def __init__(self):
        self.heap = []
        self.in_heap = set()
        self.size = 0

    def build_heap(self, A):
        self.heap = A[:]
        self.size=len(self.heap)
        for i in range(self.size//2-1,-1,-1):
            self.min_heapify(i)

    def min_heapify(self, i):
        left = 2*i+1
        right = 2*i+2
        smallest=i

        if left<self.size and self.heap[left][0]<self.heap[smallest][0]:
            smallest=left
        if right < self.size and self.heap[right][0] < self.heap[smallest][0]:
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
        
        if self.size > 0:
            self.heap[0] = last
            self.min_heapify(0)
            
        self.in_heap.remove(min_node[0])
        return min_node

    def insert(self, v, weight):
        if v not in self.in_heap:
            self.size += 1
            self.heap.append((v, weight))
            self.in_heap.add(v)
            index = self.size - 1

            while index > 0 and self.heap[(index-1)//2][1] > self.heap[index][1]:
                self.swap(index, (index-1)//2)
                index = (index-1)//2
        else:
            pass

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def prim(vertices, edges):
    # Adjacency list construction
    adjacency_list = {v: [] for v in vertices}

    for (u, v), w in edges.items():
        adjacency_list[u].append((v, w))
        adjacency_list[v].append((u, w))

    # Initialize
    d = {v: float('inf') for v in vertices}
    prev = {v: None for v in vertices}

    S = set()
    H = MinHeap()

    # Start at s
    source = vertices[0]
    d[source] = 0
    prev[source] = None
    H.insert(source, 0)

    mst = []
    mst_weight = 0

    while H.size > 0:
        u, weight = H.extract_min()
        S.add(u)
        
        if prev[u] is not None:
            mst.append((prev[u], u, weight))
            mst_weight += weight

        for v, w in adjacency_list[u]:
            if v not in S and d[v] > w:
                d[v] = w
                prev[v] = u
                H.insert(v, d[v])

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

if dimension == 0:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        adj_list = CompleteGraph(numpoints).getAdjList()

        # run MST on graph
        MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)

        # calculate averages of weights
        kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)

    kruskal_avg = kruskal_weight_sum/numtrials
    print(kruskal_avg, numpoints, numtrials, dimension)
elif dimension == 1:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        adj_list = HCubeGraph(numpoints).getAdjList()

        # run MST on graph
        MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)

        # calculate averages of weights
        kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)

    kruskal_avg = kruskal_weight_sum/numtrials
    print(kruskal_avg, numpoints, numtrials, dimension)

elif dimension == 2:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        adj_list = CompleteGraph2D(numpoints).getAdjList()

        # run MST on graph
        MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)

        # calculate averages of weights
        kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)

    kruskal_avg = kruskal_weight_sum/numtrials
    print(kruskal_avg, numpoints, numtrials, dimension)
elif dimension == 3:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        adj_list = CompleteGraph3D(numpoints).getAdjList()

        # run MST on graph
        MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)

        # calculate averages of weights
        kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)
    
    kruskal_avg = kruskal_weight_sum/numtrials
    print(kruskal_avg, numpoints, numtrials, dimension)
elif dimension == 4:
    # create graph
    start_time = time.time()
    for _ in range(numtrials):
        adj_list = CompleteGraph4D(numpoints).getAdjList()

        # run MST on graph
        MST_kruskal, max_edge_weight = kruskal(numpoints, adj_list)

        # calculate averages of weights
        kruskal_weight_sum += sum(adj_list.get(edge, 0) for edge in MST_kruskal)
    
    kruskal_avg = kruskal_weight_sum/numtrials
    print(kruskal_avg, numpoints, numtrials, dimension)
else:
    pass