

#/**
#* An evaluation function that uses a neural network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class NeuralNetworkEvaluationFunction:
#/**
#* The network
#*/
   # NeuralNetwork network
#/**
#* The examples
#*/
    #DataSet examples
#/**
#* The error measure
#*/#
   # ErrorMeasure measure
    
#/**
#* Make a new neural network evaluation function
#* @param network the network
#* @param examples the examples
#* @param measure the error measure
#*/
     def __init__(self,network, examples, measure):
        self.network = network
        self.examples = examples
        self.measure = measure
    

#/**
#* @see opt.OptimizationProblem#value(opt.OptimizationData)
#*/
     def value(self, d):
        #// set the links
        weights = d.getData()
        self.network.setWeights(weights)
       #// calculate the error
        error = 0
        for i in range(len(self.examples)):
            self.network.setInputValues(self.examples.get(i).getData())
            self.network.run()
            error += self.measure.value(Instance(network.getOutputValues()), self.examples.get(i))
        
        #// the fitness is 1 / error
        return 1.0 / error
