

#/**
#* A feed forward layer in a neural network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class FeedForwardLayer extends Layer {

#/** 
#* Feed foward all of the nodes in self layer.
#*/
      feedforward():
        for (int i = 0 i < getNodeCount() i++):
            ((FeedForwardNode) getNode(i)).feedforward()
        }
    }

}
