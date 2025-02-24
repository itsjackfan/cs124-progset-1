from random import random

class CompleteGraph:
    def __init__(self, n):
        self.n = n
        self.adj_list = {}
        for i in range(n):
            for j in range(n):
                if i != j and i < j:
                    self.adj_list[(i, j)] = random()

    def getAdjList(self):
        return self.adj_list