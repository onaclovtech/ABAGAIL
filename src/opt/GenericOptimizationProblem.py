#/**
# * A generic continuous optimization problem
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class GenericOptimizationProblem:

#    /**
#     * Make a new generic optimization problem
#     * @param dist the initial distribution
#     * @param eval the evaluation function
#     */
    def __init__(self, eval, initial):
        # Check types eventually EvaluationFunction eval, Distribution dist
        self.initial = initial;
        self.eval = eval;
    

#    /**
#     * @see opt.OptimizationProblem#value(opt.OptimizationData)
#     */
    def value(self, d):
        return self.eval.value(d)


#    /**
#     * @see opt.OptimizationProblem#random()
#     */
    def random(self):
        return self.initial.sample(None)
