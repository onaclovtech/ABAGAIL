#/**
# * A generic continuous optimization problem
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class GenericOptimizationProblem:  # Inherit? OptimizationProblem {

#    /**
#     * Make a new generic optimization problem
#     * @param dist the initial distribution
#     * @param eval the evaluation function
#     */
    def __init__(EvaluationFunction eval, Distribution dist):
        self.initial = dist;
        self.eval = eval;
    

#    /**
#     * @see opt.OptimizationProblem#value(opt.OptimizationData)
#     */
    def value(Instance d)
        return eval.value(d)


#    /**
#     * @see opt.OptimizationProblem#random()
#     */
    def random():
        return initial.sample(null)
