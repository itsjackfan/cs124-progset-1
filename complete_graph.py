from random import random
import numpy as np

class CompleteGraph:
    def __init__(self, n):
        self.n = n
        n_vals = np.random.randint(0, 1, n)
        self.adj_list = [[{i: n_vals[i+j]} for i in range(n) if i != j and i > j] for j in range(n)]
    
    def getAdjList(self):
        return self.adj_list