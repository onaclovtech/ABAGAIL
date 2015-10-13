import math
#/**
#* An evaluation function for the traveling salesman problem
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class TravelingSalesmanEvaluationFunction:
#/**
#* The distance between city i and j
#*/
    #double[][] distances
#/**
#* Make a new traveling salesman  evaluation function
#* @param points the points at which the cities are located
#*/
     def __init__(self, points):
        self.distances = [None] * len(points)
        for i in range(len(points)):
            self.distances[i] = [None] * i
            for j in range(i):
                a = points[i]
                b = points[j]
                self.distances[i][j] = math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))
    
#/**
#* Get the distance between two points
#* @param i the first point
#* @param j the second
#* @return the distance
#*/
     def getDistance(self, i, j):
        if (i==j):
            return 0
        else:
            a = max(i,j)
            b = min(i,j)
            return self.distances[a][b]
        