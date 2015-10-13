from src.opt.GenericOptimizationProblem import *
#/**
# * 
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class GenericProbabilisticOptimizationProblem(GenericOptimizationProblem):
#implements ProbabilisticOptimizationProblem {

#    /**
#     * Make a new generic probabilisitic optimiziation problem
#     * @param eval the evaluation function
#     * @param dist the initial parameter distribution
#     * @param fact the distribution factory
#     */
    def __init__(self, eval, initial, dist):
        GenericOptimizationProblem.__init__(self,eval,initial)
        self.dist = dist

#    /**
#     * @see opt.prob.ProbabilisticOptimizationProblem#getDistribution()
#     */
    def getDistribution(self):
        return self.dist
