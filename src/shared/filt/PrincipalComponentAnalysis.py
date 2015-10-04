

#/**
#* A filter that performs PCA on a set of data
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class PrincipalComponentAnalysis (ReversibleFilter):
#/**
#* The default threshold
#*/
    static final double THRESHOLD = 1E-6
    
#/**
#* The projection matrix
#*/
    Matrix projection
    
#/**
#* The eigen value matrix
#*/
    Matrix eigenValues
    
#/**
#* The mean vector
#*/
    Vector mean
    
#/**
#* Make a new PCA filter
#* @param toKeep the number of components to keep
#* @param dataSet the set form which to estimate components
#*/
     PrincipalComponentAnalysis(DataSet dataSet, int toKeep, double threshold):
        MultivariateGaussian mg = new MultivariateGaussian()
        mg.estimate(dataSet)
        Matrix covarianceMatrix = mg.getCovarianceMatrix()
        mean = mg.getMean()
        if (toKeep == -1):
            toKeep = mean.size()
        }
        SymmetricEigenvalueDecomposition sed = 
            new SymmetricEigenvalueDecomposition(covarianceMatrix)
        Matrix eigenVectors = sed.getU()
        eigenValues = sed.getD()
        int aboveThreshold = 0
        while (aboveThreshold < toKeep && 
                 eigenValues.get(aboveThreshold, aboveThreshold) > threshold):
            aboveThreshold++
        }
        toKeep = Math.min(toKeep, aboveThreshold)
        projection = new RectangularMatrix(toKeep, eigenVectors.m())
        for (int i = 0 i < toKeep i++):
            projection.setRow(i, eigenVectors.getColumn(i))
        }
    }
    
#/**
#* Make a new PCA filter
#* @param varianceToKeep The % variance to keep.  This assumes that sum(eigenvalues) represents all of the variance, and 
#* @param dataSet the set form which to estimate components
#*/
     PrincipalComponentAnalysis(DataSet dataSet, double varianceToKeep):
        MultivariateGaussian mg = new MultivariateGaussian()
        mg.estimate(dataSet)
        Matrix covarianceMatrix = mg.getCovarianceMatrix()
        mean = mg.getMean()
//        if (toKeep == -1):
//            toKeep = mean.size()
//        }
        SymmetricEigenvalueDecomposition sed = 
            new SymmetricEigenvalueDecomposition(covarianceMatrix)
        Matrix eigenVectors = sed.getU()
        eigenValues = sed.getD()

        VarianceCounter vc = new VarianceCounter(eigenValues)
        int toKeep = vc.countLeft(varianceToKeep)
        projection = new RectangularMatrix(toKeep, eigenVectors.m())
        for (int i = 0 i < toKeep i++):
            projection.setRow(i, eigenVectors.getColumn(i))
        }
    }
    
#/**
#* Make a new PCA filter
#* @param numberOfComponents the number to keep
#* @param set the data set to estimate components from
#*/
     PrincipalComponentAnalysis(DataSet set, int numberOfComponents):
        self(set, numberOfComponents, THRESHOLD)
    }

    
#/**
#* Make a new PCA filter
#* @param set the data set to estimate components from
#*/
     PrincipalComponentAnalysis(DataSet set):
        self(set, -1)
    }

#/**
#* @see shared.filt.DataSetFilter#filter(shared.DataSet)
#*/
      filter(DataSet dataSet):
        for (int i = 0 i < dataSet.size() i++):
            Instance instance = dataSet.get(i)
            instance.setData(instance.getData().minus(mean))
            instance.setData(projection.times(instance.getData()))
        }
        dataSet.setDescription(new DataSetDescription(dataSet))
    }
   

#/**
#* @see shared.filt.ReversibleFilter#reverse(shared.DataSet)
#*/
      reverse(DataSet dataSet):
        for (int i = 0 i < dataSet.size() i++):
            Instance instance = dataSet.get(i)
            instance.setData(projection.transpose().times(instance.getData()))
            instance.setData(instance.getData().plus(mean))
        }
        dataSet.setDescription(new DataSetDescription(dataSet))
    }

#/**
#* Get the projection matrix used
#* @return the projection matrix
#*/
     Matrix getProjection():
        return projection
    }
    
#/**
#* Get the mean
#* @return the mean
#*/
     Vector getMean():
        return mean
    }

#/**
#* Get the eigenvalues
#* @return the eigenvalues
#*/
     Matrix getEigenValues():
        return eigenValues
    }


}
