from src.func.nn.backprop.BackPropagationLayer import *
from src.func.nn.activation.LogisticSigmoid import *
from src.func.nn.activation.HyperbolicTangentSigmoid import *
from src.func.nn.backprop.BackPropagationNetwork import *
from src.func.nn.backprop.BackPropagationNode import *
from src.func.nn.backprop.BackPropagationBiasNode import *


#/**
#* A multi layer perceptron factory
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class BackPropagationNetworkFactory:

#/**
#* Create a multilayer perceptron
#* @param nodeCounts the number of nodes in each layer
#* @param transfer the transfer function
#* @param outputLayer the output layer of the network
#* @param outputFunction the output transfer function
#* @return a multilayer perceptron with nodeCounts.length layers
#*/
   def createNetwork(self, nodeCounts, transfer, outputLayer, outputFunction):
         #if (nodeCounts.length < 2):
         #   throw IllegalArgumentException()
         network = BackPropagationNetwork()
         
           # create the input layer
         inputLayer =  BackPropagationLayer()
         for i in range(nodeCounts[0]):
            inputLayer.addNode(BackPropagationNode(None))
         
         inputLayer.addNode(BackPropagationBiasNode(transfer, 1))
         network.setInputLayer(inputLayer)
         #print 'BackPropagationNetworkFactory.createNetwork.network.getInputLayer()' + str(network.getInputLayer())
           
         # create hidden layers
         for i in range(len(nodeCounts)):
            hiddenLayer = BackPropagationLayer()
            for j in range(nodeCounts[i]):
               hiddenLayer.addNode(BackPropagationNode(transfer))
               #print "BackPropagationNetworkFactory.createNetwork.hiddenLayer.getNode().getActivationFunction()" + str(hiddenLayer.getNode(j).getActivationFunction())
            hiddenLayer.addNode(BackPropagationBiasNode(transfer, 1))
            network.addHiddenLayer(hiddenLayer)
            #print 'BackPropagationNetworkFactory.createNetwork.network.getHiddenLayer()' + str(network.getHiddenLayer(i).)
           
           # create the output layer
         for i in range(nodeCounts[-1]):
            outputLayer.addNode(BackPropagationNode(outputFunction))
         network.setOutputLayer(outputLayer)
         #print 'BackPropagationNetworkFactory.createNetwork.network.getOutputLayer()' + str(network.getOutputLayer())
         network.connect()
         return network
      
    
#/**
#* Create a multilayer perceptron
#* @param nodeCounts the number of nodes in each layer
#* @param transfer the transfer function
#* @return a multilayer perceptron with nodeCounts.length layers
#*/
   def createRegressionNetwork(self, nodeCounts, transfer = None):
        if transfer:
         return self.createNetwork(nodeCounts, transfer, BackPropagationLayer(),LinearActivationFunction())
        else:
         return self.createRegressionNetwork(nodeCounts, HyperbolicTangentSigmoid())

#/**
#* Create a multilayer perceptron
#* with a softmax output layer
#* @param nodeCounts the number of nodes in each layer
#* @param transfer the transfer function
#* @return a multilayer perceptron with nodeCounts.length layers
#*/
   def createClassificationNetwork(self, nodeCounts, transfer = None):
       if transfer is None:
         return self.createClassificationNetwork(nodeCounts, HyperbolicTangentSigmoid())
       if (nodeCounts[-1] == 1):
           return self.createNetwork(nodeCounts, transfer, BackPropagationLayer(), LogisticSigmoid())     
       else:
           return self.createNetwork(nodeCounts, transfer, BackPropagationSoftMaxOutputLayer(),
               LinearActivationFunction())
   
    