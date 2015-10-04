

#/**
#* A filter that replaces data with a class distribution
#* from a classifier
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class DiscreteDistributionFilter (DataSetFilter):
#/**
#* The classifier in use
#*/
    ConditionalDistribution classifier
    
#/**
#* Make a new classifier filter
#* @param classifier the classifier
#*/
     DiscreteDistributionFilter(ConditionalDistribution classifier):
        self.classifier = classifier
    }

#/**
#* @see shared.filt.DataSetFilter#filter(shared.DataSet)
#*/
      filter(DataSet dataSet):
        for (int i = 0 i < dataSet.size() i++):
            Instance instance = dataSet.get(i)
            Distribution dist = classifier.distributionFor(instance)
            instance.setData(new DenseVector(
                ((DiscreteDistribution) dist).getProbabilities()))
        }
    }
    

}
