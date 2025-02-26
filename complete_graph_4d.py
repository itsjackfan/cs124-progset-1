from random import random

class CompleteGraph4D:
    def __init__(self, n):
        self.n = n
        self.adj_list = {}

        points = []
        for i in range(n):
            points.append((random(), random(), random(), random()))
        
        for i in range(n):
            for j in range(n):
                if i != j and i < j:
                    self.adj_list[(j, i)] = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2 + (points[i][2] - points[j][2])**2 + (points[i][3] - points[j][3])**2)**0.5
    
    def getAdjList(self):
        return self.adj_list