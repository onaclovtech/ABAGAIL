

#/**
#* A distribution who's  probabilities
#* are precalculated and stored in the observation
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class PrecalculatedDistribution extends AbstractDistribution (Copyable):
#/**
#* The index at which the precalculated probability is stored
#*/
    int i
    
#/**
#* Make a new precalculated output distribution
#* @param i the index
#*/
     PrecalculatedDistribution(int i):
        self.i = i
    }

#/**
#* @see hmm.distribution.OutputDistribution#generateRandom(hmm.observation.Observation)
#*/
     Instance sample(Instance input):
        return null
    }

#/**
#* @see hmm.distribution.OutputDistribution#generateMostLikely(hmm.observation.Observation)
#*/
     Instance mode(Instance input):
        return null
    }

#/**
#* @see hmm.distribution.OutputDistribution#probabilityOfObservation(hmm.observation.Observation)
#*/
     double p(Instance inst):
        return inst.getContinuous(i)
    }
    

#/**
#* @see dist.Distribution#logLikelihood(shared.Instance)
#*/
     double logp(Instance i):
        return Math.log(p(i))
    }

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
      estimate(DataSet observations): }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return "Precalculated " + i
    }

#/**
#* @see shared.Copyable#copy()
#*/
     Copyable copy():
        return self
    }




}
