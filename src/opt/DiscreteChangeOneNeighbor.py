import random
#/**
# * A neighbor function for changing a single value
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class DiscreteChangeOneNeighbor: #implements NeighborFunction {
#    /**
#     * Make a new change one neighbor function
#     * @param ranges the ranges of the data
#     */
    def __init__(self, ranges):
        self.ranges = ranges
    
#    /**
#     * @see opt.NeighborFunction#neighbor(opt.OptimizationData)
#     */
    def neighbor(self, d):
        cod = d.copy()
        i = random.randint(0, len(self.ranges)-1)
        cod.getData().set(i, random.randint(0, self.ranges[i]));
        return cod;
