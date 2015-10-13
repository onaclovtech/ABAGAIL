import random
#/**
# * A mutation function for changing a single value
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class DiscreteChangeOneMutation:    

#    /**
#     * Make a new discrete change one mutation function
#     * @param ranges the ranges of the data
#     */
    def __init__(self,ranges): 
        self.ranges = ranges

#    /**
#     * @see opt.ga.MutationFunction#mutate(opt.OptimizationData)
#     */
    def mutate(self, d):
        i = random.randint(0, d.size() - 1)
        d.getData().set(i, random.randint(0, self.ranges[i]))

