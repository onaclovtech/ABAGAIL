from src.shared.Instance import *
import random
#/**
# * A swap one neighbor function
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class SwapNeighbor: # implements NeighborFunction {
    
#    /**
#     * @see opt.ga.MutationFunction#mutate(opt.OptimizationData)
#     */
    def neighbor(self, d):
        if not isinstance(d, Instance):
            raise TypeError("Expected Instance got " + str(d.__class__))
        cod = d.copy()
        i = random.randint(0,cod.getData().size()-1)
        j = random.randint(0,cod.getData().size()-1)
        temp = cod.getContinuous(i)
        cod.getData().set(i, cod.getContinuous(j))
        cod.getData().set(j, temp)
        return cod
