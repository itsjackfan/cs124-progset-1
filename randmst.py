import sys
from complete_graph import CompleteGraph
from hypercube_graph import HCubeGraph
from complete_graph_2d import CompleteGraph2D
from complete_graph_3d import CompleteGraph3D
from complete_graph_4d import CompleteGraph4D

numpoints = sys.argv[2]
numtrials = sys.argv[3]
dimension = sys.argv[4]

if numtrials == 0:
    # create graph
    graph = CompleteGraph()
    
    # run MST on graph

    # calculate averages of weights

elif numtrials == 1:
    # create graph
    graph = HCubeGraph()
    
    # run MST on graph

    # calculate averages of weights
elif numtrials == 2:
    # create graph
    graph = CompleteGraph2D()
    
    # run MST on graph

    # calculate averages of weights
elif numtrials == 3:
    # create graph
    graph = CompleteGraph3D()
    
    # run MST on graph

    # calculate averages of weights
elif numtrials == 4:
    # create graph
    graph = CompleteGraph4D()
    
    # run MST on graph

    # calculate averages of weights
else:
    pass
