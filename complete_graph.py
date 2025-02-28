from random import random

class CompleteGraph:
    def __init__(self, n):
        self.n = n
        self.adj_list = { i: [] for i in range(n) }
        self.vertices = list(range(n))

        for i in range(n):
            self.vertices.append(i)
            for j in range(i+1, n):
                edge_val = random()
            
                if edge_val < 20/n:
                    self.adj_list[i].append((j, random()))
                    self.adj_list[j].append((i, random()))

    def getAdjList(self):
        return self.adj_list
    
    def getVertices(self):
        return self.vertices