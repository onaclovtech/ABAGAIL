from src.opt.GenericOptimizationProblem import *
#/**
# * A generic hill climbing problem
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class GenericHillClimbingProblem(GenericOptimizationProblem):

#    /**
#     * Make a new hill climbing problem
#    * @param eval the evaulation function
#     * @param dist the initial distribution
#     * @param neigh the neighbor function
#     */
    def __init__(self, eval, dist, neigh):
        # Check types eventually (if we have problems) EvaluationFunction eval, Distribution dist, NeighborFunction neigh
        GenericOptimizationProblem.__init__(self, eval, dist)
        #print "GHCP" + str(self.initial.__class__)
        self.neigh = neigh

#    /**
#     * @see opt.HillClimbingProblem#neighbor(opt.OptimizationData)
#     */
    def neighbor(self, d):
        return self.neigh.neighbor(d);
