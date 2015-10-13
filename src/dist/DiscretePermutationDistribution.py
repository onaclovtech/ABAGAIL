from src.util.ABAGAILArrays import *
from src.dist.AbstractDistribution import *
from src.shared.Instance import *

#/**
#* A distribution of all of the permutations
#* of a set size.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DiscretePermutationDistribution (AbstractDistribution):
#/**
#* The size of the data
#*/
    #int n
    
#/**
#* The probability
#*/
    #double p
    
#/**
#* Make a new discrete permutation distribution
#* @param n the size of the data
#*/
     def __init__(self, n):
        self.n = n
        self.p = n
        #for (int i = n - 1 i >= 1 i--): # not entirely sure why you would start at the end and multiply decremented. I'm just going to do nrmal
        for i in range(1,n):
            self.p = self.p * i
        self.p = 1.0 / self.p
    

#/**
#* @see dist.Distribution#probabilityOf(shared.Instance)
#*/
     def p(self, i):
        return p
    

#/**
#* @see dist.Distribution#generateRandom(shared.Instance)
#*/
     def sample(self, ignored):
        temp = ABAGAILArrays()
        d  = temp.dindices(self.n)
        temp.permute(d)
        return Instance(ds = d)
    

#/**
#* @see dist.Distribution#generateMostLikely(shared.Instance)
#*/
     def mode(self, ignored):
        return sample(ignored)
    

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
     def estimate(self, observations):
        raise ImplementationError("This was never implemented")
        return
    
