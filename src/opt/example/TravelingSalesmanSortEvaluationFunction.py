from src.opt.example.TravelingSalesmanEvaluationFunction import *


#/**
#* A traveling salesman evaluation function that works with
#* routes that are encoded as sorts.  That is the route
#* is the permutaiton of indices found by sorting the data.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class TravelingSalesmanSortEvaluationFunction (TravelingSalesmanEvaluationFunction):


#/**
#* Make a new traveling salesman evaluation function
#* @param points the points at which the cities are located
#*/
     def __init__(self, points):
        TravelingSalesmanEvaluationFunction.__init__(self,points)
    

#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     def value(d):
        ddata = [None] * d.size()
        for i in range(len(ddata)):
            ddata[i] = d.getContinuous(i)

        order = ABAGAILArrays.indices(d.size())
        ABAGAILArrays.quicksort(ddata, order)
        distance = 0.0
        for i in range(len(order) - 1):
            distance += getDistance(order[i], order[i+1])
        
        distance += getDistance(order[order.length - 1], order[0])
        return 1/distance

