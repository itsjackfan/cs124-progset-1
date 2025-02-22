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

class UnionFind:
    def __init__(self):
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