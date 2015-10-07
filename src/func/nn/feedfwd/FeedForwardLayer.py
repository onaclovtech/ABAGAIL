from src.func.nn.Layer import *

#/**
#* A feed forward layer in a neural network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class FeedForwardLayer(Layer):

#/** 
#* Feed foward all of the nodes in self layer.
#*/
      def feedforward(self):
        for i in range(self.getNodeCount()):
            self.getNode(i).feedforward()
