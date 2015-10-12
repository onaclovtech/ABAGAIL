import random
#/**
# * A continuous add one neighbor function
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class ContinuousAddOneMutation:
#    /**
#     * Continuous add one neighbor
#     * @param amount the amount to add
#     */
    def __init__(self, amount = 1):
        self.amount = amount

#    /**
#     * @see opt.ga.MutationFunction
#     */
    def mutate(self, cod):
        i = random.randint(0,cod.size()-1)
        cod.getData().set(i, cod.getContinuous(i) + random.random() * self.amount - self.amount / 2)
