#/**
# * A uniform cross over function
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class UniformCrossOver(CrossoverFunction):

#    /**
#     * @see opt.CrossOverFunction#mate(opt.OptimizationData, opt.OptimizationData)
#     */
    def mate(self, Instance a, Instance b):
        newData = new double[a.size()];
        for (i = 0; i < newData.length; i++):
            if (Distribution.random.nextBoolean()):
                newData[i] = a.getContinuous(i)
            else:
                newData[i] = b.getContinuous(i)
        return new Instance(newData)
