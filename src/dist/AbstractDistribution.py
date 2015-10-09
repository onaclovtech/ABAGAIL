from src.util.linalg.Vector import *

#/**
#* An abstract distribution
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class AbstractDistribution:
    
#/**
#* @see dist.Distribution#logp(shared.Instance)
#*/
     def logp(i):
        p = p(i)
        logp = Math.log(p)
        if (Double.isInfinite(logp)):
            return -Double.MAX_VALUE
        
        return logp
    
    
#/**
#* Get an unconditional sample
#* @return the unconditional sample
#*/
     def sample(self):
        return sample(None)
    
    
#/**
#* Get an unconditional sample
#* @return the unconditional sample
#*/
     def mode(self):
        return mode(None)
    
