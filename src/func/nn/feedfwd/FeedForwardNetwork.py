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
            print "FeedForwardNetwork.self.getHiddenLayer(i).__class__" + str(self.getHiddenLayer(i).__class__)
            self.getHiddenLayer(i).feedforward()
        self.getOutputLayer().feedforward()
    
