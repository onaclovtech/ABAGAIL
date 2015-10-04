

#/**
#* A four peaks evaluation function
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class FourPeaksEvaluationFunction (EvaluationFunction):
#/**
#* The t value
#*/
    int t
    
#/**
#* Make a new four peaks function
#* @param t the t value
#*/
     FourPeaksEvaluationFunction(int t):
        self.t = t
    }

#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     double value(Instance d):
        Vector data = d.getData()
        int i = 0
        while (i < data.size() && data.get(i) == 1):
            i++
        }
        int head = i
        i = data.size() - 1
        while (i >= 0 && data.get(i) == 0):
            i--
        }
        int tail = data.size() - 1 - i
        int r = 0
        if (head > t && tail > t):
            r = data.size()
        }
        return Math.max(tail, head) + r
    }
    
    
}
