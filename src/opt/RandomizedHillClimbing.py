from src.opt.OptimizationAlgorithm import *
#/**
# * A randomized hill climbing algorithm
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class RandomizedHillClimbing(OptimizationAlgorithm):
    
#    /**
#     * Make a new randomized hill climbing
#    */
    def __init__(self, hcp):
        OptimizationAlgorithm.__init__(self,hcp) # For all I know this really doesn't do much of anything
        self.cur = hcp.random()
        self.curVal = hcp.value(self.cur)

#    /**
#     * @see shared.Trainer#train()
#     */
    def train(self):
        hcp = self.getOptimizationProblem()
        print self.cur
        neigh = hcp.neighbor.neighbor(self.cur) # This seems very odd, we call the neighbor variable then call neighbor on it...oddness
                                                # Not entirely sure how it worked in java
        neighVal = hcp.value(neigh)
        if (neighVal > self.curVal):
            self.curVal = neighVal
            self.cur = neigh
        return self.curVal

#    /**
#     * @see opt.OptimizationAlgorithm#getOptimalData()
#     */
    def getOptimal(self):
        return self.cur
