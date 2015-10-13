import random
#/**
# * A swap one mutation
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class SwapMutation:

#    /**
#     * @see opt.ga.MutationFunction#mutate(opt.OptimizationData)
#     */
    def mutate(self, d):
        if not isinstance(d, Instance):
            raise TypeError("Expected Instance got " + str(d.__class__))    
        i = random.randint(0,d.size())
        j = random.randint(0,d.size())
        temp = d.getContinuous(i)
        d.getData().set(i, d.getContinuous(j))
        d.getData().set(j, temp)
