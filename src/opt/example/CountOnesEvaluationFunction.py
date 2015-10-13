

#/**
#* A function that counts the ones in the data
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class CountOnesEvaluationFunction:
#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     def value(self, d):
        data = d.getData()
        val = 0.0
        for i  in range(data.size()):
            if (data.get(i) == 1):
                val = val + 1
        return val
