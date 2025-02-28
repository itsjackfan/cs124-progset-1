from random import random

class HCubeGraph:
    def __init__(self, n):
        self.n = n
        self.adj_list = {}


        for i in range(n):
            for j in range(n):
                if (i-j) & (i-j-1) == 0 and i-j > 0:
                    value = random()

                    if value < 0.07 * n + 2.5:
                        self.adj_list[(j, i)] = value
    
    def getAdjList(self):
        return self.adj_list