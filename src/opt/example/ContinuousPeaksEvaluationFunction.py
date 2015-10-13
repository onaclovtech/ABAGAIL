

#/**
#* A continuous peaks function
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class ContinuousPeaksEvaluationFunction:
#/**
#* The t value
#*/
 #   int t
    
#/**
#* Make a new continuous peaks function
#* @param t the t value
#*/
     def __init__(self, t):
        self.t = t
    

#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     def value(self, d):
        data = d.getData()
        max0 = 0
        count = 0
        for i  in range(data.size()):
            if (data.get(i) == 0):
                count = count + 1
            else:
                if (count > max0):
                    max0 = count
                    count = 0
        max1 = 0
        count = 0
        for i  in range(data.size()):
            if (data.get(i) == 1):
                count = count + 1
            else:
                if (count > max1):
                    max1 = count
                    count = 0
        r = 0
        if (max1 > self.t and max0 > self.t):
            r = data.size()
        
        return max(max1, max0) + r