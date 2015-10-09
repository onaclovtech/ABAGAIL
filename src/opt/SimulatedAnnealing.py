import random
import math
from src.opt.OptimizationAlgorithm import *
#/**
# * A simulated annealing hill climbing algorithm
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class SimulatedAnnealing(OptimizationAlgorithm):
#    /**
#     * Make a new simulated annealing hill climbing
#     * @param t the starting temperature
#     * @param cooling the cooling exponent
#     * @param hcp the problem to solve
#     */
    def __init__(self, t, cooling, hcp):
        OptimizationAlgorithm.__init__(self,hcp) 
        #self.hcp = hcp
        self.t = t
        self.cooling = cooling
        self.cur = hcp.random()
        self.curVal = hcp.value(self.cur)

#    /**
#     * @see shared.Trainer#train()
#     */
    def train(self):
        p = self.getOptimizationProblem()
        neigh = p.neighbor.neighbor(self.cur)
        neighVal = p.value(neigh)
        if (neighVal > self.curVal or (random.random() < math.exp((neighVal - self.curVal) / self.t))):
            self.curVal = neighVal
            self.cur = neigh
        self.t = self.t * self.cooling
        return self.curVal

#    /**
#     * @see opt.OptimizationAlgorithm#getOptimal()
#     */
    def getOptimal(self):
        return self.cur
