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
    def __init__(double amount = 1):
        self.amount = amount

#    /**
#     * @see opt.NeighborFunction#neighbor(opt.OptimizationData)
#     */
    def neighbor(Instance d):
        int i = Distribution.random.nextInt(d.size())
        Instance cod = (Instance) d.copy()
        cod.getData().set(i, cod.getContinuous(i)+ Distribution.random.nextDouble() * amount - amount / 2)
        return cod
