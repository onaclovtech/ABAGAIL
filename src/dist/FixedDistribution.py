

#/**
#* A distribution that does not reestimate
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class FixedDistribution extends AbstractDistribution (Copyable):
    
#/**
#* The distribution
#*/
    Distribution dist
    
#/**
#* Make a new label distribution
#* @param dist the distribution
#*/
     FixedDistribution(Distribution dist):
        self.dist = dist
    }

#/**
#* @see dist.Distribution#probabilityOf(shared.Instance)
#*/
     double p(Instance i):
        return dist.p(i)
    }

#/**
#* @see dist.Distribution#logLikelihood(shared.Instance)
#*/
     double logp(Instance i):
        return dist.logp(i)
    }

#/**
#* @see dist.Distribution#generateRandom(shared.Instance)
#*/
     Instance sample(Instance i):
        return dist.sample(i)
    }
   
#/**
#* @see dist.Distribution#mode(shared.Instance)
#*/ 
     Instance mode(Instance i):
        return dist.mode(i)
    }

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
      estimate(DataSet observations):
        return
    }

#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return "Fixed Distribution " + dist.toString()
    }

#/**
#* @see shared.Copyable#copy()
#*/
     Copyable copy():
        return new FixedDistribution((Distribution) ((Copyable) dist).copy())
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
