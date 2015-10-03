#/**
# * A randomized hill climbing algorithm
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class RandomizedHillClimbing: # extends OptimizationAlgorithm {
    
#    /**
#     * Make a new randomized hill climbing
#    */
    def __init__(HillClimbingProblem hcp):
#        super(hcp);
        self.cur = hcp.random()
        self.curVal = hcp.value(cur)

#    /**
#     * @see shared.Trainer#train()
#     */
    def train():
        HillClimbingProblem hcp = (HillClimbingProblem) getOptimizationProblem()
        Instance neigh = hcp.neighbor(cur)
        double neighVal = hcp.value(neigh)
        if (neighVal > curVal):
            self.curVal = neighVal
            self.cur = neigh
        return curVal

#    /**
#     * @see opt.OptimizationAlgorithm#getOptimalData()
#     */
    def getOptimal():
        return cur
