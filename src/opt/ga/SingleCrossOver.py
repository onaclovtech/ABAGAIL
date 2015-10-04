#/**
# * A single point cross over function
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class SingleCrossOver(CrossoverFunction):

#    /**
#     * @see opt.CrossOverFunction#mate(opt.OptimizationData, opt.OptimizationData)
#     */
    def mate(self, a, b):
        newData = new double[a.size()]
        point = Distribution.random.nextInt(newData.length + 1)
        for (i = 0; i < newData.length; i++):
            if (i >= point):
                newData[i] = a.getContinuous(i)
            else:
                newData[i] = b.getContinuous(i)
        return new Instance(newData)
