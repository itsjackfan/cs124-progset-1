from random import random

class CompleteGraph4D:
    def __init__(self, n):
        self.n = n
        self.adj_list = { i: [] for i in range(n) }
        self.vertices = list(range(n))

        points = []
        for i in range(n):
            self.vertices.append(i)
            points.append((random(), random(), random(), random()))
        
        for i in range(n):
            x_i,y_i,z_i,a_i = points[i]
            for j in range(n):
                x_j,y_j,z_j,a_j = points[j]
                if i != j and i < j:
                    dist = ((x_i - x_j)**2 + (y_i - y_j)**2 + (z_i - z_j)**2 + (a_i - a_j)**2)**0.5

                    if dist < 0.6:
                        self.adj_list[i].append((j, dist))
                        self.adj_list[j].append((i, dist))
    
    def getAdjList(self):
        return self.adj_list
    
    def getVertices(self):
        return self.vertices