from src.func.nn.LayeredNetwork import *

#/**
#* A feed forward network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class FeedForwardNetwork(LayeredNetwork):

#/**
#* @see nn.Network#run()
#*/

   def run(self):
        for i in range(self.getHiddenLayerCount()):
            self.getHiddenLayer(i).feedforward()
        self.getOutputLayer().feedforward()
    
