

#/**
#* A simple state functin doesn't look at the input
#* observations at all when updating it's probabilities
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class SimpleStateDistribution extends DiscreteDistribution
        (StateDistribution), Copyable {

    
#/**
#* Make a new simple state distribution
#* @param probabilities the probabilities
#*/
     SimpleStateDistribution(double[] probabilities):
        super(probabilities)
    }
    

#/**
#* @see hmm.distribution.StateDistribution#probabilityOfState(int, hmm.observation.Observation)
#*/
     double p(int nextState, Instance observation):
        return p(new Instance(nextState))
    }

#/**
#* @see hmm.distribution.StateDistribution#match(double[][], hmm.observation.Observation[])
#*/ 
      estimate(double[][] expectations, DataSet observations):
        double sum = 0
        double[] probabilities = getProbabilities()
        for (int i = 0 i < probabilities.length i++):
           probabilities[i] = 0
        }
        // sum up expectations
        for (int t = 0 t < expectations.length t++):
            for (int j = 0 j < expectations[t].length j++):
                probabilities[j] += expectations[t][j]
                sum += expectations[t][j]
            }
        }
        // probability = expected / sum of expected
        for (int j = 0 j < probabilities.length j++):
            probabilities[j] = (probabilities[j] + getM() * getPrior()[j]) / (sum + getM())
        }
    }

#/**
#* @see hmm.distribution.TransitionDistribution#generateState(hmm.observation.Observation)
#*/
     int generateRandomState(Instance o):
        return sample(o).getDiscrete()
    }

#/**
#* @see hmm.distribution.StateDistribution#generateMostLikely(hmm.observation.Observation)
#*/
     int mostLikelyState(Instance o):
        return mode(o).getDiscrete()
    }
    
     Copyable copy():
        DiscreteDistribution copy = (DiscreteDistribution) super.copy()
        SimpleStateDistribution sscopy = new SimpleStateDistribution(copy.getProbabilities())
        sscopy.setM(getM())
        sscopy.setPrior(getPrior())
        return sscopy
    }
    
    
}
