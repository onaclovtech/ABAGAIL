from src.opt.example.TravelingSalesmanEvaluationFunction import *
from src.shared.Instance import *
#/**
#* An implementation of the traveling salesman problem
#* where the encoding used is a permutation of [0, ..., n]
#* where there are n+1 cities.  That is the encoding
#* is just the path to take.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class TravelingSalesmanRouteEvaluationFunction (TravelingSalesmanEvaluationFunction):

#/**
#* Make a new route evaluation function
#* @param points the points of the cities
#*/
     def __init__(self,points):
        TravelingSalesmanEvaluationFunction.__init__(self, points)

#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     def value(self, d):
        if not isinstance(d, Instance):
            raise TypeError("Expected Instance got " + str(d.__class__))
        self.distance = 0
        for i in range(d.size() - 1): # Is -1 the right result?
            self.distance += self.getDistance(d.getDiscrete(i), d.getDiscrete(i+1))
        self.distance += self.getDistance(d.getDiscrete(d.size() - 1), d.getDiscrete(0))
        return 1/self.distance
