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
    def __init__(double t, double cooling, HillClimbingProblem hcp):
        self.hcp = hcp
        self.t = t
        self.cooling = cooling
        self.cur = hcp.random()
        self.curVal = hcp.value(cur)

#    /**
#     * @see shared.Trainer#train()
#     */
    def train(self):
        HillClimbingProblem p = (HillClimbingProblem) getOptimizationProblem()
        Instance neigh = p.neighbor(cur)
        double neighVal = p.value(neigh)
        if (neighVal > self.curVal || Distribution.random.nextDouble() < Math.exp((neighVal - self.curVal) / self.t)):
            self.curVal = neighVal
            self.cur = neigh
        self.t = self.t * cooling
        return self.curVal

#    /**
#     * @see opt.OptimizationAlgorithm#getOptimal()
#     */
    def getOptimal(self):
        return self.cur
