import random
from src.shared.Instance import *
#/**
# * A single point cross over function
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class SingleCrossOver:

#    /**
#     * @see opt.CrossOverFunction#mate(opt.OptimizationData, opt.OptimizationData)
#     */
    def mate(self, a, b):
        newData = [None] * a.size()
        point = random.randint(0,len(newData) + 1)
        for i in range(len(newData)):
            if (i >= point):
                newData[i] = a.getContinuous(i)
            else:
                newData[i] = b.getContinuous(i)
        return Instance(ds = newData)
