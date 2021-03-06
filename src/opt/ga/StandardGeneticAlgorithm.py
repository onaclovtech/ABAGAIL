import random
import math
from src.opt.OptimizationAlgorithm import *
from src.dist.DiscreteDistribution import *
#/**
# * Genetic algorithms are pretty stupid.
# * This is based on the version in Andrew Moore's tutorial.
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class StandardGeneticAlgorithm(OptimizationAlgorithm):
#    /**
#     * Make a genetic algorithm
#     * @param populationSize the size
#     * @param toMate the number to mate each iteration
#     * @param toMutate the number to mutate each iteration
#     * @param gap the problem to solve
#     */
    def __init__(self, populationSize, toMate, toMutate, gap):
        OptimizationAlgorithm.__init__(self,gap)
        self.toMate = toMate
        self.toMutate = toMutate
        self.populationSize = populationSize
        self.population = [None] * populationSize
        for i in range(len(self.population)):
           self.population[i] = gap.random()
        self.values = [None] * populationSize
        for i in range(len(self.values)):
            self.values[i] = gap.value(self.population[i])
        #print 'StandardGeneticAlgo.__init__.self.values' + str(self.values)
        
#    /**
#     * @see shared.Trainer#train()
#     */
    def train(self):
        ga = self.getOptimizationProblem();
        probabilities = [None] * len(self.population)
        # calculate probability distribution over the population
        sum = 0
        for i in range(len(probabilities)):
            probabilities[i] = self.values[i]
            sum = sum + probabilities[i]
        if (math.isinf(sum)):
            return sum

        for i in range(len(probabilities)):
            probabilities[i] /= float(sum)

        dd = DiscreteDistribution(probabilities = probabilities)
  
        # make the children
        newValues = [None] * self.populationSize
        newPopulation = [None] * self.populationSize
        #print "SGA.train.self.population.length" + str(len(self.population))
        for i in range(self.toMate):
            # pick the mates
            a = self.population[dd.sample(None).getDiscrete()]
            b = self.population[dd.sample(None).getDiscrete()]
            # make the kid
            newPopulation[i] = ga.mate(a, b)
            newValues[i] = -1

        # elite for the rest
        for i in range(len(newPopulation)):
            j = dd.sample(None).getDiscrete()
            newPopulation[i] = self.population[j]
            newValues[i] = self.values[j]
        
        # mutate
        for i in range(self.toMutate):
            j = random.randint(0,len(newPopulation)-1)
            #print "Standard.Genetic.Algorithm.ga: " + str(ga.__class__)
            #print "Standard.Genetic.Algorithm.ga.mutate: " + str(ga.mutate.__dict__)
            #print "Standard.Genetic.Algorithm.newPopulation: " + str(newPopulation[j])
            ga.mutate(newPopulation[j])
            newValues[j] = -1
            
        # calculate the values
        for i in range(len(newValues)):
            if (newValues[i] == -1):
                newValues[i] = ga.value(newPopulation[i])
        # the generation
        self.population = newPopulation
        self.values = newValues
        return float(sum) / self.populationSize

#    /**
#     * @see opt.OptimizationAlgorithm#getOptimalData()
#     */
    def getOptimal(self):
        ga = self.getOptimizationProblem();
        bestVal = self.values[0];
        best = 0;
        for i in range(len(self.population)):
            value = self.values[i]
            if (value > bestVal):
                bestVal = value
                best = i
        return self.population[best]
