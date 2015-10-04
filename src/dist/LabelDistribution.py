

#/**
#* A distribution that acts on the label of the instance
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class LabelDistribution extends AbstractDistribution (Copyable):
    
#/**
#* The distribution
#*/
    Distribution dist
    
#/**
#* Make a new label distribution
#* @param dist the distribution
#*/
     LabelDistribution(Distribution dist):
        self.dist = dist
    }

#/**
#* @see dist.Distribution#probabilityOf(shared.Instance)
#*/
     double p(Instance i):
        return dist.p(i.getLabel())
    }

#/**
#* @see dist.Distribution#logLikelihood(shared.Instance)
#*/
     double logp(Instance i):
        return dist.logp(i.getLabel())
    }

#/**
#* @see dist.Distribution#generateRandom(shared.Instance)
#*/
     Instance sample(Instance i):
        return dist.sample(i.getLabel())
    }
   
#/**
#* @see dist.Distribution#mode(shared.Instance)
#*/ 
     Instance mode(Instance i):
        return dist.mode(i.getLabel())
    }

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
      estimate(DataSet observations):
        dist.estimate(observations.getLabelDataSet())
    }

#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return "Label Distribution " + dist.toString()
    }

#/**
#* @see shared.Copyable#copy()
#*/
     Copyable copy():
        return new LabelDistribution((Distribution) ((Copyable) dist).copy())
    }
    
#/**
#* Get the distribution
#* @return returns the distribution
#*/
     Distribution getDistribution():
        return dist
    }
#/**
#* Set the distribution
#* @param dist The distribution to set
#*/
      setDistribution(Distribution dist):
        self.dist = dist
    }
}
