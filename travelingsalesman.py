# traveling salesman algorithm implementation in jython
# This also prints the index of the points of the shortest route.
# To make a plot of the route, write the points at these indexes 
# to a file and plot them in your favorite tool.
import random
from array import array
from src.dist.DiscreteDependencyTree import *
from src.dist.DiscreteUniformDistribution import *
from src.dist.DiscretePermutationDistribution import *
from src.opt.GenericHillClimbingProblem import *
from src.opt.RandomizedHillClimbing import *
from src.opt.SimulatedAnnealing import *
from src.opt.ga.GenericGeneticAlgorithmProblem import *
from src.opt.ga.StandardGeneticAlgorithm import *
from src.opt.prob.GenericProbabilisticOptimizationProblem import *
from src.opt.prob.MIMIC import *
from src.shared.FixedIterationTrainer import *
from src.opt.example.TravelingSalesmanRouteEvaluationFunction import *
from src.opt.SwapNeighbor import *
from src.opt.ga.SwapMutation import *
from src.opt.example.TravelingSalesmanCrossOver import *
from src.opt.example.TravelingSalesmanSortEvaluationFunction import *
from src.util.ABAGAILArrays import *

#Candidates for removal.
#import sys
#import os
#import time
#from src.dist.Distribution import *
# from src.opt.DiscreteChangeOneNeighbor import *
# from src.opt.EvaluationFunction import *
# from src.opt.HillClimbingProblem import *
# from src.opt.NeighborFunction import *
# from src.opt.example.FourPeaksEvaluationFunction import *
# from src.opt.ga.CrossoverFunction import *
# from src.opt.ga.SingleCrossOver import *
# from src.opt.ga.DiscreteChangeOneMutation import *
# from src.opt.ga.GeneticAlgorithmProblem import *
# from src.opt.ga.MutationFunction import *
# from src.opt.ga.UniformCrossOver import *
# from src.opt.prob.ProbabilisticOptimizationProblem import *
# from src.opt.example.TravelingSalesmanEvaluationFunction import *
# from src.shared.Instance import *

"""
Commandline parameter(s):
    none
"""

# set N value.  This is the number of points
N = 50

points = [[0 for x in xrange(2)] for x in xrange(N)]
for i in range(0, len(points)):
    points[i][0] = random.random()
    points[i][1] = random.random()

ef = TravelingSalesmanRouteEvaluationFunction(points)
odd = DiscretePermutationDistribution(N)
nf = SwapNeighbor()
mf = SwapMutation()
cf = TravelingSalesmanCrossOver(ef)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)

rhc = RandomizedHillClimbing(hcp)
fit = FixedIterationTrainer(rhc, 200000)
fit.train()
print "RHC Inverse of Distance: " + str(ef.value(rhc.getOptimal()))
print "Route:"
path = []
for x in range(0,N):
    path.append(rhc.getOptimal().getDiscrete(x))
print path

sa = SimulatedAnnealing(1E12, .999, hcp)
fit = FixedIterationTrainer(sa, 200000)
fit.train()
print "SA Inverse of Distance: " + str(ef.value(sa.getOptimal()))
print "Route:"
path = []
for x in range(0,N):
    path.append(sa.getOptimal().getDiscrete(x))
print path


ga = StandardGeneticAlgorithm(2000, 1500, 250, gap)
fit = FixedIterationTrainer(ga, 1000)
fit.train()
print "GA Inverse of Distance: " + str(ef.value(ga.getOptimal()))
print "Route:"
path = []
for x in range(0,N):
    path.append(ga.getOptimal().getDiscrete(x))
print path


# for mimic we use a sort encoding
ef = TravelingSalesmanSortEvaluationFunction(points);
fill = [N] * N
ranges = list(array('i', fill))
odd = DiscreteUniformDistribution(ranges);
df = DiscreteDependencyTree(.1, ranges); 
pop = GenericProbabilisticOptimizationProblem(ef, odd, df);

mimic = MIMIC(500, 100, pop)
fit = FixedIterationTrainer(mimic, 1000)
fit.train()
print "MIMIC Inverse of Distance: " + str(ef.value(mimic.getOptimal()))
print "Route:"
path = []
optimal = mimic.getOptimal()
fill = [0] * optimal.size()
ddata = list(array('d', fill))
for i in range(0,len(ddata)):
    ddata[i] = optimal.getContinuous(i)
temp = ABAGAILArrays()
order = temp.indices(optimal.size())
temp.quicksort(ddata, order)
print order
