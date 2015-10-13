# import sys
# import os
# import time


from src.dist.DiscreteDependencyTree import *
from src.dist.DiscreteUniformDistribution import *
#from src.dist.Distribution import *
from src.opt.DiscreteChangeOneNeighbor import *
#from src.opt.EvaluationFunction import *
from src.opt.GenericHillClimbingProblem import *
#from src.opt.HillClimbingProblem import *
#from src.opt.NeighborFunction import *
from src.opt.RandomizedHillClimbing import *
from src.opt.SimulatedAnnealing import *
#from src.opt.example.FourPeaksEvaluationFunction import *
#from src.opt.ga.CrossoverFunction import *
from src.opt.ga.SingleCrossOver import *
from src.opt.ga.DiscreteChangeOneMutation import *
from src.opt.ga.GenericGeneticAlgorithmProblem import *
#from src.opt.ga.GeneticAlgorithmProblem import *
#from src.opt.ga.MutationFunction import *
from src.opt.ga.StandardGeneticAlgorithm import *
#from src.opt.ga.UniformCrossOver import *
from src.opt.prob.GenericProbabilisticOptimizationProblem import *
from src.opt.prob.MIMIC import *
#from src.opt.prob.ProbabilisticOptimizationProblem import *
from src.shared.FixedIterationTrainer import *
from src.opt.example.CountOnesEvaluationFunction import *
from array import array




"""
Commandline parameter(s):
   none
"""

N=80
fill = [2] * N
ranges = list(array('i', fill))

ef = CountOnesEvaluationFunction()
odd = DiscreteUniformDistribution(ranges)
nf = DiscreteChangeOneNeighbor(ranges)
mf = DiscreteChangeOneMutation(ranges)
cf = SingleCrossOver()
df = DiscreteDependencyTree(.1, ranges)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
pop = GenericProbabilisticOptimizationProblem(ef, odd, df)

rhc = RandomizedHillClimbing(hcp)
fit = FixedIterationTrainer(rhc, 200)
fit.train()
print "RHC: " + str(ef.value(rhc.getOptimal()))

sa = SimulatedAnnealing(100, .95, hcp)
fit = FixedIterationTrainer(sa, 200)
fit.train()
print "SA: " + str(ef.value(sa.getOptimal()))

ga = StandardGeneticAlgorithm(20, 20, 0, gap)
fit = FixedIterationTrainer(ga, 300)
fit.train()
print "GA: " + str(ef.value(ga.getOptimal()))

mimic = MIMIC(50, 10, pop)
fit = FixedIterationTrainer(mimic, 100)
fit.train()
print "MIMIC: " + str(ef.value(mimic.getOptimal()))
