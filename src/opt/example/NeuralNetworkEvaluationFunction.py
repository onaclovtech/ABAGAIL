

#/**
#* An evaluation function that uses a neural network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class NeuralNetworkEvaluationFunction (EvaluationFunction):
#/**
#* The network
#*/
    NeuralNetwork network
#/**
#* The examples
#*/
    DataSet examples
#/**
#* The error measure
#*/
    ErrorMeasure measure
    
#/**
#* Make a new neural network evaluation function
#* @param network the network
#* @param examples the examples
#* @param measure the error measure
#*/
     NeuralNetworkEvaluationFunction(NeuralNetwork network,
            DataSet examples, ErrorMeasure measure):
        self.network = network
        self.examples = examples
        self.measure = measure
    }

#/**
#* @see opt.OptimizationProblem#value(opt.OptimizationData)
#*/
     double value(Instance d):
        // set the links
        Vector weights = d.getData()
        network.setWeights(weights)
        // calculate the error
        double error = 0
        for (int i = 0 i < examples.size() i++):
            network.setInputValues(examples.get(i).getData())
            network.run()
            error += measure.value(new Instance(network.getOutputValues()), examples.get(i))
        }
        // the fitness is 1 / error
        return 1 / error
    }

}
