import random
from src.dist.AbstractDistribution import *
from src.util.ABAGAILArrays import *
from src.shared.Instance import *
#/**
#* A probabilitiy function for representing single discrete
#* output values
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class DiscreteDistribution(AbstractDistribution):
	
#/**
#* The array of probabilities
#*/
 #   double[] probabilities
    
#/**
#* The prior probabilities
#*/
  #  double[] prior
    
#/**
#* The cummulatives
#*/
  #  double[] cummulatives
    
#/**
#* The continuity parameter
#*/
   # double m
    
#/**
#* Make a new single discrete output
#* that models the given probabilities
#* @param probabilities array of probabilitites
#* such that the probabilities of output i
#* is probabilitites[i]
#* @param m the continuity parameter
#*/
      def __init__(self, vector = None, probabilities= None):
         if vector:
            if type(vector) != type(Vector()):
               raise TypeError('Expected Vector got ' + str(vector.__class__))
            self.m = vector.size()
            self.prior = [1.0/vector.size()] * vector.size()
            self.probabilities = [None] * vector.size()
            for i in range(vector.size()):
               self.probabilities[i] = vector.get(i)
      
         
         if probabilities:
            self.probabilities = probabilities
            #print "DiscreteDistribution.__init__.self.probabilities.length" + str(len(self.probabilities))
            self.m = len(probabilities)
            self.prior = [1.0/len(probabilities)] * len(probabilities)
         self.cummulatives = None
     
     
#/**
#* Set the probabilities
#* @param probabilities the probabilities
#*/
      def setProbabilities(self,probabilities):
        self.probabilities = probabilities
        self.cummulatives = None
    
    
#/**
#* Get the probabilities
#* @return the probailities
#*/
      def getProbabilities(self):
        return self.probabilities

#/**
#* Get the probability of i
#* @param i the discrete value to get the probability of
#* @return the probability of i
#*/
      def p(self, i):
        return self.probabilities[i.getDiscrete()]
    

#/**
#* Generate a discrete value consistent with the distribution
#* @return the discrete value
#*/
      def sample(self, ignored):
        if self.cummulatives is None:
            self.calculateCummulatives()
        rand = random.random()
        #print "DiscreteDistribution.sample.random" + str(rand)
        #print "DiscreteDistribution.sample.cummulative" + str(self.cummulatives)
        temp = ABAGAILArrays()
        result = temp.search(self.cummulatives, rand)
       # print "DiscreteDistribution.sample.search.result" + str(result)
        return Instance(val = result)  
    # }
    
# #/**
# #* Recalculate the cummulativies
# #*/
      def calculateCummulatives(self):
        self.cummulatives = [None] * len(self.probabilities)
        self.cummulatives[0] = self.probabilities[0]
        for i in range(1, len(self.cummulatives)):
            self.cummulatives[i] = self.cummulatives[i-1] + self.probabilities[i]
    
# #/**
# #* Generate the most likely value
# #* @return the value
# #*/
     # Instance mode(Instance ignored):
        # int argMax = 0
        # for (int i = 1 i < probabilities.length i++):
            # if (probabilities[i] > probabilities[argMax]):
                # argMax = i
            # }
        # }
        # return new Instance(argMax)
    # }
    
# #/**
# #* Reestimage based on the given data set
# #* @param observations the observations
# #*/
      # estimate(DataSet observations):
        # double weightSum = 0
        # for (int i = 0 i < probabilities.length i++):
            # probabilities[i] = 0
        # }
        # for (int i = 0 i < observations.size() i++):
            # Instance cur = observations.get(i)
            # weightSum += cur.getWeight()
            # probabilities[cur.getDiscrete()] += cur.getWeight()
        # }
        # for (int i = 0 i < probabilities.length i++):
            # probabilities[i] = (probabilities[i] + m * prior[i])
                # / (weightSum + m)
        # }
        # cummulatives = null
    # }
    
# #/**
# #* Get the range of values represented
# #* @return the range
# #*/
     # int getRange():
        # return probabilities.length
    # }
    
# #/**
# #* Get the m value
# #* @return the m value
# #*/
     # double getM():
        # return m
    # }

# #/**
# #* Set the m value
# #* @param d the new m value
# #*/
      # setM(double d):
        # m = d
    # }
    
# #/**
# #* Set the prior probability
# #* @param priors the prior
# #*/
      # setPrior(double[] priors):
    		# self.prior = priors
    # }
    
# #/**
# #* Get the prior probability
# #* @return the prior probability
# #*/
     # double[] getPrior():
    		# return prior
    # }
    
# #/**
# #* @see java.lang.Object#toString()
# #*/
     # String toString():
        # return ABAGAILArrays.toString(probabilities)
    # }
    

# #/**
# #* @see shared.Copyable#copy()
# #*/
     # Copyable copy():
        # double[] copyProbabilities = new double[probabilities.length]
        # for (int i = 0 i < copyProbabilities.length i++):
            # copyProbabilities[i] = probabilities[i]
        # }
        # DiscreteDistribution copy = new DiscreteDistribution(copyProbabilities)
        # copy.setM(m)
        # copy.setPrior(prior)
        # return copy
    # }
    
# #/**
# #* Make a new single discrete output
# #* that models values [0, 1, 2, ..., range - 1]
# #* @param range the upper range of the output
# #*/
     # static DiscreteDistribution random(int range):
        # double[] probabilities = new double[range]
        # // random intial values
        # double sum = 0
        # for (int i = 0 i < probabilities.length i++):
            # probabilities[i] = random.nextDouble()
            # sum += probabilities[i]
        # }
        # for (int i = 0 i < probabilities.length i++):
            # probabilities[i] /= sum
        # }
        # return new DiscreteDistribution(probabilities)
    # }
    
# #/**
# #* Make a new single discrete output
# #* that models values [0, 1, 2, ..., range - 1]
# #* @param range the upper range of the output
# #*/
     # static DiscreteDistribution uniform(int range):
        # double[] probabilities = new double[range]
        # Arrays.fill(probabilities, 1.0/probabilities.length)
        # return new DiscreteDistribution(probabilities)
    # }

    



# }
