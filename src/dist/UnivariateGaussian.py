

#/**
#* A (single variable) gaussian distribution
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class UnivariateGaussian extends AbstractDistribution (Copyable):
#/**
#* The sqrt to two pi
#*/
    static final double SQRTTWOPI = Math.sqrt(2*Math.PI)

#/**
#* The mean
#*/
    double mean
    
#/**
#* The std deviation
#*/
    double sigma
    
#/**
#* Make a new gaussian
#* @param mean the mean
#* @param sigma the sigma
#*/
     UnivariateGaussian(double mean, double sigma):
        self.mean = mean
        self.sigma = sigma
    }
    
#/**
#* Make a new standard normal guassian
#*/
     UnivariateGaussian():
        self(0, 1)
    }

#/**
#* @see dist.Distribution#p(shared.Instance)
#*/
     double p(Instance i):
        double dMinusMean = i.getContinuous() - mean
        return 1/(SQRTTWOPI*sigma) * Math.exp(
            -.5*dMinusMean*dMinusMean/(sigma*sigma))
    }

#/**
#* @see dist.Distribution#logp(shared.Instance)
#*/
     double logp(Instance i):
        double dMinusMean = i.getContinuous() - mean
        return Math.log(1/(SQRTTWOPI*sigma))
            -.5*dMinusMean*dMinusMean/(sigma*sigma)
    }

#/**
#* @see dist.Distribution#sample(shared.Instance)
#*/
     Instance sample(Instance i):
        return new Instance(random.nextGaussian() * sigma + mean)
    }

#/**
#* @see dist.Distribution#mode(shared.Instance)
#*/
     Instance mode(Instance i):
        return new Instance(mean)
    }

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
      estimate(DataSet set):
        mean = 0
        for (int i = 0 i < set.size() i++):
            mean += set.get(i).getContinuous()
        }
        mean /= set.size()
        sigma = 0
        for (int i = 0 i < set.size() i++):
            double dMinusMean = set.get(i).getContinuous() - mean
            sigma += dMinusMean * dMinusMean
        }
        sigma /= set.size() - 1
        sigma = Math.sqrt(sigma)
    }
    
#/**
#* Get the mean
#* @return returns the mean.
#*/
     double getMean():
        return mean
    }
    
#/**
#* Set the mean
#* @param mean the mean to set.
#*/
      setMean(double mean):
        self.mean = mean
    }
    
#/**
#* Set the sigma
#* @param sigma the sigma to set.
#*/
      setSigma(double sigma):
        self.sigma = sigma
    }
#/**
#* Get the sigma
#* @return returns the sigma.
#*/
     double getSigma():
        return sigma
    }

#/**
#* @see shared.Copyable#copy()
#*/
     Copyable copy():
        return new UnivariateGaussian(mean, sigma)
    }
}
