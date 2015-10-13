

#/**
#* A checker board evaluation function
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class KnapsackEvaluationFunction:
    
#/**
#* The weights for the things that can be put in the sack
#*/
#    double[] weights
    
#/**
#* The volumes for the things that can be put in the sack
#*/
 #   double[] volumes
    
#/**
#* The maximum volume in the knapsack
#*/
  #  double maxVolume
    
#/**
#* The maximum sum of all items
#*/
   # double maxVolumeSum
    
#/**
#* Make a new knapsack evaluation function
#* @param w the set of values
#* @param v the set of volumes
#* @param maxV the maximum volumes
#* @param maxC the maximum counts
#*/
     def __init__(self, w, v, maxV, maxC):
        # double[] w, double[] v, double maxV, int[] maxC
        self.weights = w
        self.volumes = v
        self.maxVolume = maxV
        self.maxVolumeSum = 0.0
        for i in range(len(v)):
            self.maxVolumeSum += maxC[i] * v[i]
        
    

#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     def value(self, d):
        # Instance d
        data = d.getData()
        volume = 0.0
        value = 0.0
        for i in range(data.size()):
            volume += self.volumes[i] * data.get(i)
            value += self.weights[i] * data.get(i)
        
        if (volume > self.maxVolume):
            smallNumber = 1E-10
            return smallNumber*(self.maxVolumeSum - volume)
        else:
            return value
        