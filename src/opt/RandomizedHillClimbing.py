
#/**
# * A randomized hill climbing algorithm
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class RandomizedHillClimbing: # extends OptimizationAlgorithm {
    
#    /**
#     * Make a new randomized hill climbing
#    */
    def __init__(self, hcp):
#        super(hcp);
        self.cur = hcp.random()
        self.curVal = hcp.value(self.cur)

#    /**
#     * @see shared.Trainer#train()
#     */
    def train(slef):
        hcp = getOptimizationProblem()
        neigh = hcp.neighbor(self.cur)
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
