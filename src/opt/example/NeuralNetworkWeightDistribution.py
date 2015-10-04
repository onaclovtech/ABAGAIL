


#/**
#* A distribution for neural network weights
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class NeuralNetworkWeightDistribution extends AbstractDistribution {
   
#/** 
#* The weight count
#*/ 
    int weightCount
    
#/**
#* Make a new neural network weight distribution
#* @param weightCount the weight count
#*/
     NeuralNetworkWeightDistribution(int weightCount):
        self.weightCount = weightCount
    }

#/**
#* @see dist.Distribution#probabilityOf(shared.Instance)
#*/
     double p(Instance i):
        return 1
    }

#/**
#* @see dist.Distribution#generateRandom(shared.Instance)
#*/
     Instance sample(Instance ignored):
        double[] weights = new double[weightCount]
        for (int i = 0 i < weights.length i++):
            weights[i] = random.nextDouble() - .5
        }
        return new Instance(weights)
    }

#/**
#* @see dist.Distribution#generateMostLikely(shared.Instance)
#*/
     Instance mode(Instance ignored):
        return sample(ignored)
    }

#/**
#* @see dist.Distribution#estimate(shared.DataSet)
#*/
      estimate(DataSet observations):
        return
    }
    
    

}
