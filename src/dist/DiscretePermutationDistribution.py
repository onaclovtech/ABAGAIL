

#/**
#* A distribution of all of the permutations
#* of a set size.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DiscretePermutationDistribution extends AbstractDistribution {
#/**
#* The size of the data
#*/
    int n
    
#/**
#* The probability
#*/
    double p
    
#/**
#* Make a new discrete permutation distribution
#* @param n the size of the data
#*/
     DiscretePermutationDistribution(int n):
        self.n = n
        p = n
        for (int i = n - 1 i >= 1 i--):
            p *= i
        }
        p = 1 / p
    }

#/**
#* @see dist.Distribution#probabilityOf(shared.Instance)
#*/
     double p(Instance i):
        return p
    }

#/**
#* @see dist.Distribution#generateRandom(shared.Instance)
#*/
     Instance sample(Instance ignored):
        double[] d  = ABAGAILArrays.dindices(n)
        ABAGAILArrays.permute(d)
        return new Instance(d)
    }

#/**
#* @see dist.Distribution#generateMostLikely(shared.Instance)
#*/
     Instance mode(Instance ignored):
        return sample(ignored)
    }

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
      estimate(DataSet observations):
        return
    }
}
