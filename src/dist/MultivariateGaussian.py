

#/**
#* A multivariate gaussian distribution
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class MultivariateGaussian extends AbstractDistribution  (Copyable):
#/**
#* The default floor
#*/
    static final double FLOOR = .01
#/**
#* The change in floor
#*/
    static final double FLOOR_CHANGE = 10
    
#/**
#* The mean of the gaussian
#*/
    Vector mean
    
#/**
#* The covariance matrix
#*/
    Matrix covarianceMatrix
    
#/**
#* The decomposition of the covariance
#*/
    CholeskyFactorization decomposition
    
#/**
#* The determinant
#*/
    double determinant
    
#/**
#* The minimum allowed value in the covariance matrices
#*/
    double floor
    
#/**
#* Whether to print lots of stuff out
#*/
    boolean debug
    
#/**
#* Make a new multivariate gaussian
#* @param mean the mean
#* @param covariance the covariance
#*/
     MultivariateGaussian(Vector mean, Matrix covariance, double floor):
        self.mean = mean
        self.covarianceMatrix = covariance
        self.floor = floor
        decomposition = new CholeskyFactorization(covariance)
        determinant = decomposition.determinant()
    }
    
#/**
#* Make a new multivariate gaussian
#* @param mean the mean
#* @param covariance the covariance
#*/
     MultivariateGaussian(Vector mean, Matrix covariance):
        self(mean, covariance, 0)
    }
    
#/**
#* Make a new multivariate gaussian
#* @param floor the floor value
#*/
     MultivariateGaussian(double floor):
        self.floor = floor
    }
    
#/**
#* Make a new multivariate gaussian
#*/
     MultivariateGaussian():
    }

#/**
#* @see dist.Distribution#probabilityOf(shared.Instance)
#*/
     double p(Instance i):
        Vector d = i.getData()
        Vector dMinusMean = d.minus(mean)
        double p = 1/Math.sqrt(Math.pow(2*Math.PI, mean.size())* determinant)
#* Math.exp(-.5 * dMinusMean.dotProduct(decomposition.solve(dMinusMean)))
        return p
    }
    
#/**
#* Calculate the log likelihood
#* @param i the instance
#* @return the log likelihood
#*/
     double logp(Instance i):
        Vector d = i.getData()
        Vector dMinusMean = d.minus(mean)
        double p = Math.log(1/Math.sqrt(Math.pow(2*Math.PI, mean.size())* determinant))
                - .5 * dMinusMean.dotProduct(decomposition.solve(dMinusMean))
        return p
    }

#/**
#* @see dist.Distribution#generateRandom(shared.Instance)
#*/
     Instance sample(Instance ignored):
        Vector r = new DenseVector(mean.size())
        for (int i = 0 i < r.size() i++):
            r.set(i, random.nextGaussian())
        }
        return new Instance(decomposition.getL().times(r).plus(mean))
    }

#/**
#* @see dist.Distribution#generateMostLikely(shared.Instance)
#*/
     Instance mode(Instance ignored):
        return new Instance((Vector) mean.copy())
    }

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
      estimate(DataSet observations):
        double weightSum = 0
        // calculate mean
        mean = new DenseVector(observations.get(0).size())
        for (int t = 0 t < observations.size() t++):
            double weight = observations.get(t).getWeight()
            Vector d = observations.get(t).getData()
            for (int i = 0 i < mean.size() i++):
                mean.set(i, mean.get(i) + d.get(i) * weight)
            }
            weightSum += weight
        }
        mean.timesEquals(1/weightSum)
        // and covariance
        covarianceMatrix = new RectangularMatrix(mean.size(), mean.size())
        for (int t = 0 t < observations.size() t++):
            Vector d = observations.get(t).getData()
            double weight = observations.get(t).getWeight()
            Vector dMinusMean = d.minus(mean)
            for (int i = 0 i < covarianceMatrix.m() i++):
                for (int j = 0 j < covarianceMatrix.n() j++):
                    covarianceMatrix.set(i,j,
                        covarianceMatrix.get(i,j) +
                        dMinusMean.get(i) * dMinusMean.get(j) * weight)
                }
            }
        }
        covarianceMatrix.timesEquals(1/weightSum)
        boolean scale = false
        for (int i = 0 i < covarianceMatrix.m() i++):
            if (covarianceMatrix.get(i, i) < floor):
                scale = true
            }
        }
        if (scale):
            for (int i = 0 i < covarianceMatrix.m() i++):
                covarianceMatrix.set(i, i, covarianceMatrix.get(i,i) + floor)
            }
        }
        // decompose the covariance matrix
        decomposition = new CholeskyFactorization(covarianceMatrix)
        determinant = decomposition.determinant()
        // the matrix isn't positive
        if (determinant == 0 || Double.isNaN(determinant)):
            if (debug):
                System.out.println("Covariance matrix not positive, applying ridge adjustment")
                System.out.println(covarianceMatrix)
            }
            if (floor == 0):
                floor = FLOOR
            } else {
                floor *= FLOOR_CHANGE
            }
            // try again
            estimate(observations)
        }
    }
    
     String toString():
        return "mean =\n" + mean.toString()
            + "\ncovariance matrix =\n" + covarianceMatrix.toString()
    }

#/**
#* Get the covariance matrix
#* @return the covariance matrix
#*/
     Matrix getCovarianceMatrix():
        return covarianceMatrix
    }

#/**
#* Get the mean
#* @return the mean vector
#*/
     Vector getMean():
        return mean
    }

#/**
#* Set the covariance matrix
#* @param matrix the matrix
#*/
      setCovarianceMatrix(Matrix matrix):
        covarianceMatrix = matrix
    }

#/**
#* Set the mean vector
#* @param vector the new mean
#*/
      setMean(Vector vector):
        mean = vector
    }

#/**
#* Whether to print out lots of stuff
#* @return true if we should
#*/
     boolean isDebug():
        return debug
    }

#/**
#* Set the debug mode
#* @param b true if you want to see stuff printe dout
#*/
      setDebug(boolean b):
        debug = b
    }
    
     Copyable copy():
        return new MultivariateGaussian((Vector) mean.copy(), 
                    (Matrix) covarianceMatrix.copy(), floor)
    }

}
