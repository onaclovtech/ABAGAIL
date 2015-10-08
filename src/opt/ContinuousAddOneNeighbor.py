import random
#/**
# * A continuous add one neighbor function
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class ContinuousAddOneNeighbor: # implements NeighborFunction {

    
#    /**
#     * Continuous add one neighbor
#     * @param amount the amount to add
#     */
    def __init__(self, amount = 1):
        self.amount = amount

#    /**
#     * @see opt.NeighborFunction#neighbor(opt.OptimizationData)
#     */
    def neighbor(self, d):
        i = random.randint(0,d.size() - 1)
        cod = d.copy()
        cod.getData().set(i, cod.getContinuous(i)+ random.random() * self.amount - self.amount / 2.0)
        return cod
