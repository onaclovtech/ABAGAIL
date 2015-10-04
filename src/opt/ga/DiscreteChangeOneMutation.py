#/**
# * A mutation function for changing a single value
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class DiscreteChangeOneMutation(MutationFunction):    

#    /**
#     * Make a new discrete change one mutation function
#     * @param ranges the ranges of the data
#     */
    def __init__(int[] ranges): 
        self.ranges = ranges

#    /**
#     * @see opt.ga.MutationFunction#mutate(opt.OptimizationData)
#     */
    def mutate(self, Instance d):
        int i = Distribution.random.nextInt(d.size())
        d.getData().set(i, Distribution.random.nextInt(ranges[i]))
