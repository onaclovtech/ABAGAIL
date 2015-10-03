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
    def __init__(int[] ranges):
        this.ranges = ranges;
    
#    /**
#     * @see opt.NeighborFunction#neighbor(opt.OptimizationData)
#     */
    def neighbor(Instance d):
        Instance cod = (Instance) d.copy();
        int i = Distribution.random.nextInt(ranges.length);
        cod.getData().set(i, Distribution.random.nextInt(ranges[i]));
        return cod;
