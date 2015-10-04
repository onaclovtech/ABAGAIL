#/**
# * Genetic algorithms are pretty stupid.
# * This is based on the version in Andrew Moore's tutorial.
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class StandardGeneticAlgorithm(OptimizationAlgorithm):
#    /**
#     * Make a new genetic algorithm
#     * @param populationSize the size
#     * @param toMate the number to mate each iteration
#     * @param toMutate the number to mutate each iteration
#     * @param gap the problem to solve
#     */
    def __init__(self, int populationSize, int toMate, int toMutate, GeneticAlgorithmProblem gap) {
        self.gap = gap
        self.toMate = toMate
        self.toMutate = toMutate
        self.populationSize = populationSize
        self.population = new Instance[populationSize]
        for (int i = 0; i < population.length; i++):
            population[i] = gap.random()
        self.values = new double[populationSize]
        for (i = 0; i < values.length; i++):
            values[i] = gap.value(population[i])
        
#    /**
#     * @see shared.Trainer#train()
#     */
    def train(self):
        GeneticAlgorithmProblem ga = (GeneticAlgorithmProblem) getOptimizationProblem();
        probabilities = new double[population.length]
        // calculate probability distribution over the population
        sum = 0
        for (i = 0; i < probabilities.length; i++):
            probabilities[i] = values[i]
            sum += probabilities[i]
        if (Double.isInfinite(sum)):
            return sum

        for (i = 0; i < probabilities.length; i++):
            probabilities[i] /= sum

        DiscreteDistribution dd = new DiscreteDistribution(probabilities)
  
        // make the children
        newValues = new double[populationSize];
        newPopulation = new Instance[populationSize];
        for (i = 0; i < toMate; i++):
            // pick the mates
            Instance a = population[dd.sample(null).getDiscrete()]
            Instance b = population[dd.sample(null).getDiscrete()]
            // make the kid
            newPopulation[i] = ga.mate(a, b)
            newValues[i] = -1

        // elite for the rest
        for (i = toMate; i < newPopulation.length; i++):
            j = dd.sample(null).getDiscrete()
            newPopulation[i] = population[j]
            newValues[i] = values[j]
        
        // mutate
        for (i = 0; i < toMutate; i++):
        	j = random.nextInt(newPopulation.length)
            ga.mutate(newPopulation[j])
            newValues[j] = -1
            
        // calculate the new values
        for (i = 0; i < newValues.length; i++):
            if (newValues[i] == -1):
                newValues[i] = ga.value(newPopulation[i])
        // the new generation
        population = newPopulation
        values = newValues
        return sum / populationSize

#    /**
#     * @see opt.OptimizationAlgorithm#getOptimalData()
#     */
    def getOptimal(self):
        GeneticAlgorithmProblem ga = (GeneticAlgorithmProblem) getOptimizationProblem();
        bestVal = values[0];
        best = 0;
        for (i = 1; i < population.length; i++):
            value = values[i]
            if (value > bestVal):
                bestVal = value
                best = i
        return population[best]
