from src.shared.Instance import *

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
        #print "neuralnetworkevalfunc.__init__.examples" + str(examples.__class__)
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
        for i in range(self.examples.size()):
            self.network.setInputValues(self.examples.get(i).getData())
            #print 'NNEvalFunction.self.network.run()' + str(self.network.__class__)
            print 'NNEvalFunction.self.examples.get(i).getData().toString()' + str(self.examples.get(i).getData().toString())
            self.network.run()
            error += self.measure.value(Instance(self.network.getOutputValues()), self.examples.get(i))
        
        #// the fitness is 1 / error
        return 1.0 / error
