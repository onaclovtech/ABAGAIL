

#/**
#* An abstract distribution
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 abstract class AbstractDistribution (Distribution):
    
#/**
#* @see dist.Distribution#logp(shared.Instance)
#*/
     double logp(Instance i):
        double p = p(i)
        double logp = Math.log(p)
        if (Double.isInfinite(logp)):
            return -Double.MAX_VALUE
        }
        return logp
    }
    
#/**
#* Get an unconditional sample
#* @return the unconditional sample
#*/
     Instance sample():
        return sample(null)
    }
    
#/**
#* Get an unconditional sample
#* @return the unconditional sample
#*/
     Instance mode():
        return mode(null)
    }

}
