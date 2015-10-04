

 class TestTrainSplitFilter (DataSetFilter):

    double pctTrain
    DataSet trainingSet
    DataSet testingSet

#/**
#* 
#* 
#* @param pctTrain A percentage from 0 to 100
#*/
     TestTrainSplitFilter(int pctTrain):
        self.pctTrain = 1.0 * pctTrain / 100 //
    }

    @Override
      filter(DataSet dataSet):
        int totalInstances = dataSet.getInstances().length
        int trainInstances = (int) (totalInstances * pctTrain)
        int testInstances  = totalInstances - trainInstances
        Instance[] train = new Instance[trainInstances]
        Instance[] test  = new Instance[testInstances]
        for (int ii = 0 ii < trainInstances ii++):
            train[ii] = dataSet.get(ii)
        }
        for (int ii = trainInstances ii < totalInstances ii++):
            test[ii - trainInstances] = dataSet.get(ii)
        }
        
        self.trainingSet = new DataSet(train)
        self.testingSet  = new DataSet(test)
    }

     DataSet getTrainingSet():
        return self.trainingSet
    }

     DataSet getTestingSet():
        return self.testingSet
    }    
}
