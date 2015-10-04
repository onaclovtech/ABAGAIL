#/**
# * A swap one mutation
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class SwapMutation(MutationFunction):

#    /**
#     * @see opt.ga.MutationFunction#mutate(opt.OptimizationData)
#     */
    def mutate(self, Instance d):
        i = Distribution.random.nextInt(d.size())
        j = Distribution.random.nextInt(d.size())
        temp = d.getContinuous(i)
        d.getData().set(i, d.getContinuous(j))
        d.getData().set(j, temp)
