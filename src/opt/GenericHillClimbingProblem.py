#/**
# * A generic hill climbing problem
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class GenericHillClimbingProblem: # extends GenericOptimizationProblem implements HillClimbingProblem {

#    /**
#     * Make a new hill climbing problem
#    * @param eval the evaulation function
#     * @param dist the initial distribution
#     * @param neigh the neighbor function
#     */
    def __init__(EvaluationFunction eval, Distribution dist, NeighborFunction neigh):
        super(eval, dist);
        this.neigh = neigh;

#    /**
#     * @see opt.HillClimbingProblem#neighbor(opt.OptimizationData)
#     */
    def neighbor(Instance d):
        return neigh.neighbor(d);
