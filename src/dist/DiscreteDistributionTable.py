


#/**
#* A class implementing a look up table for
#* conditional probability, that is
#* representing P(O = o | I = i) for some single
#* discrete random variables O the output and
#* I the input
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DiscreteDistributionTable extends AbstractConditionalDistribution (Copyable):

#/**
#* The probability table
#*/
    DiscreteDistribution[] discreteDistributions
    
#/**
#* Make a new look up table conditional probability
#* @param probabilities the initial probabilities
#* @param m the m estimate parameter
#*/
     DiscreteDistributionTable(double[][] probabilities):
        discreteDistributions = new DiscreteDistribution[probabilities.length]
        for (int i = 0 i < discreteDistributions.length i++):
            discreteDistributions[i] = new DiscreteDistribution(probabilities[i])
        }
    }
    
#/**
#* Make a new table
#* @param table the table to use
#* @param m the m estimate parameter
#*/
     DiscreteDistributionTable(DiscreteDistribution[] table):
        self.discreteDistributions = table
    }

#/**
#* @see dist.ConditionalDistribution#distributionFor(shared.Instance)
#*/
     Distribution distributionFor(Instance i):
        return discreteDistributions[i.getDiscrete()]
    }

#/**
#* @see shared.Distribution#reestimate(shared.DataSet)
#*/
      estimate(DataSet observations):
        double[] sums = new double[discreteDistributions.length]
        double[][] probabilities = getProbabilityMatrix()
        for (int i = 0 i < probabilities.length i++):
            for (int j = 0 j < probabilities[i].length j++):
                probabilities[i][j] = 0
            }
        }
        for (int i = 0 i < observations.size() i++):
            Instance cur = observations.get(i)
            sums[cur.getDiscrete()] += cur.getWeight()
            probabilities[cur.getDiscrete()][cur.getLabel().getDiscrete()] += cur.getWeight()
        }
        for (int i = 0 i < probabilities.length i++):
        	   double[] prior = discreteDistributions[i].getPrior()
        	   double m = discreteDistributions[i].getM()
            for (int j = 0 j < probabilities[i].length j++):
                probabilities[i][j] = (probabilities[i][j] + prior[i] * m) / (sums[i] + m)
            }
        }
    }
    
    
    
#/**
#* Get the probability matrix
#* value [i][j] i the matrix is the
#* probability of observing j given i
#* @return the matrix
#*/
     double[][] getProbabilityMatrix():
        double[][] matrix = new double[getInputRange()][]
        for (int i = 0 i < getInputRange() i++):
            matrix[i] = discreteDistributions[i].getProbabilities()
        }
        return matrix
    }
    
#/**
#* Set the probability matrix
#* @param matrix the matrix
#*/
      setProbabilityMatrix(double[][] matrix):
        for (int i = 0 i < getInputRange() i++):
            discreteDistributions[i].setProbabilities(matrix[i])
        }
    }
    
#/**
#* Get the discrete distributions
#* @return the distributions
#*/
     DiscreteDistribution[] getDistributions():
    		 return discreteDistributions
    }
    
#/**
#* Set the distributions
#* @param distributions the distributions
#*/
      setDistributions(DiscreteDistribution[] distributions):
    		self.discreteDistributions = distributions
    }
    
#/**
#* Get the input range
#* @return the range
#*/
     int getInputRange():
        return discreteDistributions.length
    }
    
#/**
#* Get the output range
#* @return the range
#*/
     int getOutputRange():
        return discreteDistributions[0].getRange()
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return ABAGAILArrays.toString(getProbabilityMatrix())
    }
    
#/**
#* Make a uniform table
#* @param inputRange the input range
#* @param outputRange the output range
#* @param m the m value
#* @return the table
#*/
     static DiscreteDistributionTable uniform(int inputRange, int outputRange):
        DiscreteDistribution[] table = new DiscreteDistribution[inputRange]
        for (int i = 0 i < table.length i++):
            table[i] = DiscreteDistribution.uniform(outputRange)
        }
        return new DiscreteDistributionTable(table)
    }
    
#/**
#* Make a random table
#* @param inputRange the input range
#* @param outputRange the output range
#* @param m the m value
#* @return the table
#*/
     static DiscreteDistributionTable random(int inputRange, int outputRange):
        DiscreteDistribution[] table = new DiscreteDistribution[inputRange]
        for (int i = 0 i < table.length i++):
            table[i] = DiscreteDistribution.random(outputRange)
        }
        return new DiscreteDistributionTable(table)
    }

#/**
#* @see shared.Copyable#copy()
#*/
     Copyable copy():
        DiscreteDistribution[] copies = new DiscreteDistribution[discreteDistributions.length]
        for (int i = 0 i < copies.length i++):
            copies[i] = (DiscreteDistribution) discreteDistributions[i].copy()
        }
        DiscreteDistributionTable copy = new DiscreteDistributionTable(copies)
        return copy
    }



}
