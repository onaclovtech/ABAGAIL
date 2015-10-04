

#/**
#* A look up table distribution for transitions
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class SimpleStateDistributionTable extends DiscreteDistributionTable
         (StateDistribution), Copyable {

    
#/**
#* Create a new look up table transition distribution
#* @param probabilities the array of probabilities
#*/
     SimpleStateDistributionTable(double[][] probabilities):
        super(probabilities)
    }
    
#/**
#* Make a new look up table of transition probabilities
#* @param distributions
#*/
     SimpleStateDistributionTable(DiscreteDistribution[] distributions):
    	    super(distributions)
    }

#/**
#* @see hmm.distribution.TransitionDistribution#probabilityOfState(int, hmm.observation.Observation)
#*/
     double p(int nextState, Instance o):
        Instance instance = new Instance(o.getData(), new Instance(nextState))
        return p(instance)
    }

#/**
#* @see hmm.distribution.TransitionDistribution#generateState(hmm.observation.Observation)
#*/
     int generateRandomState(Instance o):
        return sample(o).getDiscrete()
    }

#/**
#* @see hmm.distribution.TransitionDistribution#match(double[][], hmm.observation.Observation[])
#*/
      estimate(double[][] expectations, DataSet observations):
        double[][] matrix = getProbabilityMatrix()
        double[] sums = new double[getInputRange()]
        for (int i = 0 i < matrix.length i++):
            for (int j = 0 j < matrix[i].length j++):
            	    matrix[i][j] = 0
            }
        }
        // sum up expectations
        for (int t = 0 t < expectations.length t++):
            int input = observations.get(t).getDiscrete()
            for (int j = 0 j < expectations[t].length j++):
                matrix[input][j] += expectations[t][j]
                sums[input] += expectations[t][j]
            }
        }

        // probability = expected / sum of expected
        for (int i = 0 i < matrix.length i++):
        	    double[] prior = getDistributions()[i].getPrior()
        	    double m = getDistributions()[i].getM()
            for (int j = 0 j < matrix[i].length j++):
                matrix[i][j] = (matrix[i][j] + m * prior[j]) /  (sums[i] + m)
            }   
           
        }
    }

#/**
#* @see hmm.distribution.StateDistribution#generateMostLikely(hmm.observation.Observation)
#*/
     int mostLikelyState(Instance o):
        return mode(o).getDiscrete()
    }
    
     Copyable copy():
        DiscreteDistributionTable copy = (DiscreteDistributionTable) super.copy()
        DiscreteDistributionTable sscopy = new SimpleStateDistributionTable(copy.getDistributions())
        return sscopy
    }

}
