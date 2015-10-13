from src.opt.OptimizationAlgorithm import *
#/**
# * Based on the MIMIC algorithm
# * J. S. De Bonet, C. L. Isbell, and P. Viola (1997). 
# * MIMIC: Finding Optima by Estimating Probability Densities, 
# * Advances in Neural Information Processing Systems, Vol. 9 .
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class MIMIC(OptimizationAlgorithm):
#    /**
#     * Make a new mimic
#     * @param samples the number of samples to take each iteration
#     * @param random how many of those samples should be completely random
#     * @param theta the starting theta
#     * @param increment the increment
#     * @param stoppingCount the minimum number of good samples needed to continue
#     * @param op the problem
#     */
    def __init__(self, samples, tokeep,  op):
        OptimizationAlgorithm.__init__(self,op)
        self.tokeep = tokeep
        self.samples = samples
        data = [None] * samples
        for i in range(len(data)):
            data[i] = self.op.random()
        self.distribution = self.op.getDistribution()
        self.distribution.estimate(DataSet(ds = data))

#    /**
#     * @see opt.OptimizationAlgorithm#getOptimal()
#     */
    def getOptimal(self):
        op = getOptimizationProblem()
        data = [None] * samples
        for i in range(len(data)):
            data[i] = distribution.sample(None)
        bestVal = op.value(data[0])
        best = data[0]
        for i in range(len(data)):
            value = op.value(data[i])
            if (value > bestVal):
                bestVal = value
                best = data[i]
        return best;

#    /**
#     * @see shared.Trainer#train()
#     */
    # def train(self):
        # op = getOptimizationProblem();
        # data = [None] * samples
        # for i in range(len(data)):
            # data[i] = distribution.sample(None)
        # values = [None] * len(data)
        # for i in range(len(data)):
            # values[i] = op.value(data[i])
        # double[] temp = new double[values.length];
        # System.arraycopy(values, 0, temp, 0, temp.length);
        # double cutoff = ABAGAILArrays.randomizedSelect(temp, temp.length - tokeep);
        # int j = 0;
        # Instance[] kept = new Instance[tokeep];
        # for (int i = 0; i < data.length && j < kept.length; i++):
            # if (values[i] >= cutoff):
                # kept[j] = data[i];
                # j++;
        # distribution.estimate(new DataSet(kept))
        # return cutoff
