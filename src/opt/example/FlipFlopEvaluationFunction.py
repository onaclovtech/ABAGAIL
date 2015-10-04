

#/**
#* A function that counts the ones in the data
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class FlipFlopEvaluationFunction (EvaluationFunction):
#/**
#* @see opt.EvaluationFunction#value(opt.OptimizationData)
#*/
     double value(Instance d):
        Vector data = d.getData()
        double val = 0
        for (int i = 0 i < data.size() - 1 i++):
            if (data.get(i) != data.get(i + 1)):
                val++
            }
        }
        return val
    }
}
