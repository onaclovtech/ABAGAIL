

#/**
#* A distribution of all of the permutations
#* of a set size.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DiscreteUniformDistribution extends AbstractDistribution {
#/**
#* The ranges of the data
#*/
    int[] n
    
#/**
#* The probability
#*/
    double p
    
#/**
#* Make a new discrete permutation distribution
#* @param n the size of the data
#*/
     DiscreteUniformDistribution(int[] n):
        self.n = n
        p = n[0]
        for (int i = 1 i < n.length i++):
            p *= n[i]
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
        double[] d  = new double[n.length]
        for (int i = 0 i < d.length i++):
            d[i] = random.nextInt(n[i])
        }
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
