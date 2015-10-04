

#/**
#* A filter that performs a random projection
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class RandomizedProjectionFilter (ReversibleFilter):
#/**
#* The projection itself
#*/
    Matrix projection
#/**
#* Make a new random projection
#* @param componentsOut the number of components to keep
#* @param componentsIn the number of original components
#*/
     RandomizedProjectionFilter(int componentsOut, int componentsIn){
        projection = RectangularMatrix.random(componentsOut, componentsIn)
        projection.minusEquals(RectangularMatrix.ones(projection.m(), projection.n()).times(.5))
        SingularValueDecomposition svd = new SingularValueDecomposition(projection)
        if (componentsIn <= componentsOut):
            projection = svd.getU().get(0,projection.m(),0,projection.n())
        } else {
            projection = svd.getV().get(0,projection.m(),0,projection.n())
        }
    }

#/**
#* @see shared.filt.DataSetFilter#filter(shared.DataSet)
#*/
      filter(DataSet dataSet):
        for (int i = 0 i < dataSet.size() i++):
            Instance instance = dataSet.get(i)
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
        }
        dataSet.setDescription(new DataSetDescription(dataSet))
    }

#/**
#* Get the projection
#* @return the projection
#*/
     Matrix getProjection():
        return projection
    }



}
