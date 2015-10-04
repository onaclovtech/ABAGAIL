

#/**
#* A checker board evaluation function
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class KnapsackEvaluationFunction (EvaluationFunction):
    
#/**
#* The weights for the things that can be put in the sack
#*/
    double[] weights
    
#/**
#* The volumes for the things that can be put in the sack
#*/
    double[] volumes
    
#/**
#* The maximum volume in the knapsack
#*/
    double maxVolume
    
#/**
#* The maximum sum of all items
#*/
    double maxVolumeSum
    
#/**
#* Make a new knapsack evaluation function
#* @param w the set of values
#* @param v the set of volumes
#* @param maxV the maximum volumes
#* @param maxC the maximum counts
#*/
     KnapsackEvaluationFunction(double[] w, double[] v, double maxV,
            int[] maxC):
        weights = w
        volumes = v
        maxVolume = maxV
        for (int i = 0 i < v.length i++):
            maxVolumeSum += maxC[i] * v[i]
        }
    }

#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     double value(Instance d):
        Vector data = d.getData()
        double volume = 0
        double value = 0
        for (int i = 0 i < data.size() i++):
            volume += volumes[i] * data.get(i)
            value += weights[i] * data.get(i)
        }
        if (volume > maxVolume):
            double smallNumber = 1E-10
            return smallNumber*(maxVolumeSum - volume)
        } else {
            return value
        }
        
    }

}
