from random import random

class HCubeGraph:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[{i: random()} for i in range(n) if ((i-j) & (i-j-1)) == 0 and i-j > 0] for j in range(n)]
    
    def getAdjList(self):
        return self.adj_list