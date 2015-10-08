import random
from src.dist.AbstractDistribution import *
from src.shared.Instance import *


#/**
#* A distribution for neural network weights
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class NeuralNetworkWeightDistribution(AbstractDistribution):
   
#/** 
#* The weight count
#*/ 
    #int weightCount
    
#/**
#* Make a new neural network weight distribution
#* @param weightCount the weight count
#*/
     def __init__(self, weightCount):
        self.weightCount = weightCount
    

#/**
#* @see dist.Distribution#probabilityOf(shared.Instance)
#*/
     def p(self, i):
        return 1
    

#/**
#* @see dist.Distribution#generateRandom(shared.Instance)
#*/
     def sample(self, ignored):
        weights = [self.weightCount]
        for i in range(len(weights)):
            weights[i] = random.random() - .5
        return Instance(ds =weights)
    

#/**
#* @see dist.Distribution#generateMostLikely(shared.Instance)
#*/
     def mode(self, ignored):
        return sample(ignored)
    

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
     def estimate(observations):
        return
    
    
    


