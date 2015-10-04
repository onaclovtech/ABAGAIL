

#/**
#* A filter that performs PCA on a set of data
#* and then keeps the smallest eigenvalues instead of
#* the largest
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class InsignificantComponentAnalysis (ReversibleFilter):
#/**
#* The default threshold
#*/
    static final double THRESHOLD = Double.MAX_VALUE
    
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
     InsignificantComponentAnalysis(DataSet dataSet, int toKeep, double threshold):
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
        int belowThreshold = 0
        while (belowThreshold < toKeep && 
                 eigenValues.get(eigenValues.m() - belowThreshold - 1, 
                     eigenValues.m() - belowThreshold - 1) < threshold):
            belowThreshold++
        }
        toKeep = Math.min(toKeep, belowThreshold)
        projection = new RectangularMatrix(toKeep, eigenVectors.m())
        for (int i = eigenVectors.m() - 1 eigenVectors.m() - i  - 1 < toKeep i--):
            projection.setRow(eigenVectors.m() - i - 1, eigenVectors.getColumn(i))
        }
    }
    
     InsignificantComponentAnalysis(DataSet dataSet, double varianceToKeep):
        MultivariateGaussian mg = new MultivariateGaussian()
        mg.estimate(dataSet)
        Matrix covarianceMatrix = mg.getCovarianceMatrix()
        mean = mg.getMean()

        SymmetricEigenvalueDecomposition sed = 
            new SymmetricEigenvalueDecomposition(covarianceMatrix)
        Matrix eigenVectors = sed.getU()
        eigenValues = sed.getD()

        VarianceCounter vc = new VarianceCounter(eigenValues)
        int toKeep = vc.countRight(varianceToKeep)
        projection = new RectangularMatrix(toKeep, eigenVectors.m())
        for (int i = eigenVectors.m() - 1 eigenVectors.m() - i  - 1 < toKeep i--):
            projection.setRow(eigenVectors.m() - i - 1, eigenVectors.getColumn(i))
        }
    }

#/**
#* Make a new PCA filter
#* @param numberOfComponents the number to keep
#* @param set the data set to estimate components from
#*/
     InsignificantComponentAnalysis(DataSet set, int numberOfComponents):
        self(set, numberOfComponents, THRESHOLD)
    }

    
#/**
#* Make a new PCA filter
#* @param set the data set to estimate components from
#*/
     InsignificantComponentAnalysis(DataSet set):
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
