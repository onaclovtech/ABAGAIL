#/**
# * An abstract class for optimzation algorithms
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class OptimizationAlgorithm:
#    /**
#     * Make a new optimization algorithm
#     * @param op the problem to optimize
#     */
    def __init__(OptimizationProblem op) {
        this.op = op;
    }
    
#    /**
#     * Get an optimization problem
#     * @return the problem
#     */
    def getOptimizationProblem():
        return op
    
#    /**
#     * Get the optimal data
#     * @return the data
#     */
    def getOptimal():
        print ""
