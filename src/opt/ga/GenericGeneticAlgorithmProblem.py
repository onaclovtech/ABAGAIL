from src.opt.GenericOptimizationProblem import *
#/**
# * 
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class GenericGeneticAlgorithmProblem(GenericOptimizationProblem):


#    /**
#     * Make a new generic genetic algorithm problem
#     * @param crossover the cross over operator
#     * @param muation the mutation operator
#     * @param eval the evaluation function
#     * @param dist the initial distribution
#     */
    def __init__(self,eval, dist, mutation, crossover):
       # check types eventually EvaluationFunction eval, Distribution dist, MutationFunction mutation, CrossoverFunction crossover
        GenericOptimizationProblem.__init__(self,eval, dist)
        self.mutation = mutation
        #print "GGAP" + str(crossover.__class__)
        self.crossover = crossover
        
#    /**
#     * @see opt.ga.GeneticAlgorithmProblem#mate(opt.Instance, opt.Instance)
#     */
    def mate(self, a, b):
        return self.crossover.mate(a, b)

#    /**
#     * @see opt.ga.GeneticAlgorithmProblem#mutate(opt.Instance)
#     */
    def mutate(self, d):
        self.mutation.mutate(d)
