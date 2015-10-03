#/**
# * A generic hill climbing problem
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class GenericHillClimbingProblem(GenericOptimizationProblem,HillClimbingProblem):

#    /**
#     * Make a new hill climbing problem
#    * @param eval the evaulation function
#     * @param dist the initial distribution
#     * @param neigh the neighbor function
#     */
    def __init__(EvaluationFunction eval, Distribution dist, NeighborFunction neigh):
        self.eval = eval
        self.dist = dist
        self.neigh = neigh

#    /**
#     * @see opt.HillClimbingProblem#neighbor(opt.OptimizationData)
#     */
    def neighbor(self, Instance d):
        return self.neigh.neighbor(d);
