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

def kruskal(v, e):
    uf = UnionFind()
    sorted_edges = dict(sorted(e.items(), key = lambda x:x[1]))

    X = []

    for i in range(v):
        uf.makeset(i)
    
    for edge in sorted_edges:
        if uf.find(edge[0]) != uf.find(edge[1]):
            X.append(edge)
            uf.union(edge[0], edge[1])
    
    return X

weight_sum = 0

if dimension == 0:
    # create graph
    for _ in range(numtrials):
        adj_list = CompleteGraph(numpoints).getAdjList()
        print(adj_list)

        # run MST on graph
        MST = kruskal(numpoints, adj_list)

        # calculate averages of weights -- currently a placeholder for sum cuz we probably want to run multiple trials
        weight_sum += sum(adj_list.get(edge, 0) for edge in MST)
    
    avg = weight_sum/numtrials
    print("AVERAGE WEIGHT: ", avg)

elif dimension == 1:
    for _ in range(numtrials):
        # create graph
        adj_list = HCubeGraph(numpoints).getAdjList()
        print(adj_list)
        
        # run MST on graph
        MST = kruskal(numpoints, adj_list)

        # calculate averages of weights -- currently a placeholder for sum cuz we probably want to run multiple trials
        weight_sum += sum(adj_list.get(edge, 0) for edge in MST)

    avg = weight_sum/numtrials
    print("AVERAGE WEIGHT: ", avg)

elif dimension == 2:
    for i in range(numtrials):
        # create graph
        adj_list = CompleteGraph(numpoints).getAdjList()
        print(adj_list)
        
        # run MST on graph
        MST = kruskal(numpoints, adj_list)

        # calculate averages of weights -- currently a placeholder for sum cuz we probably want to run multiple trials
        weight_sum += sum(adj_list.get(edge, 0) for edge in MST)

    avg = weight_sum/numtrials
    print("AVERAGE WEIGHT: ", avg)

elif dimension == 3:
    for i in range(numtrials):
        # create graph
        adj_list = CompleteGraph(numpoints).getAdjList()
        print(adj_list)
        
        # run MST on graph
        MST = kruskal(numpoints, adj_list)

        # calculate averages of weights -- currently a placeholder for sum cuz we probably want to run multiple trials
        weight_sum += sum(adj_list.get(edge, 0) for edge in MST)

    avg = weight_sum/numtrials
    print("AVERAGE WEIGHT: ", avg)
elif dimension == 4:
    for i in range(numtrials):
        # create graph
        adj_list = CompleteGraph(numpoints).getAdjList()
        print(adj_list)
        
        # run MST on graph
        MST = kruskal(numpoints, adj_list)

        # calculate averages of weights -- currently a placeholder for sum cuz we probably want to run multiple trials
        weight_sum += sum(adj_list.get(edge, 0) for edge in MST)
    
    avg = weight_sum/numtrials
    print("AVERAGE WEIGHT: ", avg)
else:
    pass