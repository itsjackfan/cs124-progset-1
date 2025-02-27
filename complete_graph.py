from random import random

class CompleteGraph:
    def __init__(self, n):
        self.n = n
        self.adj_list = {}

        for i in range(n):
            for j in range(i+1, n):
                edge_val = random()
            
                if edge_val < 20/n:
                    self.adj_list[(i, j)] = random()

    def getAdjList(self):
        return self.adj_list