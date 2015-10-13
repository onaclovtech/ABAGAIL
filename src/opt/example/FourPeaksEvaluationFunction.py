

#/**
#* A four peaks evaluation function
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class FourPeaksEvaluationFunction:
#/**
#* The t value
#*/
#    int t
    
#/**
#* Make a new four peaks function
#* @param t the t value
#*/
     def __init__(self, t):
        self.t = t

#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     def value(self, d):
        data = d.getData()
        i = 0
        while (i < data.size() and data.get(i) == 1):
            i = i + 1
        head = i
        i = data.size() - 1
        while (i >= 0 and data.get(i) == 0):
            i = i - 1 
        
        tail = data.size() - 1 - i
        r = 0
        if (head > self.t and tail > self.t):
            r = data.size()
        
        return max(tail, head) + r