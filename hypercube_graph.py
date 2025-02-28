from random import random

class HCubeGraph:
    def __init__(self, n):
        self.n = n
        self.adj_list = { i: [] for i in range(n) }
        self.vertices = list(range(n))

        for i in range(n):
            self.vertices.append(i)
            for j in range(n):
                if (i-j) & (i-j-1) == 0 and i-j > 0:
                    value = random()

                    if value < 0.7:
                        self.adj_list[i].append((j, value))
                        self.adj_list[j].append((i, value))
    
    def getAdjList(self):
        return self.adj_list
    
    def getVertices(self):
        return self.vertices