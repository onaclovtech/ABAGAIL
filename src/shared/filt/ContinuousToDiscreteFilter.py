

#/**
#* A continuous to discrete filter
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class ContinuousToDiscreteFilter (DataSetFilter):
#/**
#* The number of bins
#*/
    int numberOfBins
    
#/**
#* Make a new continuous to discrete filter
#* @param numberOfBins the number of bins
#*/
     ContinuousToDiscreteFilter(int numberOfBins):
        self.numberOfBins = numberOfBins
    }

#/**
#* @see shared.filt.DataSetFilter#filter(shared.DataSet)
#*/
      filter(DataSet dataSet):
        if (dataSet.getDescription() == null):
            dataSet.setDescription(new DataSetDescription(dataSet))
        }
        DataSetDescription oldDescription = dataSet.getDescription()
        // for each instance
        for (int i = 0 i < dataSet.size() i++):
            Instance instance = dataSet.get(i)
            for (int j = 0 j < oldDescription.getAttributeCount() j++):
                if (oldDescription.getAttributeTypes()[j] == AttributeType.CONTINUOUS):
                    double cv = instance.getContinuous(j)
                    int dv = (int) ((cv - oldDescription.getMin(j)) 
#* numberOfBins / oldDescription.getRange(j))
                    instance.getData().set(j, dv)
                }
            }
        }
        
        // the description is no longer valid so generate a new one
        dataSet.setDescription(new DataSetDescription(dataSet))
        dataSet.getDescription().setLabelDescription(new DataSetDescription(dataSet.getLabelDataSet()))
    }
}
