# import sys
# import os
# import time
import random
from src.dist.DiscreteDependencyTree import *
from src.dist.DiscreteUniformDistribution import *
# import dist.Distribution as Distribution
from src.opt.DiscreteChangeOneNeighbor import *
# import opt.EvaluationFunction as EvaluationFunction
from src.opt.GenericHillClimbingProblem import *
# import opt.HillClimbingProblem as HillClimbingProblem
# import opt.NeighborFunction as NeighborFunction
from src.opt.RandomizedHillClimbing import *
from src.opt.SimulatedAnnealing import *
# import opt.example.FourPeaksEvaluationFunction as FourPeaksEvaluationFunction
# import opt.ga.CrossoverFunction as CrossoverFunction
# import opt.ga.SingleCrossOver as SingleCrossOver
from src.opt.ga.DiscreteChangeOneMutation import *
from src.opt.ga.GenericGeneticAlgorithmProblem import *
# import opt.ga.GeneticAlgorithmProblem as GeneticAlgorithmProblem
#from src.opt.ga.MutationFunction import *
from src.opt.ga.StandardGeneticAlgorithm import *
from src.opt.ga.UniformCrossOver import *
from src.opt.prob.GenericProbabilisticOptimizationProblem import *
from src.opt.prob.MIMIC import *
# import opt.prob.ProbabilisticOptimizationProblem as ProbabilisticOptimizationProblem
from src.shared.FixedIterationTrainer import *
from src.opt.example.KnapsackEvaluationFunction import *
from array import array




"""
Commandline parameter(s):
    none
"""

# The number of items
NUM_ITEMS = 40
# The number of copies each
COPIES_EACH = 4
# The maximum weight for a single element
MAX_WEIGHT = 50
# The maximum volume for a single element
MAX_VOLUME = 50
# The volume of the knapsack 
KNAPSACK_VOLUME = MAX_VOLUME * NUM_ITEMS * COPIES_EACH * .4

# create copies
fill = [COPIES_EACH] * NUM_ITEMS
copies = array('i', fill)

# create weights and volumes
fill = [0] * NUM_ITEMS
weights = array('d', fill)
volumes = array('d', fill)
for i in range(0, NUM_ITEMS):
    weights[i] = random.random() * MAX_WEIGHT
    volumes[i] = random.random() * MAX_VOLUME


# create range
fill = [COPIES_EACH + 1] * NUM_ITEMS
ranges = list(array('i', fill))
ef = KnapsackEvaluationFunction(weights, volumes, KNAPSACK_VOLUME, copies)
odd = DiscreteUniformDistribution(ranges)
nf = DiscreteChangeOneNeighbor(ranges)
mf = DiscreteChangeOneMutation(ranges)
cf = UniformCrossOver()
df = DiscreteDependencyTree(.1, ranges)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
pop = GenericProbabilisticOptimizationProblem(ef, odd, df)

rhc = RandomizedHillClimbing(hcp)
fit = FixedIterationTrainer(rhc, 200000)
fit.train()
print "RHC: " + str(ef.value(rhc.getOptimal()))

sa = SimulatedAnnealing(100, .95, hcp)
fit = FixedIterationTrainer(sa, 200000)
fit.train()
print "SA: " + str(ef.value(sa.getOptimal()))

ga = StandardGeneticAlgorithm(200, 150, 25, gap)
fit = FixedIterationTrainer(ga, 1000)
fit.train()
print "GA: " + str(ef.value(ga.getOptimal()))

mimic = MIMIC(200, 100, pop)
fit = FixedIterationTrainer(mimic, 1000)
fit.train()
print "MIMIC: " + str(ef.value(mimic.getOptimal()))
