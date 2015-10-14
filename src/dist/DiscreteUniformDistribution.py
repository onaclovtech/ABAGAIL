from src.dist.AbstractDistribution import *
from src.shared.Instance import *
import random

#/**
#* A distribution of all of the permutations
#* of a set size.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DiscreteUniformDistribution (AbstractDistribution):
#/**
#* The ranges of the data
#*/
   # int[] n
    
#/**
#* The probability
#*/
   # double p
    
#/**
#* Make a new discrete permutation distribution
#* @param n the size of the data
#*/
     def __init__(self, n):
        if not isinstance(n, list):
            raise TypeError("Expected a list got " + str(n.__class__))
        self.n = n
        self.p = n[0] #doesn't setting self.p to 1 and then looping through from i = 0 to length accomplish the same thing?
        for i in range(1, len(n)):
            self.p *= n[i]
        
        self.p = 1 / self.p
    

#/**
#* @see dist.Distribution#probabilityOf(shared.Instance)
#*/
     def p(self, i): # i is unused...this is really weird. may need to get rid of all together
        if not isinstance(i, Instance):
            raise TypeError("Expected Instance got " + str(i.__class__))
        return p

#/**
#* @see dist.Distribution#generateRandom(shared.Instance)
#*/
     def sample(self, ignored): # Strange that we pass anything in. also the type check is probably unnecessary
        # if not isinstance(ignored, Instance):
            # raise TypeError("Expected Instance got " + str(ignored.__class__))
        d  = [None] * len(self.n)
        for i in range(len(d)):
            d[i] = random.randint(0,self.n[i]-1)
        
        return Instance(ds = d)
    

#/**
#* @see dist.Distribution#generateMostLikely(shared.Instance)
#*/
     def mode(self, ignored):
        if not isinstance(ignored, Instance):
            raise TypeError("Expected Instance got " + str(ignored.__class__))
        return sample(ignored)
    

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
     # Does Nothing, Why is this being called?
     def estimate(self, observations):
        if not isinstance(observations, DataSet):
            raise TypeError("Expected DataSet got " + str(observations.__class__))
        raise ImplementationError("Not Implemented")
        return
    