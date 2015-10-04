

#/**
#* A continuous peaks function
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class ContinuousPeaksEvaluationFunction (EvaluationFunction):
#/**
#* The t value
#*/
    int t
    
#/**
#* Make a new continuous peaks function
#* @param t the t value
#*/
     ContinuousPeaksEvaluationFunction(int t):
        self.t = t
    }

#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     double value(Instance d):
        Vector data = d.getData()
        int max0 = 0
        int count = 0
        for (int i = 0 i < data.size() i++):
            if (data.get(i) == 0):
                count++
            } else {
                if (count > max0):
                    max0 = count
                    count = 0
                }
            }
        }
        int max1 = 0
       count = 0
        for (int i = 0 i < data.size() i++):
            if (data.get(i) == 1):
                count++
            } else {
                if (count > max1):
                    max1 = count
                    count = 0
                }
            }
        }
        int r = 0
        if (max1 > t && max0 > t):
            r = data.size()
        }
        return Math.max(max1, max0) + r
    }
}
