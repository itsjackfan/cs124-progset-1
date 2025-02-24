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
        return self.link(self.find(self.nodes[x]), self.find(self.nodes[y]))

    def find(self, x):
        if self.nodes[x] != self.nodes[x].parent:
            self.nodes[x].parent = self.find(self.nodes[x].parent.x)
        return self.nodes[x].parent
     
    def link(self, x, y):
        if self.nodes[x].rank > self.nodes[y].rank:
            return self.link(self.nodes[y], self.nodes[x])
        else:
            self.nodes[y].rank += 1
        self.nodes[x].parent = self.nodes[y]
        return self.nodes[y]

def kruskal(g):
    pass

if dimension == 0:
    # create graph
    adj_list = CompleteGraph(numpoints).getAdjList()

    # run MST on graph

    # calculate averages of weights

elif dimension == 1:
    # create graph
    start_time = time.time()
    adj_list = HCubeGraph(numpoints).getAdjList()
    print(time.time() - start_time)
    
    # run MST on graph

    # calculate averages of weights
elif dimension == 2:
    # create graph
    graph = CompleteGraph2D(numpoints)
    
    # run MST on graph

    # calculate averages of weights
elif dimension == 3:
    # create graph
    graph = CompleteGraph3D(numpoints)
    
    # run MST on graph

    # calculate averages of weights
elif dimension == 4:
    # create graph
    graph = CompleteGraph4D(numpoints)
    
    # run MST on graph

    # calculate averages of weights
else:
    pass