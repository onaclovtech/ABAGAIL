

#/**
#* A gaussian process regression
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class GaussianProcessRegression extends AbstractConditionalDistribution (FunctionApproximater):
#/**
#* The kernel
#*/
    Kernel kernel
#/**
#* The noise sigma
#*/
    double noiseSigma
#/**
#* The kernel matrix
#*/
    Matrix c
#/**
#* The cholesky factorization of the kernel matrix
#*/
    CholeskyFactorization cf
#/**
#* The a values
#*/
    Vector a
    
#/**
#* Make a new gaussian process regression
#* @param k the kernel to use
#* @param noise the noise sigma value
#*/
     GaussianProcessRegression(Kernel k, double noise):
        self.kernel = k
        self.noiseSigma = noise
    }
#/**
#* Make a new default gaussian process regression
#*/
     GaussianProcessRegression():
        self(new LinearKernel(), 1)
    }
#/**
#* @see func.FunctionApproximater#estimate(shared.DataSet)
#*/
      estimate(DataSet set):
        // make the kernel matrix
        c = new RectangularMatrix(set.size(), set.size())
        kernel.setExamples(set)
        for (int i = 0 i < c.m() i++):
            for (int j = 0 j < c.n() j++):
                c.set(i,j, kernel.value(i,j))
            }
        }
        // add in the noise
        c.plusEquals(RectangularMatrix.eye(set.size()).times(noiseSigma * noiseSigma))
        // make the target vector
        Vector t = new DenseVector(set.size())
        for (int i = 0 i < t.size() i++):
            t.set(i, set.get(i).getLabel().getContinuous())
        }
        // solve for the weights
        cf = new CholeskyFactorization(c)
        a = cf.solve(t)
    }
    
#/**
#* @see func.FunctionApproximater#value(shared.Instance)
#*/
     Instance value(Instance i):
        return distributionFor(i).mode()
    }
    
#/**
#* @see dist.ConditionalDistribution#distributionFor(shared.Instance)
#*/
     Distribution distributionFor(Instance instance):
        Vector k = new DenseVector(c.m())
        for (int i = 0 i < k.size() i++):
            k.set(i, kernel.value(i, instance))
        }        
        double mean = a.dotProduct(k)
        double sigma = Math.sqrt(
            kernel.value(instance, instance) - k.dotProduct(cf.solve(k)))
        return new UnivariateGaussian(mean, sigma)
    }
    

}
