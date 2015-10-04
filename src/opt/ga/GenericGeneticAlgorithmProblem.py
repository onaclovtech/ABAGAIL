#/**
# * 
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class GenericGeneticAlgorithmProblem(GenericOptimizationProblem):
#        GeneticAlgorithmProblem {

#    /**
#     * Make a new generic genetic algorithm problem
#     * @param crossover the cross over operator
#     * @param muation the mutation operator
#     * @param eval the evaluation function
#     * @param dist the initial distribution
#     */
    def __init__(EvaluationFunction eval, Distribution dist, MutationFunction mutation, CrossoverFunction crossover):
        self.eval = eval
        self.dist = dist
        self.mutation = mutation
        self.crossover = crossover
        
#    /**
#     * @see opt.ga.GeneticAlgorithmProblem#mate(opt.Instance, opt.Instance)
#     */
    def mate(self,Instance a, Instance b):
        return self.crossover.mate(a, b)

    /**
     * @see opt.ga.GeneticAlgorithmProblem#mutate(opt.Instance)
     */
    def mutate(Instance d):
        self.mutation.mutate(d)
