#/**
# * A uniform cross over function
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class UniformCrossOver:

#    /**
#     * @see opt.CrossOverFunction#mate(opt.OptimizationData, opt.OptimizationData)
#     */
    def mate(self, a, b):
        newData = double[a.size()];
        for i in range(len(newData)):
            if (Distribution.random.nextBoolean()):
                newData[i] = a.getContinuous(i)
            else:
                newData[i] = b.getContinuous(i)
        return Instance(newData)
